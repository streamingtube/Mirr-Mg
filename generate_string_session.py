from pyrogram import Client

API_KEY = int(input("Enter API KEY: "))
API_HASH = input("Enter API HASH: ")
with Client(':memory:', api_id=3237659, api_hash=0bf84cfae9ed74566fd9bc36ce793c5f) as app:
    print("\nHere is your String Session: \n")
    print(app.export_session_string())
    print("\nBy https://t.me/linux_repo \n")
