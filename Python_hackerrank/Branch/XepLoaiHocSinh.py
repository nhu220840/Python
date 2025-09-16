a, b, c, d = map(float, input().split())

gpa = (a + b + c * 2 + d * 3) / 7

if gpa >= 8: print("GIOI")
elif gpa >= 6.5: print("KHA")
elif gpa >= 5: print("TRUNG BINH")
else: print("YEU")