import random
import asyncio
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
import pandas as pd
from telethon import errors
from telethon.tl.types import PeerUser
import datetime
import time
from telethon import sync
from telethon.tl import types as t
import csv
from Online_Members_Only import *

# Set these varibles

Members_From = "Scamalerts12"
File_Save1 = "Members1.csv"
File_Save2 = "Members2.csv"
File_Save3 = "Members3.csv"
File_From = "Members0.csv"
Members_To_Add = 2000
Sleep_Until_Reconnect = 500
Line_Target = Members_To_Add // 3

#---------------------------------------
df = pd.read_csv(File_From, nrows=Members_To_Add)
IDs_Not_Proccess = pd.read_csv(File_From, skiprows=Members_To_Add)

X = []

for i in df["user id"].dropna():
    X.append(i)


#--------------------
Filtered_Users = []
print("Starting with", len(X))

for A in reversed(X):
    try:
        api_id = 1840120
        api_hash = 'eb921ae6a9b1a9ba9245d675003fba66'
        client = TelegramClient('Fillter_Account', api_id, api_hash)



        async def main():
            await client.get_participants(Members_From)
            my_user = await client.get_entity(PeerUser(A))
            if online_within(my_user, 30) == True:
                Filtered_Users.append(my_user)

            else:
                print("Delete this shit user.")


        with client:
            client.loop.run_until_complete(main())

        X.remove(A)

    except ValueError:
        print("Vale error, skipping...")
        print(A)
        continue

    except errors.UserNotParticipantError:
        print("User not part of group, skipping...")
        continue

    except ConnectionError: #This not working when you get a connectrion error in the middle of the proccess.
        print("No Connection In Range.")
        print("Wait {} seconds....".format(Sleep_Until_Reconnect))
        time.sleep(Sleep_Until_Reconnect)
        continue
    finally:


        df_File_Save1 = pd.read_csv("members1.csv")
        df_File_Save2 = pd.read_csv("members2.csv")
        df_File_Save3 = pd.read_csv("members3.csv")

        #Make it so after it does file 3 it then does 1 to 3 again

        if len(df_File_Save1) < Line_Target:

            with open(File_Save1, "w", encoding='UTF-8') as f:
                writer = csv.writer(f, delimiter=",", lineterminator="\n")
                writer.writerow(['user id'])

            with open(File_Save1, "a+", encoding='UTF-8') as f:
                writer = csv.writer(f, delimiter=",", lineterminator="\n")
                for user in Filtered_Users:
                    writer.writerow([user.id])



            with open(File_From, "w", encoding='UTF-8') as f: #adds user id to the top and clears evey old list
                writer = csv.writer(f, delimiter=",", lineterminator="\n")
                writer.writerow(['user id'])

            IDs_Not_Proccess.to_csv(File_From, index=False)#Adds the Ids that we sidnt proccess




        else:
            print(len(df_File_Save1))
            if len(df_File_Save2) < Line_Target:
                with open(File_Save2, "w", encoding='UTF-8') as f:
                    writer = csv.writer(f, delimiter=",", lineterminator="\n")
                    writer.writerow(['user id'])

                with open(File_Save2, "a+", encoding='UTF-8') as f:
                    writer = csv.writer(f, delimiter=",", lineterminator="\n")
                    for user in Filtered_Users:
                        writer.writerow([user.id])

                with open(File_From, "w", encoding='UTF-8') as f:
                    writer = csv.writer(f, delimiter=",", lineterminator="\n")
                    writer.writerow(['user id'])

                IDs_Not_Proccess.to_csv(File_From, index=False)
            else:
                print(len(df_File_Save2))
                if len(df_File_Save3) < Line_Target:

                    with open(File_Save3, "w", encoding='UTF-8') as f:
                        writer = csv.writer(f, delimiter=",", lineterminator="\n")
                        writer.writerow(['user id'])

                    with open(File_Save3, "a+", encoding='UTF-8') as f:
                        writer = csv.writer(f, delimiter=",", lineterminator="\n")
                        for user in Filtered_Users:
                            writer.writerow([user.id])

                    with open(File_From, "w", encoding='UTF-8') as f:
                        writer = csv.writer(f, delimiter=",", lineterminator="\n")
                        writer.writerow(['user id'])

                    IDs_Not_Proccess.to_csv(File_From, index=False)

                else:

                    print("jvndfjfvdj")




print("Done Add_Members")
print(len(X), "are left.")