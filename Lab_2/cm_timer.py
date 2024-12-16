import contextlib
from time import time, sleep


class cm_timer_1:
    def __init__(self):
        self.time = time()

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        print(f"Time: {time() - self.time}")


@contextlib.contextmanager
def cm_timer_2():
    t = time()
    try:
        yield {}
    finally:
        print(f"Time: {time() - t}")


if __name__ == "__main__":
    with cm_timer_2():
        sleep(5.5)

    with cm_timer_1():
        sleep(5.5)
