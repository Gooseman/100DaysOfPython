
from functools import reduce


def calc_sum(*args):
    return reduce(lambda x, y: x + y, args, 0)
    # total = 0

    # for num in args:
    #     total += num

    # return total


if __name__ == "__main__":
    print(calc_sum(1, 2, 3))
    print(calc_sum(4, 5))
    print(calc_sum(10))
