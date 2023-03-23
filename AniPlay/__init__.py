from os import environ
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(environ.get("APP_ID", "20424692")),
    api_hash= environ.get("API_HASH", "ae5738c411c5848960f5249e466c5f6a"),
    bot_token= environ.get("TOKEN", "5560545615:AAFWUM7D3CpbSkcVgBbg55SNTFYBEBN8tX8")
)
