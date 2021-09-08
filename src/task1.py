import time
from collections import defaultdict


class Tracer:
    __runs = defaultdict(int)

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.f(*args, **kwargs)
        time_used = round(time.time() - start, 4)
        self.__runs[self.f.__name__] += 1
        print(f"{self.f.__name__} call {self.__runs[self.f.__name__]} executed in {time_used} sec")

        return result
