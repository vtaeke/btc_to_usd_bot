import requests
from datetime import datetime
import telebot
from auth_data import token


def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    # print(response)
    sell_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello friend! Write the '/price' or '/high' or '/low'"
                                          " to find out the cost of BTC!")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "/price":
            req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
            response = req.json()
            sell_price = response["btc_usd"]["sell"]
            bot.send_message(
                message.chat.id,
                f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}"
            )
        elif message.text.lower() == "/high":
            req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
            response = req.json()
            high_price = response["btc_usd"]["high"]
            bot.send_message(
                message.chat.id,
                f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {high_price}"
            )
        elif message.text.lower() == "/low":
            req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
            response = req.json()
            low_price = response["btc_usd"]["low"]
            bot.send_message(
                message.chat.id,
                f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {low_price}"
            )
        else:
            bot.send_message(message.chat.id, "What??? Check the command!")


    bot.polling()


if __name__ == '__main__':
    # get_data()
    telegram_bot(token)