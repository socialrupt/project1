#Can this file replace the scraper file
import datetime
from telethon.sync import TelegramClient
import csv

api_id = 1840120
api_hash = 'eb921ae6a9b1a9ba9245d675003fba66'
client = TelegramClient('Fillter_Account', api_id, api_hash)

# set these values
Target_Gorup_ID = "Scamalerts12"
Members_From = "VidyCoin"
File_Save = "members0.csv"
# ----------------
Target_Gorup_ID_Participents = []
Group2 = []

async def main():
    try:
        async for group1 in client.iter_participants(Target_Gorup_ID, aggressive=True):
            Target_Gorup_ID_Participents.append(group1)

        async for group2 in client.iter_participants(Members_From, aggressive=True):
            Group2.append(group2)

    finally:
        print(1)

        for a in Target_Gorup_ID_Participents:
            if a in Group2:
                Group2.remove(a)
            else:
                pass


with client:
    client.loop.run_until_complete(main())

with open(File_Save, "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['user id'])

with open(File_Save, "a+", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")

    for user in Group2:
        writer.writerow([user.id])
