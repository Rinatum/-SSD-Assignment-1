import time
from collections import defaultdict
from contextlib import redirect_stdout
from io import StringIO

from src.task2 import dumper

CONTEXT = {"__runs": defaultdict(int)}


@dumper(context=CONTEXT)
def sleep(n):
    """
    Sleeeep
    """
    time.sleep(n)


def test_dumper():
    corrects = [
        "Name:   sleep",
        "Type:   <class 'function'>",
        "Sign:   (n)",
        "Args:   positional",
        "key=worded",
        "Sleeeep",
        '@dumper'
    ]
    std_output = StringIO()
    with redirect_stdout(std_output):
        sleep(2)
    output = std_output.getvalue()

    for correct in corrects:
        assert correct in output
