import os
import telebot
import csv
from telebot import types
import Googlemap
import googlemaps
from Googlemap import get_lat_lng, generate_map_popup

API_KEY_Google = 'X'
API_KEY = "Y"
bot = telebot.TeleBot(API_KEY)

# Maximum number of rentals to display at once
MAX_RENTALS = 5

# /Hello


@bot.message_handler(commands=['Hello', 'hello', 'hi', 'Hi'])
def greet(message):
    # Create inline keyboard
    keyboard = types.InlineKeyboardMarkup()
    help_button = types.InlineKeyboardButton("Help", callback_data='help')
    rent_button = types.InlineKeyboardButton("Rent", callback_data='rent')
    keyboard.add(help_button, rent_button)

    bot.send_message(message.chat.id, "Welcome to Lodz housing bot, your rightful place to look for rent freely without the need to keep jumping between websites and agencies. If you want to see available rentals, click the 'Rent' button below:", reply_markup=keyboard)

# /start


@bot.message_handler(commands=['start', "Start"])
def start(message):
    greet(message)

# /help


@bot.message_handler(commands=['help', "Help"])
def help(message):
    # Create inline keyboard
    keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton("Back", callback_data='greet')
    keyboard.add(back_button)

    bot.send_message(message.chat.id, '''
        /start -> Welcome to LodzHousingBot
        /help  -> Guide of our bot
        /rent -> Display available rentals
    ''', reply_markup=keyboard)
# /Rent


@bot.message_handler(commands=['rent', 'Rent'])
def rent(message):
    with open('LodzHousingWlink.csv', newline='', encoding='utf-8') as csvfile:
        data = list(csv.DictReader(csvfile))

        # Print the header
        header = f"{data[0]['Title']}  {data[0]['Price']}  {data[0]['Location/Date']}  {data[0]['Area']}  {data[0]['Link']}"
        bot.send_message(message.chat.id, header)

        # Print the first MAX_RENTALS and map popup
        for row in data[1:MAX_RENTALS+1]:
            address = row['Location/Date']
            lat, lng = get_lat_lng(address)
            if lat is not None and lng is not None:
                bot.send_location(message.chat.id, lat, lng)
            else:
                bot.send_message(message.chat.id, "Could not find location")

            row_text = f"{row['Title']}  {row['Price']}  {row['Location/Date']}  {row['Area']}"
            bot.send_message(message.chat.id, row_text)

            link = "olx.pl" + row['Link']
            bot.send_message(message.chat.id, link)


        # Ask if user wants more rentals
        if len(data) > MAX_RENTALS:
            keyboard = types.InlineKeyboardMarkup()
            more_button = types.InlineKeyboardButton(
                "More Rentals", callback_data='more_rentals')
            keyboard.add(more_button)
            bot.send_message(
                message.chat.id, "Would you like to see more rentals?", reply_markup=keyboard)


def send_more_rentals(message, data, start_idx):
    # Print the first MAX_RENTALS and map popup
    for row in data[start_idx:start_idx+MAX_RENTALS]:
        address = row['Location/Date']
        lat, lng = get_lat_lng(address)
        if lat is not None and lng is not None:
            bot.send_location(message.chat.id, lat, lng)
        else:
            bot.send_message(message.chat.id, "Could not find location")

        row_text = f"{row['Title']}  {row['Price']}  {row['Location/Date']}  {row['Area']}"
        bot.send_message(message.chat.id, row_text)

        link = "olx.pl" + row['Link']
        bot.send_message(message.chat.id, link)

    # Ask if user wants more rentals
    if start_idx + MAX_RENTALS < len(data):
        keyboard = types.InlineKeyboardMarkup()
        more_button = types.InlineKeyboardButton(
            "More Rentals", callback_data=f"more_rentals,{start_idx+MAX_RENTALS}")
        keyboard.add(more_button)
        bot.send_message(
            message.chat.id, "Would you like to see more rentals?", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "No more rentals available")

# Callback function for inline keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'rent':
        rent(call.message)
    elif call.data == 'help':
        help(call.message)
    elif call.data == 'greet':
        greet(call.message)
    elif call.data.startswith('more_rentals'):
        start_idx = int(call.data.split(
            ',')[1]) if ',' in call.data else MAX_RENTALS
        with open('LodzHousingWlink.csv', newline='', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))
            send_more_rentals(call.message, data, start_idx)






# Handler to print the chat ID
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    print("Chat ID:", chat_id)
    exit()



bot.polling()
