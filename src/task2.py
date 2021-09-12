from contextlib import redirect_stdout
from inspect import signature, getsource, Parameter
from io import StringIO

from task1 import Timer, log


def dump(f, args, kwargs, output):
    """
    Dump basic info about the decorated function
    """
    sign = signature(f)
    defaults = {
        k: v.default
        for k, v in sign.parameters.items()
        if v.default is not Parameter.empty
    }
    key_worded = {**defaults, **kwargs}
    return f"""  
Name:   {f.__name__}
Type:   {type(f)}
Sign:   {sign}
Args:   positional {args} 
    key=worded {key_worded}

Doc:    {f.__doc__}

Source: {getsource(f)}

Output: {output}
"""


def dumper(context):
    def inner_function(f):
        def wrapper(*args, **kwargs):
            context["__runs"][f.__name__] += 1
            timer = Timer()
            std_output = StringIO()
            with timer:
                with redirect_stdout(std_output):
                    output = f(*args, **kwargs)
            dump_info = dump(f, args, kwargs, std_output.getvalue())
            trace_info = (
                f"{f.__name__} call {context['__runs'][f.__name__]} executed in "
                f"{timer.time_delta} sec"
            )
            log([trace_info, dump_info])
            return output

        return wrapper

    return inner_function
