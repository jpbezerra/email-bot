# About the Repository
- This repository is for an email generator. This email generator is based on a dictionary, which the keys are the emails and the values are the paths of files that will be sent.
- Each email address will receive the wanted code (with a description on the email itself) and the code that the bot is using to send his code.

# Files/Folders
#### `email-bot/files-to-send`
- Here has some example codes, just to test if the codes sent are the correct ones.
#### `email-bot/bot.py`
- The main code, it has the full funcionality of the BOT and also writes a new file with only the code used for the BOT.
#### `email-bot/get-files.py`
- It's where I can get the emails and the files, not the ideal maybe some adjustments (like get the emails and files from a sheet (maybe using Google Sheets API), and maybe get the files from another method instead of the path).
#### `email-bot/send-code.py`
- The code written automatically by the bot.py file.
