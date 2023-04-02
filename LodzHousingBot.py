import os
import telebot
import csv

API_KEY = "6133530193:AAERkEbOUOFfRi1zbgBpKGTQJiLeMKrajVU"
bot= telebot.TeleBot(API_KEY)
#/Hello
@bot.message_handler(commands=['Hello','hello','hi','Hi'])
def greet(message):
    bot.send_message(message.chat.id,"Hey, How can i help you today ?")

#/start
@bot.message_handler(commands=['start',"Start"])
def start(message):
    bot.send_message(message.chat.id, "Welcome to Lodz housing bot, your righfull place to look for rent freely without the need to keep jumping between websites and agencies, if you want the available commands for our bot use /help")
       
#/help
@bot.message_handler(commands=['help',"Help"])
def help(message):
    bot.send_message(message.chat.id,'''
        /start -> Welcome to LodzHousingBot
        /help  -> Guide with our bot
        /Rent -> display available rentals
    ''')

#/Rent
@bot.message_handler(commands=['rent',"Rent"])
def rent(message):
    with open('LodzHousing.csv', newline='', encoding='utf-8') as csvfile:
        data = list(csv.DictReader(csvfile))

        # Print the header
        header = f"{data[0]['Title']}  {data[0]['Price']}  {data[0]['Location/Date']}  {data[0]['Area']}"
        bot.send_message(message.chat.id, header)

        # Print each row
        for row in data[1:]:
            row_text = f"{row['Title']}  {row['Price']}  {row['Location/Date']}  {row['Area']}"
            bot.send_message(message.chat.id, row_text)
bot.polling()