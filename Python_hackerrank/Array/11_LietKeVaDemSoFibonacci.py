from math import *

F = [0] * 100

def init():
    F[0] = 0
    F[1] = 1
    for i in range(2, 100):
        F[i] = F[i - 1] + F[i - 2]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    init()

    foundedFibo = False
    for i in arr:
        if i in F:
            print(i, end = ' ')
            foundedFibo = True
    if foundedFibo == False:
        print("NONE")
        
