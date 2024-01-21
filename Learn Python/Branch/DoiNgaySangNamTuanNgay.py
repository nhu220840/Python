n = int(input())

yrs = n // 365
wks = (n % 365) // 7
ds = n % 12

print(yrs, wks, ds, sep = " ")