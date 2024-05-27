# TimeTrace

TimeTrace is a simple performance tracing and visualization library for Python.

## Installation

```sh
pip install timetrace


from timetrace import TimeTrace

tracer = TimeTrace()

@tracer.trace
def my_function():
    # Function implementation

my_function()
tracer.report()