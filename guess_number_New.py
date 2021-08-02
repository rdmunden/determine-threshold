def try_digit(n):
    if n >= 7897:
        return True

N = 9999
c = 4
d = 0

for f in range (1,c+1):
    for i in range(10*d, 10*d+9+1):
        if next_digit := try_digit(i + N//10**f):
            d = next_digit

print (d)
