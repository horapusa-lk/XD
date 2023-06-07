from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

sudo_list = [1436625686, -1001972140628]

driver = webdriver.Chrome("chromedriver")
driver.get("https://sexy.ai")
time.sleep(5)
button_element_1 = driver.find_element(By.XPATH, '//button[text()="I AM 18 Years or Older"]')
button_element_1.click()
time.sleep(2)
input_element = driver.find_elements(by=By.TAG_NAME, value="textarea")[2]


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.chat.id in sudo_list:
        await update.message.reply_text(f"""Hello you can generate Hentai Arts using this bot. 
Just send me the prompt as normal message""")


async def nfsw(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.chat.id in sudo_list:
        x = await context.bot.get_chat_member(chat_id=-1001517984656, user_id=update.message.from_user.id)
        user = str(x.status)
        if user == 'member' or update.message.from_user.id == 1436625686:
            prompt = update.message.text[6:]
            input_element.clear()
            input_element.send_keys(prompt)
            button_element = driver.find_element(By.XPATH, '//button[text()="Generate 2 Images"]')
            button_element.click()
            time.sleep(10)
            img_url_1 = driver.find_elements(by=By.TAG_NAME, value="img")[1].get_attribute("src")
            img_url_2 = driver.find_elements(by=By.TAG_NAME, value="img")[2].get_attribute("src")
            await update.message.reply_photo(img_url_1)
            await update.message.reply_photo(img_url_2)
            time.sleep(1)
        else:
            await update.message.reply_text('''You need to join our main group to use this bot
👇👇👇
https://t.me/hora_pusa_ai''')


# Create the Application and pass it your bot's token.
application = Application.builder().token("6213444100:AAEzkJSbzmV4n4_kx1H2ao5zd-NIVk5XYXE").build()
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("nfsw", nfsw))

# Run the bot until the user presses Ctrl-C
application.run_polling()

# jexoc82465@onlcool.com
# 91780
