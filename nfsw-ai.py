from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("chromedriver")
driver.get("https://sexy.ai")
time.sleep(5)
button_element_1 = driver.find_element(By.XPATH, '//button[text()="I AM 18 Years or Older"]')
button_element_1.click()
time.sleep(2)
input_element = driver.find_elements(by=By.TAG_NAME, value="textarea")[2]


# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(f"""Hello you can generate NFSW Arts using this bot. 
Just send me the prompt as normal message""")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    prompt = update.message.text
    input_element.clear()
    input_element.send_keys(prompt)
    button_element = driver.find_element(By.XPATH, '//button[text()="Generate 2 Images"]')
    button_element.click()
    time.sleep(10)
    img_url_1 = driver.find_elements(by=By.TAG_NAME, value="img")[1].get_attribute("src")
    img_url_2 = driver.find_elements(by=By.TAG_NAME, value="img")[2].get_attribute("src")
    await update.message.reply_photo(img_url_1)
    await update.message.reply_photo(img_url_2)


"""Start the bot."""
# Create the Application and pass it your bot's token.
application = Application.builder().token("6237921114:AAHiT5zxkzM3-zNxK_CpV5X6HQ6ZsoFEXgA").build()

# on different commands - answer in Telegram
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))

# on non command i.e message - echo the message on Telegram
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Run the bot until the user presses Ctrl-C
application.run_polling()

# jexoc82465@onlcool.com
# 91780
