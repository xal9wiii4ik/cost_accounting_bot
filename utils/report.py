import datetime

from handlers import dp
from utils.services import get_data_from_request


async def month_report():
    """Отчет за месяц"""

    date_now = datetime.datetime.now()
    if date_now.day == 1:
        users = get_data_from_request(path='users')
        for user in users:
            if user['chat_id'] != 0:
                datas = get_data_from_request(path='cost_history')
                price_report = [
                    {
                        'date': datas[0]['date'],
                        'price': float(0)
                    }
                ]
                text = ''
                counter = 0
                for data in datas:
                    month = int(data['date'].split('-')[1])
                    if month == (date_now.month - 1) or month == (date_now.month + 1):
                        text += f'{data["name_spending"]} {data["price_spending"]}\n'
                    if price_report[counter]['date'].split('-')[1] != data['date'].split('-')[1]:
                        price_report.append(
                            {
                                'date': data['date'],
                                'price': float(0)
                            }
                        )
                        counter += 1
                    price_report[counter]['price'] += float(data['price_spending'])
                text += '\nPRICE REPORT:\n'
                for price in price_report:
                    text += f'In month which number: {price["date"].split("-")[1]}\n you spent: {price["price"]}'
                await dp.bot.send_message(chat_id=user['chat_id'],
                                          text=text)
