Number = ('One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Forteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty');
Tens = ('Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety')
Hang_Tram = 0
Hang_Chuc = 0
Hang_Don_Vi = 0

x = int(input('Please type a 3-digit positive integer: x = '))
if (x > 999) or (x < 100):
  print (x,' is not a 3-digit number.')
else:
  Hang_Tram = int((x - x%100)/100);
  Hang_Chuc = int(((x - Hang_Tram*100) - (x - Hang_Tram*100)%10)/10);
  Hang_Don_Vi = int((x - Hang_Tram*100)%10);
  print('Hang_Tram = ', Hang_Tram);
  print('Hang_Chuc = ', Hang_Chuc);
  print('Hang_Don_Vi = ', Hang_Don_Vi);
  if Hang_Chuc*10 >= 20:
    Word_Number = Number[Hang_Tram-1] + ' Hundred and ' + Tens[Hang_Chuc-1] + ' ' + Number[Hang_Don_Vi-1];
  else:
    Word_Number = Number[Hang_Tram-1] + ' Hundred and ' + Number[Hang_Chuc*10+Hang_Don_Vi-1];
  print('English word representation for ', x, ' is: ', Word_Number)