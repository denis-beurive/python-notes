import typing


# This function returns a closure.
# The value of "x" is "enclosed".

def enclose1(x: int) -> typing.Callable[[], int]:

    def func() -> int:
        return 2 * x

    return func


c1: typing.Callable[[int], int] = enclose1(2)
print(f'exec c1 -> {c1():d}')


# Using a defined (multiline) function
def enclose2(f: typing.Callable[[int], int]) -> typing.Callable[[int], int]:

    def func(value: int) -> int:
        return 2 * f(value)

    return func


c2: typing.Callable[[int], int] = enclose2(lambda x: 3*x)
print('c2(4) = {:d}'.format(c2(4)))  # Should return 3*4*2


@enclose2
def my_function(x: int) -> int:
    return 10 * x


# We should get: 10 * 4 * 2 = 80
print('(enclose2 o my_function)(4) = {:d}'.format(my_function(4)))

