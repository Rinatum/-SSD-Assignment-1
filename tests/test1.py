import time
from collections import defaultdict
from contextlib import redirect_stdout
from io import StringIO

from src.task1 import tracer

CONTEXT = {"__runs": defaultdict(int)}


@tracer(CONTEXT)
def kek():
    time.sleep(2)


def test_tracer():
    correct_part1 = "kek call 1 executed in"
    correct_part2 = "2"
    std_output = StringIO()
    with redirect_stdout(std_output):
        kek()
    output = std_output.getvalue()

    assert correct_part1 in output and correct_part2 in output
