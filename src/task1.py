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


class Tracer:
    """
    The class that allows to trace function execution as decorator
    """

    def __init__(self, context={}):
        """
        :param context: the context in which we want to trace
        """
        self.context = context
        self.f = None

    def __call__(self, f, *args, **kwargs):
        self.f = f

        def inner_func(*args, **kwargs):
            self.update_runs()
            timer = Timer()
            with timer:
                output = self.f(*args, **kwargs)
            trace_info = (
                f"{self.f.__name__} call {self.context['__runs'][self.f.__name__]} executed in "
                f"{timer.time_delta} sec"
            )
            self.log([trace_info])
            return output

        return inner_func

    def update_runs(self):
        """
        Update how many times specific function was executed
        :return:
        """
        self.context["__runs"][self.f.__name__] += 1

    def log(self, information_blocks=[]):
        """
        Print basic information into STDOUT
        :param information_blocks: what we want to print
        """
        for block in information_blocks:
            print(block)
