from collections.abc import Iterable


def is_iterable(obj):
    return isinstance(obj, Iterable)


def ensure_iterable(obj, raise_err=True, return_single=False):
    if isinstance(obj, Iterable):
        return obj
    elif raise_err:
        raise TypeError(f"{obj} is not iterable")
    elif return_single:
        return (obj,)
    else:
        return tuple()


def test():
    # Example usage:
    print(is_iterable([1, 2, 3]))  # Output: True
    print(is_iterable("hello"))  # Output: True
    print(is_iterable(123))  # Output: False
