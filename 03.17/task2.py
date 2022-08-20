a = int (input ('Введите ваш возраст: '))
if a>0 and a<=13:
    print ('Детство')
elif a>=14 and a<=24:
    print (' Молодость')
elif a>=25 and a<=59:
    print ('Зрелость')
elif a>=60 and a<122:
    print ('Старость')
else:
    print ('Ископаемое')