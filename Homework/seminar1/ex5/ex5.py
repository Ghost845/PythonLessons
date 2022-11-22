# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1

# out
# 5.099

print('Введите координату плоскости X первой точки: ')
x1 = int(input())
print('Введите координату плоскости Y первой точки: ')
y1 = int(input())
print('Введите координату плоскости X второй точки: ')
x2 = int(input())
print('Введите координату плоскости Y второй точки: ')
y2 = int(input())
print('in')
print(f'- {x1}')
print(f'- {y1}')
print(f'- {x2}')
print(f'- {y2}')
ab = (((x2 - x1)**2 + (y2 - y1)**2)**0.5)
print('out')
print(round(ab, 4)) 
