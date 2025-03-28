# Задание 3. Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых
# (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада,
# и на них в следующем году тоже будут проценты).
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

def bank(a, years):

    rate = 0.10

    for _ in range(years):
        a += a * rate
        print(f"Общий годовой доход - {a}")
    return a

initial_deposit = 1500000
investment_period = 7

result = bank(initial_deposit, investment_period)
print(f"Общая сумма дохода через {investment_period} лет: {result:.2f} рублей")