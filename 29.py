import telebot
import mysql.connector
c = mysql.connector.connect(user="root", password="12345678", host="127.0.0.1",  database="city")
cursor = c.cursor()
cursor.execute("select * from city")
r=cursor.fetchall()
for i in r:
    print(i)
c.commit()

token="647727261:AAFoPy7EDu8maw02FID9G7dLek-NJx7-GRI"
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=["text"])
def sendmess(message):
    bot.send_message(message.chat.id, "it works")
bot.polling()