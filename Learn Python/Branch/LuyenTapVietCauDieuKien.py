n = int(input())

if n % 2 == 0: print("YES")
else: print("NO")

if n % 3 == 0 and n % 5 == 0: print("YES")
else: print("NO")

if n % 3 == 0 and n % 7 != 0: print("YES")
else: print("NO")

if n % 3 == 0 or n % 7 == 0: print("YES")
else: print("NO")

if 30 < n < 50: print("YES")
else: print("NO")

if n >= 30 and (n % 2 == 0 or n % 3 == 0 or n % 5 == 0): print("YES")
else: print("NO")

if 10 <= n <= 99 and (n % 10 == 2 or n % 10 == 3 or n % 10 == 5 or n % 10 == 7): print('YES')
else: print('NO')

if n <= 100 and n % 23 == 0: print("YES")
else: print("NO")

if n < 10 or n > 20: print("YES")
else: print("NO")

if (n % 10) % 3 == 0: print("YES")
else: print("NO")