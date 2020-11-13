

is_all_true = all([0, True, 10, False, {}, []])
print(is_all_true)  # False: all values are not True

is_all_true = all([True, 10])
print(is_all_true)  # True: all values are True

is_any_true = any([0, True, 10, False, {}, []])
print(is_any_true)  # True: at least one value is True