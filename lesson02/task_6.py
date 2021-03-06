"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

i = 0
data_structure = []

while True:
    name = input('Название товара: ')
    price = input('Цена: ')
    count = input('Количество: ')
    unit = input('Единица измерения: ')
    i += 1
    data_structure += [(i, {'название': name, 'цена': price, 'количество': count, 'ед': unit})]
    stop = input('Если вы закончили ввод данных введите: exit или 0: ')
    if stop == '0' or stop.lower() == 'exit':
        break
print(data_structure)

analytics = {}
for el in data_structure:
    if not analytics:
        analytics.update(el[1])
        for key, value in analytics.items():
            analytics[key] = [analytics[key]]
    else:
        for key, value in el[1].items():
            analytics[key].append(value)
print(analytics)

