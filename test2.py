print('Nguyễn Thị Quỳnh Anh')
number = ['', 'One', 'Two',  'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
nty = ['', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
tens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Forteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
x = int(input('Please type a 3-digit positive integer: x = '))
n=x
if n > 999 or n < 100:
  print (n,' is not a 3-digit number.')
else:
  d = [0,0,0]
  i=0
  while n>0:
    d[i]=n%10
    i+=1
    n=n//10
    print ('d = ',d)
    print ('i = ', i)
    print ('x = ', n)
  num = ''
  if d[2]!=0:
    num+=number[d[2]]+' hundred '
  if d[1]!=0:
    if (d[1]==1):
      num+=tens[d[0]]
    if (d[1]!=1):
      num+=nty[d[1]-1]+' '+ number[d[0]]
    else:
      num+=''
  else:
    num+=' and '+number[d[0]]
print (x,' is ', num)