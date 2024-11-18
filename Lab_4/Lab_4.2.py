# Вам требуется прочитать содержимое CSV файла, распарсить его и преобразовать в структуру данных JSON. Ваша задача
# состоит в том, чтобы написать программу, которая прочитает CSV файл, разберет его на отдельные столбцы и создаст
# для каждой записи словарь в формате JSON, где ключами будут названия столбцов, а значениями - соответствующие
# значения в этой строке. Задачи Реализовать конвертер из csv в json формат: название столбца — значение. Для csv
# формата принять разделитель между значениями, по умолчанию "," разделитель строк, по умолчанию "\n". В результате
# распечатать json строку с отступами равными 4. Используйте `DictReader` для чтения значений из CSV. `DictReader`
# возвращает каждую строку в виде типа данных `OrderedDict` из модуля `collections`. Этот тип данных сериализуется
# как обычный python словарь.

#ШАБЛОН КОДА
#INPUT_FILENAME = "input.csv"
#OUTPUT_FILENAME = "output.json"


#def task() -> None:
    #...  # TODO считать содержимое csv файла

    #...  # TODO Сериализовать в файл с отступами равными 4


#if __name__ == '__main__':
    # Нужно для проверки
    #task()

    #with open(OUTPUT_FILENAME) as output_f:
        #for line in output_f:
            #print(line, end="")

import csv
import json

INPUT_FILENAME = r"C:\Users\rykov\PycharmProjects\Course Python английский\Работа с источниками данных\Лабораторная " \
                 r"работа\Конвертер из CSV в JSON формат\input.csv"
OUTPUT_FILENAME = r"C:\Users\rykov\PycharmProjects\Course Python английский\Работа с источниками данных\Лабораторная " \
                  r"работа\Конвертер из CSV в JSON формат\output.json"


def task() -> None:
    try:
        with open(INPUT_FILENAME, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            if reader.fieldnames is None:
                raise ValueError("CSV файл не содержит заголовков.")

            rows = [row for row in reader]

        with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as jsonfile:
            json.dump(rows, jsonfile, ensure_ascii=False, indent=4)

    except FileNotFoundError:
        print(f"Ошибка: Файл {INPUT_FILENAME} не найден.")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == '__main__':
    task()

    try:
        with open(OUTPUT_FILENAME, encoding='utf-8') as output_f:
            for line in output_f:
                print(line, end="")
    except FileNotFoundError:
        print("JSON файл не был создан.")
