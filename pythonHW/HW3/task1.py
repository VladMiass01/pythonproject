# На вход подается словарь со списком вещей для похода в качестве ключа и их
# массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Предметы не должны дублироваться.
# Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен
# в переменную backpack.
# Достаточно получить один допустимый вариант и сохранить в переменную backpack.
# Не выводите backpack на экран.

items = {"ключи": 0.3, "кошелек": 0.2, "телефон": 0.5, "зажигалка": 0.1}
max_weight = 1.0
# items = sorted(items.items(), key = lambda x: x[1], reverse = True)
items = dict(sorted(items.items(), key = lambda x: x[1], reverse = True))
weight = 0.0
backpack  = {}
for key, value in items.items():
    if weight + value <= max_weight:
        weight += value
        backpack[key] = value
print(backpack)
