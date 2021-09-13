import time
from collections import defaultdict
from contextlib import redirect_stdout
from io import StringIO

from src.task3 import Tracer, Dumper, TimeRanker

CONTEXT = {"__runs": defaultdict(int)}


@Tracer(CONTEXT)
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


@Dumper(context=CONTEXT)
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
        "@Dumper",
    ]
    std_output = StringIO()
    with redirect_stdout(std_output):
        sleep(2)
    output = std_output.getvalue()

    for correct in corrects:
        assert correct in output


def test_ranker():
    table = ["kek   1", "kek2   2", "kek1   3"]

    ranker = TimeRanker()

    @ranker
    def kek():
        time.sleep(1)

    @ranker
    def kek2():
        time.sleep(2)

    @ranker
    def kek1():
        time.sleep(3)

    kek()
    kek1()
    kek2()

    std_output = StringIO()
    with redirect_stdout(std_output):
        ranker.log()
    output = std_output.getvalue()

    for raw in table:
        assert raw in output
