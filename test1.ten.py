"""Module contains a solution to the task: ten."""

def decorator(*args, **kwargs):
    """Function."""
    print((args, kwargs))

    def func_decorator(func):
        """Function."""
        def wrapper(func_args):
            """Function."""
            return func(func_args)

        return wrapper

    return func_decorator


@decorator(1, 2, 3, [1, 2, 3], 'one', 'two', 'three',
           one=1, two=2, three=3)
def identity(x):
    """Function."""
    return x


print(identity(42))


@decorator()
def identity(x):
    """Function."""
    return x


print(identity(42))
