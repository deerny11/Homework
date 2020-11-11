mag_list = []
count = 0
stop = 'Да'
while stop != 'нет':
    count += 1
    mag_list.append((count, {'Название товара': input('Название товара: '), 'Цена': float(input('Цена товара: ')),
                             'Количество': int(input('Количество товара: ')),
                             'Ед. измерения': input('Ед. измерения товара: ')}))
    stop = input('Добавляем еще товар? Введите "да" или "нет" >>>')
    print(mag_list)

a_dict = {'Название': [], 'Цена': [], 'Количество': [], 'Ед. измерения': []}
for i in range(len(mag_list)):
    for k, v in mag_list[i][1].items():
        a_dict[k].append(v)
print(a_dict)
