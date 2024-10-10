def sum_of_1(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print(sum_of_1(1,2,3,4,5,6))


def sum_of_2(**kwargs):
    total = 0
    for k, v in kwargs.items():
        total += v
    return total

print(sum_of_2(a=1,b=2,c=3))
