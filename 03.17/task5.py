c1_c = int(input())
c1_r =  input()
c2_c =  int (input())
c2_r = input()

if c1_r=='a': c1_r= 1
elif c1_r=='b': c1_r = 2
elif c1_r=='c': c1_r = 3
elif c1_r=='d': c1_r = 4
elif c1_r=='e': c1_r = 5
elif c1_r=='f': c1_r = 6
elif c1_r=='g': c1_r = 7
elif c1_r=='h': c1_r = 8

if c2_r=='a': c2_r = 1
elif c2_r=='b': c2_r = 2
elif c2_r=='c': c2_r = 3
elif c2_r=='d': c2_r = 4
elif c2_r=='e': c2_r = 5
elif c2_r=='f': c2_r = 6
elif c2_r=='g': c2_r = 7
elif c2_r=='h': c2_r = 8

c2_r = ord (c2_r)- 96

if c1_c%2==1 and c1_r%2==1 or c1_c%2==0 and c1_r%2==0:
    c1_col='black'
else:
    c1_col='white'
    
if c2_c%2==1 and c2_r%2==1 or c2_c%2==0 and c2_r%2==0:
    c2_col='black'
else:
    c2_col='white'
    
print ('ДА' if c1_col==c2_col else 'НЕТ')
