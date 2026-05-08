import requests
import time

TOKEN = "8464483700:AAHk22o89JPC0FW_M_iE2fkMSX0OSGAQKvU"
CHAT_ID = "688869599"

URL = "https://adhahi.dz/register"

def send_message():
    msg = "Oran is AVAILABLE on Adhahi!"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)

def check_site():
    try:
        r = requests.get(URL, timeout=10)
        return "Oran" in r.text
    except:
        return False

print("Bot started...")

# TEST MESSAGE (optionnel)
send_message()

while True:
    if check_site():
        send_message()
        print("Oran found!")
        time.sleep(60)
    else:
        print("Nothing yet...")
        time.sleep(30)
