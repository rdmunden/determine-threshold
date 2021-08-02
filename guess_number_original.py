lower = 1999999999999999999
upper = 2999999999999999999


lower2 = 999999999999999999
upper2 = 9999999999999999999


def is_over_limit(n):
    if n >= 7897:
        return True

#def find_lowest_wout_going_over():
def guess_number(n=9):
    """ This is going to assume the number you want is at least 1
        So it's positive non-zero
    """
    if is_over_limit(n):
        return n
    else:
        return guess_number((n*10)+9)

ans = guess_number()
print (f'ans is: {ans}')

"""
def is_found(n):
    if n == 7897:
        return n


def find_MSD(n):
    l = len(n)
    for i in range(
    if is_found(n):
        return n
    elif is_found(n//10):
            return n//10
    else:
        n =
"""