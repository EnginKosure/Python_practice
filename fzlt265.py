def print_argument(func):
    def wrapper(the_number, the_pow):
        print("Argument for",
              func.__name__,
              "is", the_number, 'and', the_pow)
        print(locals().keys())  # dict_keys(['the_number', 'the_pow', 'func'])
        print(func.__code__.co_varnames)  # ('x', 'pow')
        return func(the_number, the_pow)
    return wrapper


@print_argument
def add_one(x, pow):
    return (x + 1)**pow


print(add_one(2, 2))  # 9
