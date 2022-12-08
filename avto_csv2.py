import csv

csv_file = []


# Открыть файл
def file_open(file_name):
    with open(file_name, newLine='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            csv_file.append(row)
        print(row)
        print("Файл открыт. Записей:", len(csv_file))


# Добавление данных
def insert(vin, nomer, marka, model, age, power, probeg, vladelec, price):
    global csv_file
    try:
        csv_file.append({'vin': vin,
                         'гос номер': nomer,
                         'марка': marka,
                         'модель': model,
                         'год': age,
                         'мощность': power,
                         'пробег': probeg,
                         'кол-во владельцев': vladelec,
                         'стоимость': price})
    except Exception as e:
        return f'Ошибка при добавлении новой записи {e}'
    return "Данные добавлены."


# Удалить no vin
def drop_by_vin(val, col_name='vin'):
    global csv_file
    try:
        csv_file = list(filter(lambda x: x[col_name] != val, csv_file))
    except Exception as e:
        return f'Строка со значением {val} поля {col_name} не найдена'
    return f'Строка со значением "{val}" столбца "{col_name}" удалена.'


def find_marka(val, col_name="марка"):
    print(*list(filter(lambda x: x[col_name] == val, csv_file)))


def god_vip(val, col_name="марка"):
    print(*list(filter(lambda x: x[col_name] == val, csv_file)))


def find_nomer(val, col_name="марка"):
        print(*list(filter(lambda x: x[col_name] == val, csv_file)))


def avg_age():
    print("Средний пробегпо всем авто:",
          sum([int(row['пробег']) for row in csv_file])  // len (csv_file))
