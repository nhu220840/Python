from math import * 

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().split()))


    for i in range(len(arr)):
        sum_left, sum_right = 0, 0
        for j in range(0, i):
            sum_left += arr[j]
        for j in range(i + 1, len(arr)):
            sum_right += arr[j]
        if isPrime(sum_left) and isPrime(sum_right):
            print(i, end = ' ')
