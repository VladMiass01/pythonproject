# Напишите функцию key_params, принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def key_params(**kwargs):
    key_param_dict = {}
    for key, value in kwargs.items():
        if not isinstance(value, (int, float, str, tuple, frozenset, type(None))):
            value = str(value)
        key_param_dict[value] = key

    return key_param_dict

params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
