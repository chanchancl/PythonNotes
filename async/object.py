
import asyncio

loop = asyncio.get_event_loop()


'''
If get_event_loop_policy == nil, then return DefaultEventLoopPolicy().get_event_loop()

In unix, DefaultEventLoopPolicy == _UnixDefaultEventLoopPolicy

_UnixDefaultEventLoopPolicy.get_event_loop -> BaseDefaultEventLoopPolicy.get_event_loop
    self.set_event_loop(self.new_event_loop())
        new_event_loop
            self._loop_factory()
                _loop_factory = _UnixSelectorEventLoop

_UnixSelectorEventLoop
    _selector = selectors.DefaultSelector()
        EpollSelector()


'''


