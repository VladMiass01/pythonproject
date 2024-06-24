# Треугольник существует только тогда, когда сумма любых двух его сторон больше
# третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину
# каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется
# больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним,
# только если треугольник существует .

a = 4
b = 4
c = 4
if (a + b > c) and (a + c > b) and (b + c > a):
    print('Треугольник существует')
    if (a == b) and (b == c) and (c == a):
        print('Треугольник равносторонний')
    if ((a == b) and (a != c)) or ((a == c) and (a != b)):
        print('Треугольник равнобедренный')
    if (a != b) and (b != c) and (c != a):
        print('Треугольник разносторонний')
else:
    print('Треугольник не существует')