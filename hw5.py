proceed = int(input('Добрый день, мистер Х. Укажите вашу выручку: '))
costs = int(input('А теперь укажите ваши издержки для сравнения: '))
profit = (proceed - costs)
profitability = int(profit * proceed) / costs / 100
if proceed >= costs:
    print('У нас для вас отлчиные новости - Ваша компания работает в плюс')
    print(f'Рентабельность выручки составляет: {round(profitability)} %')
    people_1 = int(input('Напомните, сколько сотрудников работает в вашей компании? '))
    money = profit / people_1
    print(f'Мы это узнали для того, чтобы сообщить,что на одного сотрудника приходится {round(money)} руб')
else:
    print('Нужно стараться поднимать  продажи - Ваша компания работает в минус(')
