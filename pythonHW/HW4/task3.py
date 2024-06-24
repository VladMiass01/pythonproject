# У вас есть банковская карта с начальным балансом равным 0 у.е.
# Вы хотите управлять этой картой, выполняя следующие операции,
# для выполнения которых необходимо написать следующие функции:
# check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
# deposit(amount): Пополнение счёта.
# withdraw(amount): Снятие денег.
# exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.
# Пополнение счета:
# Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму.
# Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.
# Снятие средств:
# Функция withdraw(amount) позволяет клиенту снимать средства со счета.
# Сумма снятия также должна быть кратной MULTIPLICITY. При снятии средств начисляется комиссия
# в процентах от снимаемой суммы, которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.
# Завершение работы:
# Функция exit() завершает работу с банковским счетом. Перед завершением,
# если на счету больше RICHNESS_SUM, начисляется налог на богатство
# в размере RICHNESS_PERCENT процентов.
# Проверка кратности суммы:
# Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному
# множителю MULTIPLICITY. Реализуйте программу для управления банковским счетом,
# используя библиотеку decimal для точных вычислений.

import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []

def check_multiplicity(amount):
    """Проверяет, кратна ли сумма MULTIPLICITY."""
    return not amount % MULTIPLICITY


def deposit(amount):
    """Пополнение счета."""
    global count
    global bank_account
    global operations

    if check_multiplicity(amount):
        bank_account += amount
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account.normalize():f} у.е.')
    else:
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')


def withdraw(amount):
    """Снятие средств с учетом комиссии."""
    global count
    global bank_account
    global operations

    # Рассчитываем комиссию за снятие
    sum_removal = amount * PERCENT_REMOVAL
    if MIN_REMOVAL > sum_removal:
        sum_removal = MIN_REMOVAL
    elif MAX_REMOVAL < sum_removal:
        sum_removal = MAX_REMOVAL

    amount_with_commission = decimal.Decimal(amount) + decimal.Decimal(sum_removal)

    if not check_multiplicity(amount):
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')

    if bank_account - amount > 0:
        bank_account -= amount + sum_removal
        operations.append(
            f'Снятие с карты {amount} у.е. Процент за снятие {sum_removal.normalize():f} у.е.. Итого {bank_account.normalize():f} у.е.')
    else:
        operations.append(
            f'Недостаточно средств. Сумма с комиссией {amount_with_commission.normalize()} у.е. На карте {bank_account} у.е.')


def exit():
    """Завершение работы и вывод итоговой информации о состоянии счета."""
    global operations
    global bank_account

    if bank_account > RICHNESS_SUM:
        sum_deposit = bank_account * RICHNESS_PERCENT
        bank_account -= sum_deposit
        operations.append(f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {sum_deposit} у.е. Итого {bank_account} у.е.')
    operations.append(f'Возьмите карту на которой {bank_account} у.е.')


deposit(1000)
withdraw(200)
exit()
print(operations)
