# Задача 4:
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали cranes журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
#     что Петя и Сережа сделали одинаковое количество журавликов,
#     а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# cranes = int(input())
# print((cranes//6), ((cranes//6)*4), (cranes//6))
print('')

temp = 0

while not temp:
    cranes = input('Введите количество изготовленных журавликов: ')
    if not cranes.isnumeric():
        print('Вы ввели не число! \n')
    else:
        temp += 1
print(f'Петя сделал {int(cranes)//6} шт. Катя {(int(cranes)//6)*4} шт. Серёжа {int(cranes)//6} шт.')
