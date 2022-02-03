import time


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        total_time = self.end = self.start
        print(f"total run time was {total_time:.4f}")


def do_something():
    """Toy function to keep Python busy"""
    "-".join(str(n) for n in range(1000))


with Timer():  # implicit call to __enter__
    do_something()
    # implicit call to __exit__

print("the end")
