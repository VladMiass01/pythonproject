# На вход автоматически подаются две строки frac1 и frac2 вида
# a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей.
# Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def sum_and_prod(frac1, frac2):
    frac1 = Fraction(frac1)
    frac2 = Fraction(frac2)
    sum_frac = frac1 + frac2
    prod_frac = frac1 * frac2
    return sum_frac, prod_frac


frac1 = "1/2"
frac2 = "1/3"
sum_frac, prod_frac = sum_and_prod(frac1, frac2)
print(f"Сумма дробей: {sum_frac}")
print(f"Произведение дробей: {prod_frac}")

f1 = Fraction(frac1)
f2 = Fraction(frac2)
print(f"Сумма дробей: {f1 + f2}")
print(f"Произведение дробей: {f1 * f2}")
