# 🔹 Python Test Paster, Pexter

A simple Python macro tool that pastes predefined text when certain keys are pressed.
Optionally logs every macro trigger to a Discord webhook. 

This is the information about **release v1.1.0**

---

## 📦 Features

* **Custom hotkeys** for instant pasting of predefined text.
* **Optional Discord webhook logging** with embed formatting.
* **Single-letter hotkeys automatically delete themselves** before pasting text.
* **Simple "Exit" command** to quit without needing special key presses.

---

## 📋 Requirements

Before running this program, install:

* [Python 3.8+](https://www.python.org/downloads/)
* Required packages:

  ```bash
  pip install keyboard pyperclip pyautogui requests
  ```

**Edit macro text**
   In the script file, find:

   ```python
   macros = {
       'f1': "Text for Macro 1",
       'f2': "Text for Macro 2",
       'f3': "Text for Macro 3"
   }
   ```

   Change the keys and text to whatever you want.

---

## 🖥 Usage

1. **Run the program**:

   ```bash
   python macro.py
   ```

2. **Choose an option**:

   * `A` → Start Program
   * `B` → Setup System Linking (Discord Webhook, optional)
   * `C` → Exit

3. **While running**:

   * Press a macro key (`F1`, `F2`, `F3`, or a letter) to paste text instantly.
   * If the macro is a **letter**, the program will delete it first before pasting.
   * To **quit**, type:

     ```
     Exit
     ```

     and press Enter in the terminal.
## 🔗 Optional Discord Logging
If you want to log macro usage to a Discord channel:
1. Go to your Discord server settings → **Integrations** → **Webhooks**.
2. Create a webhook and copy its URL.
3. Choose **B | Setup System Linking** in the menu.
4. Paste your webhook URL.
5. Now every macro trigger will be sent as a Discord embed.

## ⚠️ Notes
- If you **don’t set a webhook**, the program will still work but won’t log to Discord.
