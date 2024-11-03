# Напишите функцию, которая принимает два аргумента:
# список товаров
# товар, который нужно найти.
# Если товар присутствует в списке, то вернуть индекс первого вхождения. Учтите, что товаров может быть несколько.
# Если товар не найден в списке, то вернуть None.

# items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
# for find_item in ['банан', 'груша', 'персик']:
# index_item = ...  # TODO Вызовите функцию, что получить индекс товара
# if index_item is not None:
# print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
# else:
# print(f"Товар '{find_item}' не найден в списке.")

def x(items_list, find_item):
    try:
        return items_list.index(find_item)
    except ValueError:
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = x(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")