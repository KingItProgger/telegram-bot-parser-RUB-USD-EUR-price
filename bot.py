import telebot


from config import keys,TOKEN
from extensions import Converter, ApiException

bot=telebot.TeleBot(TOKEN)








@bot.message_handler(commands=['start','help'])
def starter(message: telebot.types.Message):
    bot.send_message(message.chat.id, '''для просмотра доступных валют: /values. введите запрос для обработки в формате:\n
                                      <имя валюты, цену которой он хочет узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>''')

@bot.message_handler(commands=['values'])
def valuer(message: telebot.types.Message):
    text='Доступные валюты:'

    for key in keys.keys():
        text = '\n'.join((text,key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])

def convert(message:telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ApiException('неверное количестыо аргументов')
        quate, base, amount = values

        total_base = Converter.get_price(quate,base,amount)
    except ApiException as e:
        bot.reply_to(message, f'ошибка пользователя \n {e}')
    except  Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду {e}')
    else:

        text = f'Цена {amount} {quate} в {base} - {total_base*float(amount)}'

        bot.send_message(message.chat.id, text)
bot.polling(none_stop=True)