import math
def coin(x,y):
    l = math.sqrt(x**2 + y**2)
    return l
print('Введите координаты монетки')
x = float(input('X: '))
y = float(input('Y: '))
radius = float(input('Введите радиус окружности: '))

if abs(coin(x,y)) > radius:
    print ('Монетки в области нет')
else:
    print('Монетка где-то рядом')