n = int(input('Введите четырехзначное число:  '))
n2 = 0

while n>0:
    n1 = n%10
    n = n//10
    n2 = n2*10 + n1
print (n2)
