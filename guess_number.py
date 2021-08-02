# def is_over_limit(n):
#     if n >= 7897:
#         return True

#----------
def try_digit(n):
    # if n >= 7897:
    # if n >= 63107:
    if n >= 9759384755:
        print (f'was true: {n}')
        return n

#----------
# def find_lowest_wout_going_over():
def guess_number(n=9):
    """ This is going to assume the number you want is at least 1
        So it's positive non-zero
    """
    # if is_over_limit(n):
    if try_digit(n):
        return n
    else:
        return guess_number((n * 10) + 9)


N = guess_number()
print(f'ans is: {N}')


#----------
# N = 9999
# N = 99999
c = len(str(N))
d = 0

for f in range (1,c+1):
    print ('----')
    print (f'{d=}')
    for i in range(10*d, 10*d+9+1):
        print (f'{i=}')

        print ('trying {}'.format(i*10**(c-f) + (N//(10**f))))

        if next_digit := try_digit(i*10**(c-f) + (N//(10**f))):

            d = next_digit // 10**(c-f)

            break


print ('====')
print (d)
