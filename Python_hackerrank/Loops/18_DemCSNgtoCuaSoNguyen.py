n = int(input())

count_primes = 0

while n:
    r = n % 10
    if r == 2 or r == 3 or r == 5 or r == 7:
        count_primes += 1
    n //= 10

print(count_primes)