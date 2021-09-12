from collections import defaultdict
from contextlib import redirect_stdout
from io import StringIO
from inspect import signature, getsource, Parameter

from task1 import Timer, Tracer


class Dumper(Tracer):
    """
    Dump the key information about executed function
    """

    def dump(self, args, kwargs, output):
        """
        Dump basic info about the decorated function
        """
        sign = signature(self.f)
        defaults = {
            k: v.default
            for k, v in sign.parameters.items()
            if v.default is not Parameter.empty
        }
        key_worded = {**defaults, **kwargs}
        return f"""  
Name:   {self.f.__name__}
Type:   {type(self.f)}
Sign:   {sign}
Args:   positional {args} 
        key=worded {key_worded}
        
Doc:    {self.f.__doc__}

Source: {getsource(self.f)}

Output: {output}
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
            dump_info = self.dump(args, kwargs, output)
            trace_info = (
                f"{self.f.__name__} call {self.context['__runs'][self.f.__name__]} executed in "
                f"{timer.time_delta} sec"
            )
            self.log([trace_info, dump_info])
            return output

        return inner_func
