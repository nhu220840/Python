A = int(input('Please type a positive integer: A = '))
print ('\n------------------');
print ('For loop:');
for i in range (A,0,-1):
  print(i, end = ', ');
print ('\n------------------');

print ('While loop:');
while A > 0:
  print (A, end = ', \t');
  A -= 1;