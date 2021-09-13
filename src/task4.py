import sys
import traceback
from contextlib import redirect_stdout
from datetime import datetime
from io import StringIO

from src.task1 import Timer
from src.task3 import Printer, StdOutPrinter, FilePrinter


class ErrorHanler:
    def __init__(self, printer: Printer = StdOutPrinter()):
        self.printer = printer

    def __call__(self, f, *args, **kwargs):
        def inner_func(*args, **kwargs):
            try:
                output = f(*args, **kwargs)
            except Exception as e:
                std_output = StringIO()
                with redirect_stdout(std_output):
                    traceback.print_exc(file=sys.stdout)
                self.printer.print_(datetime.now().isoformat())
                self.printer.print_(std_output.getvalue())
            else:
                return output

        return inner_func
