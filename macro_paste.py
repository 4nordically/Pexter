import keyboard
import pyperclip
import pyautogui
import requests
import json
import os
from datetime import datetime

webhook_file = "webhook.json"
webhook_url = None

macros = {
    'f': "Text for Macro 1",
    'g': "Text for Macro 2",
    'h': "Text for Macro 3"
}

# Load webhook from file
def load_webhook():
    global webhook_url
    if os.path.exists(webhook_file):
        with open(webhook_file, "r") as f:
            data = json.load(f)
            webhook_url = data.get("webhook_url")

# Save webhook to file
def save_webhook(url):
    global webhook_url
    webhook_url = url
    with open(webhook_file, "w") as f:
        json.dump({"webhook_url": webhook_url}, f)

# Send embedded log to Discord
def send_to_discord(macro_key, text):
    if not webhook_url:
        return
    embed = {
        "embeds": [
            {
                "title": "Macro Triggered",
                "color": 0x3498db,  # Blue
                "fields": [
                    {"name": "Key Pressed", "value": macro_key, "inline": True},
                    {"name": "Text Pasted", "value": text, "inline": False}
                ],
                "footer": {"text": f"Triggered at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"}
            }
        ]
    }
    try:
        requests.post(webhook_url, json=embed)
    except Exception as e:
        print(f"Failed to send webhook: {e}")

# Trigger macro
def trigger_macro(key):
    text = macros[key]
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    print(f"[{key}] → Pasted: {text}")
    send_to_discord(key, text)

# Setup webhook
def setup_system():
    url = input("Enter your Discord webhook URL: ").strip()
    save_webhook(url)
    print("Webhook saved!")

# Start program (global hotkeys)
def start_program():
    print("Macro program running... (Press ESC to quit)")
    for key in macros:
        keyboard.add_hotkey(key, lambda k=key: trigger_macro(k))
    keyboard.wait('esc')

# Menu
def main_menu():
    load_webhook()
    print("Welcome, what would you like to do?")
    print("A | Start Program")
    print("B | Setup System Linking")
    print("C | Cancel")

    choice = input("Choose an option: ").strip().upper()

    if choice == 'A':
        if not webhook_url:
            print("No webhook set. Please run Setup System Linking first.")
            return
        start_program()
    elif choice == 'B':
        setup_system()
    elif choice == 'C':
        print("Exiting...")
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main_menu()
