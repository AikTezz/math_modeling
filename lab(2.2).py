n =int(input('Первый член: '))
a1 = int(input('Знаменатель: '))
a2 = int(input('Количество членов прогресии: '))
print(a1)  
b1 = a1
for i in range(1,a2+1):
    tezz = b1*a1
    print(b1)
    b1 = tezz
