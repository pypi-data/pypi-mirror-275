# tests/test_timetrace.py
import unittest
from timetrace import TimeTrace
import time

class TestTimeTrace(unittest.TestCase):
    def test_trace(self):
        tracer = TimeTrace()

        @tracer.trace
        def fast_function():
            time.sleep(0.1)

        @tracer.trace
        def slow_function():
            time.sleep(0.2)

        fast_function()
        slow_function()
        self.assertEqual(len(tracer.records), 2)
        self.assertGreater(tracer.records[1][1], tracer.records[0][1])

if __name__ == '__main__':
    unittest.main()