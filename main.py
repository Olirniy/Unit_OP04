# Задание 1. Напишите функцию **sum_range(start, end)**,
# которая суммирует все целые числа от значения **start** до величины **end** включительно.


def sum_range(start, end):
    """
    Суммирует все целые числа от start до end включительно.
    Альтернативная реализация через цикл.
    """
    if start > end:
        start, end = end, start

    total = 0
    for number in range(start, end + 1):
        total += number
    return total

print(sum_range(1, 10))
print(sum_range(10, 1))
print(sum_range(5, 17))
print(sum_range(-3, 3))