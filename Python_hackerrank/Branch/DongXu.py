from math import *

numberOfCoins, sum = map(int, input().split())

print(ceil(sum / numberOfCoins))