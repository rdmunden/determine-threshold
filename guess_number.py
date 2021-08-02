# def is_over_limit(n):
#     if n >= 7897:
#         return True

#----------
def try_digit(n):
    # if n >= 7897:
    # if n >= 63107:
    # if n >= 9759384755:
    # if n >= 2112:
    # if n >= 3178:
    # if n >= 3199:
    if n >= 69105:
    # if n >= 999:
    #     print (f'was true: {n}')
    #     print (f'Was greater than or equal to the value: {n}')
        print (f'The value {n} was greater than or equal to the target.')
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
    msd = 0
    # N = int("9" * c)

    # for f in range (1,N+1):
    # for f in range (N-1,-1,-1):
    digits_left = N
    while digits_left > 0:
        digits_left -= 1
        print ('----')
        # print (f'Most significant digits found so far: {msd=}')
        # print (f'Most significant digits found so far: {msd or "None"}')
        if msd:
            msg = format(msd, f'.<{N}')
        else:
            msg = "None"
        print (f'Digits uncovered so far: {msg}')

        for d in range(10*msd, 10*msd+9+1):
            ''' d represents the most significant digits found so far
                10*d shifts them to the left so we can find the next significant digit after them
                e.g. if two msd's have been found, and they are 19, this will loop over the range:
                190
                191
                192
                ...
                199 
            '''
            
            # print (f'\tTrying significant digits: {d=}', end='')

            ''' Even though it is a mathematical simplification to express this formula as:
                (i+1) * 10**f - 1
                I am multiplying out the (i+1) in order to make it more clear how this works
            '''
            # try_num = d * 10**f + 10**f - 1
            try_num = d * 10**digits_left + 10**digits_left - 1
            print ('\t... trying: {:0{width}}'.format(try_num, width=N))

            # if next_digit := try_digit(i*10**(c-f) + (N//(10**f))):
            # xx = ("9" * (c-f)) or "0"
            # if next_digit := try_digit(i*10**(c-f) + (int(("9" * (c-f)) or "0"))):
            # if next_digit := try_digit(i * 10**(c-f) + 10**(c-f) - 1):
            # if next_digit := try_digit(i * 10**(N-f) - 1):

            # if next_digit := try_digit((i+1) * 10**f - 1):

            # if next_digit := try_digit(d * 10**f + 10**f - 1):
            if next_digit := try_digit(try_num):
                ''' if there are 5 digits in the answer
                    and we have found the two most significant digits
                    and say e.g. they are 19 (which is represented by "i")
                    then "i * 10**f" is looping over:
                        190 * 100 = 19000
                        191 * 100 = 19100
                        192 * 100 = 19200
                        ...
                        199 * 100 = 19900
                    To that we are adding "10**f - 1", which in this case is 100 - 1 = 99
                    So the actual numbers being tried are:
                        19099
                        19199
                        19299
                        ...
                        19999
                '''
                # d = next_digit // 10**(N-f)
                # msd = next_digit // 10**f
                msd = next_digit // 10**digits_left
                break

    return msd


N = get_num_digits()
print(f'Number of digits: {N}')
# print (d)
ans = guess_number(N)
print(f'Answer is: {ans}')