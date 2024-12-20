from math import *

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False
    
    return True

if __name__ == '__main__':
    num = int(input())
    arr = list(map(int, input().split()))

    sum, count_prime = 0, 0
    for item in arr:
        if isPrime(item):
            sum += item
            count_prime += 1

    average = sum / count_prime
    print('%.3f' % (average))
