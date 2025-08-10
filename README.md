# Simple how to use
This requires a simple setup to ensure it works. You need python installed on your computer for the setup to work.

Inside your command prompt, run this:
`pip install keyboard pyperclip pyautogui requests`
Then, open the macro_paste.py file and select an option - please note, if you enter the Discord linking webhook, the program will close and you need to re-open it. This signifies that it saved your webhook locally.

## Default Settings
F - Macro 1

G - Macro 2

H - Macro 3

These macro's don't provide any benefit but purely speed up the copy/paste mechanism so that you don't have to spend load's of time typing text you know you will use repetitively!
You can change these very quickly inside of the script inside of this section (line 12) :

`macros = {
    'f': "Text for Macro 1",
    'g': "Text for Macro 2",
    'h': "Text for Macro 3"
}`
