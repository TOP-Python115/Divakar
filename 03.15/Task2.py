n = int(input('Введите четырехзначное число:  '))
one =n%10
a = n//10 
two = a%10
b = a//10
three = b%10
c = b//10
four = c%10
print( one* two*three*four )
