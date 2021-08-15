import os 
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.Telebot(API_KEY)

@bot.message_handler(command=['Greet'])
def greet(message):
  bot.reply_to(message, "Hey! Hows it going ?")

bot.polling()
