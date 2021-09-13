from collections import defaultdict

from src.task3 import FilePrinter, Dumper
from src.task4 import ErrorHanler

CONTEXT = {"__runs": defaultdict(int)}


@ErrorHanler(FilePrinter("exceptions.txt"))
@Dumper(CONTEXT)
def get_error():
    raise Exception("Oh")


def test_error_handler():
    corrects = ["Traceback", "Exception: Oh"]

    get_error()

    with open("exceptions.txt", "r") as f:
        content = f.read()

    for correct in corrects:
        assert correct in content
