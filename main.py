from avto_csv2 import file_open, insert, drop_by_vin, find_marka

FILENAME = "data.csv"

MENU =  {
    '1': 'Открыть файл',
    '2': 'Добавить новую запись',
    '3': 'Удалить авто по  VIN',
    '4': 'Найти авто по марке и модели',
    '5': 'Вывести информацию об авто с самым большим пробегом ',
    '6': 'Вывести информацию об авто с указанием года выпуска',
    '7': 'Вывести всю информацию об авто',
    '8': 'Вывести средний пробег',
    '9': 'Вывести авто по гос номеру',
    '10': 'Вывести все данные об авто в порядке возрастания цены',
    '11': 'Вывести данные об авто с заданным диапозоном цен',
    '12': 'Сохратить в файл',
    '13': 'Вывести все записи',
    '0': '<- Меню',
    'exit':  'Выход'
}

for k, v in MENU.items():
    print(k, '-', v)

while True:
    action = input('>_')
    if action == '1':
        file_open(FILENAME)
    elif action == '2':
        print(insert(input('vin: '),input('гос номера: '),input('марка: '), input('модель: '),input('год: '),
                     input('мощность: '), input('пробег: '), input('кол-во владельцев: '), input('стоимость: ')))
    elif action == '3':
        col = input('Колонка: ')
        val = input('Значение: ')
        print(drop_by_vin(val, col_name=col))
    elif action == '4':
        find_marka(input("Введите марку или модель: "), input("Колонка: "))
    elif action == '6':
        god_vip(input("Год выпуска: "), input("Колонка:"))

    elif action == '9':
        find_nomer(input("Гос номер: "), input('Колонка'))

    elif action == '13':
        show_rows()
    elif action == '0':
        for k, v in MENU.items():
            print(k, '=, v')
    elif action == 'exit':
        break





