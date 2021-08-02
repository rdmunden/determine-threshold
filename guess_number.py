# def is_over_limit(n):
#     if n >= 7897:
#         return True

#----------
def try_digit(n):
    # if n >= 7897:
    # if n >= 63107:
    # if n >= 9759384755:
    # if n >= 2112:
    if n >= 3178:
    # if n >= 3199:
    # if n >= 69105:
    # if n >= 999:
        print (f'was true: {n}')
        return n

#----------
# def find_lowest_wout_going_over():
def get_num_digits(n=9):
    """ This is going to assume the number you want is at least 1
        So it's positive non-zero
    """
    # if is_over_limit(n):
    if try_digit(n):
        # return n
        return len(str(n))
    else:
        return get_num_digits((n * 10) + 9)

def guess_number(N):
    # c = len(str(N))
    # c = N
    d = 0
    # N = int("9" * c)

    # for f in range (1,N+1):
    for f in range (N-1,-1,-1):
        print ('----')
        print (f'{d=}')
        for i in range(10*d+1, 10*d+9+2):
            print (f'{i=}')
            # print ('trying {}'.format(i*10**(c-f) + (N//(10**f))))
            #print ('trying {}'.format(i*10**(c-f) + (int("9" * (c-f)))))
            print ('trying {}'.format(i * 10**f - 1))

            # if next_digit := try_digit(i*10**(c-f) + (N//(10**f))):
            # xx = ("9" * (c-f)) or "0"
            # if next_digit := try_digit(i*10**(c-f) + (int(("9" * (c-f)) or "0"))):
            # if next_digit := try_digit(i * 10**(c-f) + 10**(c-f) - 1):
            # if next_digit := try_digit(i * 10**(N-f) - 1):
            if next_digit := try_digit(i * 10**f - 1):
                # d = next_digit // 10**(N-f)
                d = next_digit // 10**f
                break

    return d


print ('====')
N = get_num_digits()
print(f'Number of digits: {N}')
# print (d)
ans = guess_number(N)
print(f'Answer is: {ans}')