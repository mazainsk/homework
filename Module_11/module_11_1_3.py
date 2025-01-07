# Домашнее задание по теме "Обзор сторонних библиотек Python".
# Часть 3. Пример использования библиотеки request для запроса текущей цены криптовалютной торговой пары.

import requests


while True:
    print()
    ticker = input('Введите тикер торговой пары (например, BTCUSDT, ETHBTC) или 0 для выхода >> ').upper()
    if ticker == '0':
        break
    print('Запрос текущей цены на спотовом рынке биржи Binance... ', end='')
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params=f'symbol={ticker}')
    if response.status_code != 200 and response.status_code != 400:
        print('Непредвиденная ошибка.')
        break
    json_data = response.json()  # По-хорошему нужно сначала убедиться, что в словаре response.headers
            # по ключу 'Content-Type' есть значение, содержащее подстроку 'application/json',
            # но для Binance я и так знаю, что JSON там есть.
    if response.ok:
        print('Ok')
        print(f'Текущая цена {ticker} = {float(json_data['price']):.4f}')
    else:
        print('Error')
        print(f'Сообщение сервера: {json_data['msg']}')

