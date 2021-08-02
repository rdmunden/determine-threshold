def try_digit(n):
    if n >= 7897:
        print (f'was true: {n}')
        return n

N = 9999
# c = 4
c = len(str(N))
d = 0
# x = 3
x = c-1
for f in range (1,c+1):
    print ('----')
    print (f'{d=}')
    for i in range(10*d, 10*d+9+1):
        print (f'{i=}')

        # print ('trying {}'.format(i*10**x + (N//(10**f))))
        print ('trying {}'.format(i*10**(c-f) + (N//(10**f))))

        # if next_digit := try_digit(i*10**x + (N//(10**f))):
        if next_digit := try_digit(i*10**(c-f) + (N//(10**f))):

            # d = next_digit // 10**(x)
            d = next_digit // 10**(c-f)

            break
    x -= 1

print ('====')
print (d)
