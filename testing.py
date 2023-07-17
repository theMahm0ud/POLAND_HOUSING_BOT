import time
import telebot

# Define your bot's API token
API_KEY = "6133530193:AAERkEbOUOFfRi1zbgBpKGTQJiLeMKrajVU"

# Create an instance of the bot
bot = telebot.TeleBot(API_KEY)

# Test case: Send /start command and check response
def test_start_command():
    chat_id = 123456789  # Replace with your own chat ID for testing

    # Send /start command to the bot and get the response
    response = bot.reply_to(telebot.types.Message(chat_id=chat_id, text="/start"), "/start")

    # Check if the bot replied with the expected message
    expected_response = "Welcome to Lodz housing bot"
    assert response.text == expected_response
    print("Test case: /start command - Passed")

# Test case: Send /help command and check response
def test_help_command():
    chat_id = 123456789  # Replace with your own chat ID for testing

    # Send /help command to the bot and get the response
    response = bot.reply_to(telebot.types.Message(chat_id=chat_id, text="/help"), "/help")

    # Check if the bot replied with the expected message
    expected_response = "/start -> Welcome to LodzHousingBot\n/help  -> Guide of our bot\n/rent -> Display available rentals"
    assert response.text.strip() == expected_response.strip()
    print("Test case: /help command - Passed")

# Test case: Send /rent command and check response
def test_rent_command():
    chat_id = 123456789  # Replace with your own chat ID for testing

    # Send /rent command to the bot and get the response
    response = bot.reply_to(telebot.types.Message(chat_id=chat_id, text="/rent"), "/rent")

    # Check if the bot replied with the expected message
    # Adjust the condition based on your expected response
    assert response.text.startswith("Title")
    print("Test case: /rent command - Passed")

# Run the test cases
test_start_command()
test_help_command()
test_rent_command()
