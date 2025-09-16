def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    gcdOfAll = gcd(arr[0], arr[1])
    for i in range(2, len(arr)):
        gcdOfAll = gcd(gcdOfAll, arr[i])

    print(gcdOfAll)

