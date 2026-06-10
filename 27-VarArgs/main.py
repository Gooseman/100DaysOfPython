
from functools import reduce


def sum(*args):
    return reduce(lambda x, y: x + y, args, 0)
    # total = 0

    # for num in args:
    #     total += num

    # return total


if __name__ == "__main__":
    print(sum(1, 2, 3))
    print(sum(4, 5))
    print(sum(10))