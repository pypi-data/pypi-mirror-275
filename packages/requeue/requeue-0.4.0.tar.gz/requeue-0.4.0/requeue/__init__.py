import asyncio
import inspect

from typing import Any, Awaitable, Callable, Optional, Union
from dataclasses import dataclass, field


type CheckCallable[*Ts] = Union[Callable[[*Ts], bool], Callable[[*Ts], Awaitable[bool]]]


@dataclass
class _Request[*Ts]:
    lock: asyncio.Lock = field(default_factory=asyncio.Lock)
    completed: asyncio.Event = field(default_factory=asyncio.Event)
    check: Optional[CheckCallable[*Ts]] = field(default=None)
    _check_signature: Optional[inspect.Signature] = field(default=None, init=False)
    result: Optional[tuple[*Ts]] = field(default=None)

    def __post_init__(self) -> None:
        if self.check is not None:
            self._check_signature = inspect.signature(self.check)

    async def validate(self, *contents: Any) -> bool:
        """
        Validate contents against check.
        """

        if self.check is None:
            return True

        try:
            self._check_signature.bind(*contents)
        except TypeError:
            # Failing to bind arguments should not
            # cause the validation to crash.
            return False

        valid = self.check(*contents)

        if inspect.isawaitable(valid):
            return await valid
        return valid


class Requeue[*Ts]:
    """
    An asynchronous queue for requesting data
    """

    def __init__(self, contents_filter: Optional[tuple[type, ...]] = None) -> None:
        self.contents_filter = contents_filter

        self._requests: list[_Request[*Ts]] = []
        self._lock = asyncio.Lock()

    async def wait_for(self,
        check: Optional[CheckCallable[*Ts]] = None,
        timeout: Optional[float] = None,
    ) -> tuple[*Ts]:
        """
        Make a request for data and wait for it.
        
        Optionally, apply a check to only permit data matching certain criteria.
        `check` should return a boolean of whether it is a match or not.
        """

        request = _Request(check=check)

        async with self._lock:
            self._requests.append(request)

        try:
            await asyncio.wait_for(request.completed.wait(), timeout=timeout)
            
            async with request.lock:
                return request.result

        finally:
            # In case the request is still found in the list,
            # signal to `complete` that the request has expired.
            request.completed.set()

            async with self._lock:
                self._requests.remove(request)

    def _validate_contents(self, *contents: Any) -> bool:
        """
        Validate contents against the contents filter.
        """

        if self.contents_filter is None:
            return True

        if len(contents) != len(self.contents_filter):
            return False

        for c, t in zip(contents, self.contents_filter):
            if not isinstance(c, t):
                return False

        return True

    async def complete(self, *contents: Any) -> bool:
        """
        Look for a matching request and complete it.
        Returns whether a request was completed.
        """
        
        if not self._validate_contents(*contents):
            raise TypeError('Contents contain invalid types.')

        async with self._lock:
            requests = self._requests[:]

        for request in requests:
            # Skip timed out requests.
            if request.completed.is_set():
                continue

            if not await request.validate(*contents):
                continue

            async with request.lock:
                request.result = contents

            # Signal that the request has been completed.
            request.completed.set()

            return True
        return False
