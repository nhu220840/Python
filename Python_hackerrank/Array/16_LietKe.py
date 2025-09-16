from math import * 

def isPrime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

def isPalindrome(n):
    # rev = 0; tmp = n
    # while(n):
    #     rev = rev * 10 + n % 10
    #     n //= 10
    # return rev == tmp

    rev = str(n)[::-1]
    return rev == str(n)

def isSquareNumber(n):
    tmp = isqrt(n)
    return tmp * tmp == n

def sumDigitsIsPrime(n):
    sum = 0
    while(n):
        sum += n % 10
        n //= 10
    return isPrime(sum)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    isPalindrome(1243432)
    count1, count2, count3, count4 = 0, 0, 0, 0
    for i in range(len(arr)):
        if isPrime(arr[i]): count1 += 1
        if isPalindrome(arr[i]): count2 += 1
        if isSquareNumber(arr[i]): count3 += 1
        if sumDigitsIsPrime(arr[i]): count4 += 1

    print(count1, count2, count3, count4, sep = '\n')
