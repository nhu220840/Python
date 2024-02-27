import math

numberOfCoins, sum = map(int, input().split())

print(math.ceil(sum / numberOfCoins))