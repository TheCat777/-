from random import randint


def gen_random(count: int, a: int, b: int): return [randint(a, b) for _ in range(count)]


if __name__ == '__main__':
    print(gen_random(10, 2, 5))
