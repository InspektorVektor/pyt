import telebot
import mysql.connector
c = mysql.connector.connect(user="root", password="12345678", host="127.0.0.1",  database="base")
cursor = c.cursor()

def listmaker():
    a=[]
    r=cursor.fetchall()
    for i in r:
        a.append(str(i))
        q='\n'.join(a)
    return q;

token="647727261:AAFoPy7EDu8maw02FID9G7dLek-NJx7-GRI"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    markup=telebot.types.ReplyKeyboardMarkup(True, True)
    markup.row("1","2","all")
    bot.send_message(message.chat.id, "Ku", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def sendmess(message):
    if (message.text=="1"):
        cursor.execute("select title from table30 where `duration`='90 мин'")
        bot.send_message(message.chat.id, listmaker())
    elif (message.text=="2"):
        cursor.execute("select title from table30 where `duration`='80 мин'")
        bot.send_message(message.chat.id, listmaker())
    elif (message.text=="all"):
        cursor.execute("select title from table30")
        bot.send_message(message.chat.id, listmaker())
    else:
        bot.send_message(message.chat.id, "Fatal Error")

bot.polling()
c.commit()