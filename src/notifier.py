import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEBHOOK = os.getenv("DISCORD_WEBHOOK")

def send_discord(message):

    requests.post(
        WEBHOOK,
        json={
            "content": message
        }
    )