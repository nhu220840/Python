from math import *

x1, y1, x2, y2 = map(int, input().split())

print('%.2f' % sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))