import time


class Timer:
    """
    Context Manager that can estimate execution time
    """

    def __init__(self):
        self.start = 0
        self.time_delta = 0

    def __enter__(self):
        self.time_delta = 0
        self.start = time.time()

    def __exit__(self, type, value, traceback):
        self.time_delta = round(time.time() - self.start, 4)


def log(information_blocks=[]):
    """
    Print basic information into STDOUT
    :param information_blocks: what we want to print
    """
    for block in information_blocks:
        print(block)


def tracer(context):
    def inner_function(f):
        def wrapper(*args, **kwargs):
            context["__runs"][f.__name__] += 1
            timer = Timer()
            with timer:
                output = f(*args, **kwargs)
            trace_info = (
                f"{f.__name__} call {context['__runs'][f.__name__]} executed in "
                f"{timer.time_delta} sec"
            )
            log([trace_info])
            return output

        return wrapper

    return inner_function
