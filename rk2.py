from termcolor import cprint


def unit_test(**kwargs):
    def inner_decorator(func):
        def wrapped(*args):
            assert 'input' in kwargs and 'output' in kwargs and len(kwargs['output']) == len(kwargs['input'])
            for i in range(len(kwargs['input'])):
                response = func(*kwargs['input'][i])
                assert response == kwargs['output'][i], f'Incorrect return of function {func.__name__}({kwargs["input"][i]}) - {response}. Must be {kwargs["output"][i]}'
            cprint(f"Test function {func.__name__} complete. Not found errors", 'green')
            return func(*args)
        return wrapped
    return inner_decorator


@unit_test(input=[(1, 2), (2, -1), (0, 10), (4, -6)], output=[3, 1, 10, -3])
def sum1(a, b):
    return a + b


if __name__ == '__main__':
    print(sum1(1, 2))
