n = int(input())

count_digits = 0

if(n == 0): print(1)
else: 
    while n:
        count_digits += 1
        n //= 10

    print(count_digits)