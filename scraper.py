import datetime
from telethon.sync import TelegramClient
import csv

api_id = 1840120
api_hash = 'eb921ae6a9b1a9ba9245d675003fba66'
client = TelegramClient('Fillter_Account', api_id, api_hash)

# set these values
Members_From = "dx42linstalegend"
File_Save = "members1.csv"
# ----------------
all_senders = []
all_participants = []


async def main():
    try:
        async for message1 in client.iter_messages(Members_From, offset_date=datetime.datetime(2020, 10, 3), limit=1):
            all_senders.append(message1.sender_id)

        async for message2 in client.iter_participants(Members_From, aggressive=True,limit=50):
            all_participants.append(message2)

    finally:
        print(1)


with client:
    client.loop.run_until_complete(main())

with open(File_Save, "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['user id'])
    for user in all_senders:
        writer.writerow([user])

with open(File_Save, "a+", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")

    for user in all_participants:
        writer.writerow([user.id])

