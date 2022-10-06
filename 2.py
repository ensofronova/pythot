katet1=float(input('Введите значение первого катета: '))
katet2=float(input('Введите значение второго катета: '))
gipot=(katet1**2+katet2**2)**0.5
P=katet1+katet2+gipot
S=(katet1*katet2)*0.5
print('Периметр прямоугольного треугольника с катетами',katet1, 'и', katet2, 'равен', P,', а его площадь равна',S)