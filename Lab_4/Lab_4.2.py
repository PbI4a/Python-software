import csv
import json

# Указываем пути к файлам
INPUT_FILENAME = r"C:\Users\rykov\PycharmProjects\Course Python английский\Работа с источниками данных\Лабораторная работа\Конвертер из CSV в JSON формат\input.csv"
OUTPUT_FILENAME = r"C:\Users\rykov\PycharmProjects\Course Python английский\Работа с источниками данных\Лабораторная работа\Конвертер из CSV в JSON формат\output.json"


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
