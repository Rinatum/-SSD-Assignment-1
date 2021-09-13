from contextlib import redirect_stdout
from io import StringIO

from src.task1 import Timer
from src.task2 import dump


class Printer:
    """
    Basic printer class
    """

    def print_(self, raw):
        pass


class StdOutPrinter(Printer):
    """
    Prints to stdout
    """

    def print_(self, raw):
        print(raw)


class FilePrinter(Printer):
    """
    Prints to file
    """

    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath

    def print_(self, raw):
        with open(self.filepath, "a+") as f:
            f.write("\n" + raw)


class Tracer:
    """
    The class that allows to trace function execution as decorator
    """

    def __init__(self, context, printer: Printer = StdOutPrinter()):
        """
        :param context: the context in which we want to trace
        """
        self.context = context
        self.f = None
        self.printer = printer

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
            self.printer.print_(block)


class Dumper(Tracer):
    """
    Dump the key information about executed function
    """

    def __call__(self, f, *args, **kwargs):
        self.f = f

        def inner_func(*args, **kwargs):
            self.update_runs()
            timer = Timer()
            std_output = StringIO()
            with timer:
                with redirect_stdout(std_output):
                    output = self.f(*args, **kwargs)
            dump_info = dump(f, args, kwargs, std_output.getvalue())
            trace_info = (
                f"{self.f.__name__} call {self.context['__runs'][self.f.__name__]} executed in "
                f"{timer.time_delta} sec"
            )
            self.log([trace_info, dump_info])
            return output

        return inner_func


class TimeRanker:
    """
    Class to rank functions by time execution
    """

    def __init__(self, printer: Printer = StdOutPrinter()):
        self.func2time = {}
        self.printer = printer

    def __call__(self, f, *args, **kwargs):
        def inner_func(*args, **kwargs):
            timer = Timer()
            with timer:
                output = f(*args, **kwargs)
            self.func2time[f.__name__] = timer.time_delta
            return output

        return inner_func

    def log(self):
        sorted_tuples = sorted(self.func2time.items(), key=lambda item: item[1])
        self.printer.print_("PROGRAM | RANK | TIME ELAPSED")
        for i, (func_name, time_ellapsed) in enumerate(sorted_tuples):
            self.printer.print_(f"{func_name}   {i + 1}   {time_ellapsed}")
