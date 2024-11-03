# 1. Напишите функцию find_common_participants, принимающую две строки, в которых перечислены участники без пробелов,
# а также необязательный аргумент, отвечающий за разделитель по умолчанию равен запятой.
# 2. Найдите общих участников среди двух групп.
# 3. Верните полученный результат в виде списка общих участников отсортированных в алфавитном порядке.

# participants_first_group = "Иванов|Петров|Сидоров"
# participants_second_group = "Петров|Сидоров|Смирнов"

def x(group1, group2, z='|'):
    x1 = set(group1.split(z))
    x2 = set(group2.split(z))
    y = sorted(x1 & x2)
    return y

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = x(participants_first_group, participants_second_group)
print(result)
