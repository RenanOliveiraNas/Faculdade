a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
area_triangulo = a * c / 2
area_circulo = 3.14159 * c ** 2
area_trapezio = (a + b) * c / 2
area_quadrado = b**2
area_retangulo = a * b
print(f'TRIANGULO: {area_triangulo:.3f}')
print(f'CIRCULO: {area_circulo:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')
