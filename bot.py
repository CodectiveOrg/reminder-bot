
import requests
import random
import schedule
import time




GROUP_CHAT_ID = 4520085646

all_members = {341204925, 976691560} 

messages = [
    "همه چی خوب پیش میره؟ کم پیدایی",
    "سلام، فعالیت نداریا!",
    "اگر به مشکلی خوردی بپرس"
]

def welcome_message(text):
    url = f"https://tapi.bale.ai/bot{TOKEN}/sendMessage"
    data = {
        "group_chat_id": GROUP_CHAT_ID,
        "text": text
    }
    response = requests.post(url, json=data)
    print(response.json())

welcome_message("welcome-Message")

# -------------------
# inactive user
def send_message_to_chat(chat_id, text):
    url = f"https://tapi.bale.ai/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id, 
        "text": text
    }
    response = requests.post(url, json=data)
    result = response.json()
    print(f"Sending message to {chat_id}: {result}")
    return result

# ---------------

last_update_id = None

def get_updates():
    global last_update_id
    url = f"https://tapi.bale.ai/bot{TOKEN}/getUpdates"
    params = {}
    if last_update_id:
        params['offset'] = last_update_id + 1  
    response = requests.get(url, params=params)
    data = response.json()
    print("Updates:", data)

    if data.get("ok") and data.get("result"):
        last_update_id = data["result"][-1]["update_id"] 
    return data

# -----------

def get_active_users(window_seconds=60):
    data = get_updates()
    active_users = set()
    now = int(time.time())
    if data.get("ok"):
        for update in data.get("result", []):
            message = update.get("message")
            if message:
                chat = message.get("chat")
                if chat and chat.get("id") == GROUP_CHAT_ID:
                    msg_date = message.get("date")  
                    if (now - msg_date) <= window_seconds:
                        from_user = message.get("from")
                        if from_user:
                            user_id = from_user.get("id")
                            active_users.add(user_id)
    print("Active users: ", active_users)
    return active_users


# ---------------------

def notify_inactives():
    active = get_active_users()
    inactive = all_members - active
    
    print("Inactive users:", inactive)
    
    for user_id in inactive:
        msg = random.choice(messages)
        send_message_to_chat(user_id, msg)

# ----------------------

def job():
    print("Checking inactive members...")
    notify_inactives()

# schedule.every(1).hours.do(job)
# schedule.every(5).minutes.do(job)
schedule.every(1).minutes.do(job)


print("Bot started. Running scheduled tasks every 1 minutes...")
while True:
    schedule.run_pending()
    time.sleep(1)
