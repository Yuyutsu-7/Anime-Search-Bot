import importlib
import asyncio
import requests
from pyrogram import idle
from AniPlay import app
from AniPlay.plugins import ALL_MODULES

loop = asyncio.get_event_loop()

async def init():
    # Generate random parameter for the deep link
    parameter = str(requests.get('https://api.vhtear.com/randomstring?length=10&apikey=YOUR_API_KEY').json()['result'])

    # Shorten the deep link using your URL shortener API
    deep_link = "https://telegram.dog/tpe_v2_bot?start=nada1000000046_" + parameter
    response = requests.get("YOUR_URL_SHORTENER_API" + deep_link)

    # Get the shortened URL from the response
    shortened_link = response.text.strip()

    # Print the shortened link for testing purposes
    print("[INFO]: Shortened Link: ", shortened_link)

    for module in ALL_MODULES:
        importlib.import_module("AniPlay.plugins." + module)
    print("[INFO]: Imported Modules Successfully")

    await app.start()
    print("[INFO]: Bot Started")
    await idle()
    print("[INFO]: BOT STOPPED")
    await app.stop()
    for task in asyncio.all_tasks():
        task.cancel()

if __name__ == "__main__":
    loop.run_until_complete(init())
