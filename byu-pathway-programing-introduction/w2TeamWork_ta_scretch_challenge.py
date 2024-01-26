import math

comprimento = float(input('What is the length? '))
# comprimento²
comprimento_ao_quadrado = comprimento * comprimento 
# comprimento³
comprimento_ao_cubo = comprimento * comprimento * comprimento

# 1. area do quadrado = comprimento²
area_do_quadrado = comprimento_ao_quadrado
# 2. area do círculo = PI (3.14) * comprimento²
area_do_circulo = math.pi * comprimento_ao_quadrado
# 3. volume do cubo = comprimento³
volume_do_cubo = comprimento_ao_cubo
# 4. volume da esfera = 4 * PI (3.14) * 
volume_da_esfera = (4 * math.pi * comprimento_ao_cubo) / 3

print(f'The area of the square is: {area_do_quadrado}')
print(f'The area of the circle is: {area_do_circulo}')
print(f'The volume of the cube is: {volume_do_cubo}')
print(f'The voluma of the sphere is: {volume_da_esfera}')