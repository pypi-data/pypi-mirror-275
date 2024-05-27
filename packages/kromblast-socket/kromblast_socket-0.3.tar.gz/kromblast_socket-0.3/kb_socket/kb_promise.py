from promise import Promise as BasePromise
from typing import Any, Callable, Optional
from promise.promise import T, STATE_PENDING, STATE_FULFILLED
from time import sleep


class Promise(BasePromise):
    is_executor: bool

    def __init__(self, executor: Optional[Callable[[Callable[[T], None],
                                                    Callable[[Exception],
                                                             None]],
                                                   None]] = None,
                 scheduler: Any = None) -> None:
        self.is_executor = executor is not None
        super().__init__(executor, scheduler)

    @classmethod
    def resolve(cls, obj):
        # type: (T) -> Promise[T]
        if not cls.is_thenable(obj):
            if cls.is_executor:
                ret = cls
            else:
                ret = cls()  # type: Promise
            # ret._capture_stacktrace()
            ret._state = STATE_FULFILLED
            ret._rejection_handler0 = obj
            return ret

        return cls._try_convert_to_promise(obj)

    @classmethod
    def wait(cls, promise: BasePromise,
             timeout: Optional[float] = None) -> None:
        if promise.is_executor:
            return super().wait(promise, timeout)
        while promise._state == STATE_PENDING:
            sleep(0.1)
