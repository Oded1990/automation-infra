import time
import logging

log = logging.getLogger(__name__)


class TimeoutGenerator(object):
    def __init__(self, timeout, sleep, func, *func_args, **func_kwargs):
        self.timeout = timeout
        self.sleep = sleep
        if self.timeout < self.sleep:
            raise ValueError("timeout should be larger than sleep time")
        self.func = func
        self.func_args = func_args
        self.func_kwargs = func_kwargs
        self.start_time = None
        self.last_sample_time = None

    def __iter__(self):
        if self.start_time is None:
            self.start_time = time.time()
        while True:
            self.last_sample_time = time.time()
            if self.timeout <= (self.last_sample_time - self.start_time):
                raise TimeoutError
            yield self.func(*self.func_args, **self.func_kwargs)
            time.sleep(self.sleep)

    def wait_for_value(self, value):
        for i_value in self:
            if i_value == value:
                return True
