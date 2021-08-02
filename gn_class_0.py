""" This guesses a number by finding the most significant digit first and then working to the right
    This assumes the target number is at least 1
    So it's a positive, non-zero
"""


class target_num:
    def __init__(self, target):
        self.target = target

    def try_num(self, n):
        if n >= self.target:
            return n


def try_digit(n):
    # looking_for = 7897
    # looking_for = 63107
    # looking_for = 9759384758
    # looking_for = 2112
    # looking_for = 3178
    # looking_for = 3199
    # looking_for = 69105
    # looking_for = 999
    # looking_for = 1
    # looking_for = 0
    # looking_for = -123
    # looking_for = 179769313486231580793728971405303415079934132710037826936173778980444968292764750946649017977587207096330286416692887910946555547851940402630657488671505820681908902000708383676273854845817711531764475730270069855571366959622842914819860834936475292719074168444365510704342711559699508093042880177904174497791
    # looking_for = 487928273
    looking_for = 500000000

    if n >= looking_for:
        # print (f'The value {n} was greater than or equal to the target.')
        return n


def get_num_digits(n=9):
    if try_digit(n):
        return len(str(n))
    else:
        return get_num_digits((n * 10) + 9)


def guess_number(N):
    msd = 0  # The digits found so far

    digits_remaining = N - 1  # The # digits remaining to the right of the one we're working on

    while digits_remaining >= 0:
        # print ('----')
        # if msd:
        #     msg = format(msd, f'░<{N}')
        # else:
        #     msg = "None"
        # print (f'Digits found: {msg}')

        for d in range(10 * msd, 10 * msd + 10):
            ''' msd represents the most significant digits found so far
                "10*msd" shifts them to the left so we can find the next significant digit after them
                e.g. if two msd's have been found, and they are 19, this will loop over the range:
                190
                191
                192
                ...
                199 
            '''

            # print (f'\tTrying significant digits: {d=}', end='')

            ''' Even though it is a mathematical simplification to express this formula as:
                (d+1) * 10**digits_remaining - 1
                I am multiplying it out in order to make it more clear how this works
            '''
            ''' e.g. if there are 5 digits in the answer
                and we have found the 2 most significant digits
                and say they are say 19 (which is represented by "msd")
                and we are working on the 3rd digit, which means there are 2 digits remaining after that
                then "d * 10**digits_remaining" is looping over:
                    190 * 100 = 19000
                    191 * 100 = 19100
                    192 * 100 = 19200
                    ...
                    199 * 100 = 19900

                To that we are adding "10**digits_remaining - 1", which in this case is 100 - 1 = 99
                So the actual numbers being tried are:
                    19099
                    19199
                    19299
                    ...
                    19999
            '''
            try_num = (d * 10 ** digits_remaining) + (10 ** digits_remaining - 1)
            # print ('\t... trying: {:0{width}}'.format(try_num, width=N))

            if next_digit := try_digit(try_num):
                msd = next_digit // 10 ** digits_remaining
                break

        digits_remaining -= 1

    return msd


def main():
    N = get_num_digits()
    print(f'Number of digits: {N}')
    # print (d)
    ans = guess_number(N)
    print(f'Answer is: {ans}')


if __name__ == '__main__':
    main()