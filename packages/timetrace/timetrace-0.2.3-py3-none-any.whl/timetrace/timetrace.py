import time
import functools
import matplotlib.pyplot as plt

class TimeTrace:
    def __init__(self):
        self.records = []

    def trace(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            self.records.append((func.__name__, elapsed_time))
            return result
        return wrapper

    def report(self):
        if not self.records:
            print("No records to show.")
            return
        
        func_names = [record[0] for record in self.records]
        times = [record[1] for record in self.records]
        
        plt.figure(figsize=(10, 5))
        plt.bar(func_names, times, color='skyblue')
        plt.xlabel('Function Name')
        plt.ylabel('Execution Time (s)')
        plt.title('Function Execution Time')
        plt.show()

        self.records.clear()