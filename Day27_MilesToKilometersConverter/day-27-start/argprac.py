def add(*args):
    """Adds numbers input"""
    summation = 0
    for num in args:
        summation += num
    return summation


print(add(1, 2, 3, 4, 5))
