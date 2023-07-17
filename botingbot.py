import telegram.ext
import csv

Token = "X"

updater = telegram.ext.Updater("X", use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    update.message.reply_text(
        "Welcome to RentWizzard, your righfull place to look for rent freely without the need to keep jumping between websites and agancies!!!")


def help(update, context):
    update.message.reply_text(
        """
        /start -> Welcome to Rentwizzard
        /help  -> Guide with out bot
        /Rent -> display available rentals 
        """
    )

def rent (update, context):
    # Open the CSV file
    with open('housing.csv', newline='', encoding='utf-8') as csvfile:
        # Read the CSV data into a list of dictionaries
        data = list(csv.DictReader(csvfile))

        # Print the header
        header = f"{data[0]['Title']}  {data[0]['Price']}"
        update.message.reply_text(header)

        # Print each row
        for row in data[1:]:
            row_text = f"{row['Title']}  {row['Price']}"
            update.message.reply_text(row_text)


dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('rent', rent))
updater.start_polling()
updater.idle()