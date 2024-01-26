import math



side = float(input('What is the length of a side of the square? '))
area_square = side ** 2
print(f'The area of the square is: {area_square}')

# print()

length = float(input('What is the length of rectangle? ')) 
width = float(input('What is the width of rectangle? ')) 
area_rectangle = length * width
print(f'The area of the rectangle is: {area_rectangle}')

radius = float(input('What is the radius of circle? ')) 
pi = 3.14
circle = pi * (radius ** 2)
print(f'The area of the circle is: {circle}')




# Stretch 2: Many areas from one value
valor = float(input('What is the value to be used? '))

# 1. area do quadrado = comprimento²
area_do_quadrado = valor ** 2
# 2. area do círculo = PI (3.14) * comprimento²
area_do_circulo = math.pi * (valor ** 2)
# 3. volume do cubo = comprimento³
volume_do_cubo = valor ** 3
# 4. volume da esfera = 4 * PI (3.14) * 
volume_da_esfera = 4/3 * math.pi * (valor ** 3)

print(f'Area of a square: {area_do_quadrado}')
print(f'Area of a circle: {area_do_circulo}')
print(f'Volume of a cube: {volume_do_cubo}')
print(f'The voluma of the sphere is: {volume_da_esfera}')