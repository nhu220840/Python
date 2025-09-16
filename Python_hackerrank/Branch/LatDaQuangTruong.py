n, m, a = map(int, input().split())

rows = 0; columns = 0
if n % a == 0:
    rows += n // a
else:
    rows += n // a + 1;

if m % a == 0:
    columns += m // a
else:
    columns += m // a + 1

print(rows * columns)