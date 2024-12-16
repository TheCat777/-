def print_result(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        if isinstance(original_result, list): modified_result = '\n'.join(map(str, original_result))
        elif isinstance(original_result, dict): modified_result = '\n'.join([f"{k} = {v}"for k, v in original_result.items()])
        else: modified_result = original_result
        print(f'Function {func.__name__} have returned:\n{modified_result}')
        return original_result
    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
