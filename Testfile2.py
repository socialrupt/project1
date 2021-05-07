import random
import asyncio
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
import pandas as pd
from telethon import errors
from telethon.tl.types import PeerUser
import datetime
import time


from telethon.tl import functions as f, types as t
from Online_Members_Only import *

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

df = pd.read_csv("members3.csv")

X = []

for i in df["user id"].dropna():
    X.append(i)

# Set these varibles
Target_Gorup_ID = "featureamadx21"
Members_From = "dx42linstalegend"
Sleep_Until_Reconnect = 500
Max_Sec_Adding = 100

df2 = pd.read_csv("List of api ids.csv")
df3 = pd.read_csv("List of api hashs.csv")
df4 = pd.read_csv("List of api sessions.csv")
#-----------------------Test
for loop_api_id in df2["api id"]:
    for loop_api_hash in df3["api hash"]:
        for loop_api_session in df4["api session"]:
#----------------------- START
            api_id = loop_api_id
            api_hash = loop_api_hash
            client = TelegramClient(loop_api_session, api_id, api_hash)

            async def main():
                await client.get_participants(Members_From, aggressive=True)
            with client:
                client.loop.run_until_complete(main())



            print("Starting with", len(X))

            for Twenty in reversed(X):
                try:


                    async def main():
                        my_user = await client.get_entity(PeerUser(Twenty))
                        if online_within(my_user, 7) == True:
                            await client(InviteToChannelRequest(Target_Gorup_ID, [my_user]))
                            await asyncio.sleep(random.uniform(5, Max_Sec_Adding)) #change back to normal later
                        else:
                            print("Delete this shit user.")


                    with client:
                        client.loop.run_until_complete(main())

                    X.remove(Twenty)

                except errors.UserChannelsTooMuchError:
                    print("User is added to to many channels/groups error...")
                    continue
                except errors.UserNotMutualContactError:
                    print("User is not a mutral contact error...")
                    continue
                except errors.UserPrivacyRestrictedError:
                    print("The user settings restrict error...")
                    continue
                except errors.UserKickedError:
                    print("User is not in group error...")
                    continue
                except ConnectionError:
                    print("No Connection In Range.")
                    print("Wait {} seconds....".format(Sleep_Until_Reconnect))
                    time.sleep(Sleep_Until_Reconnect)
                    continue
                except ValueError:
                    print("Vale error, skipping...")
                    print(Twenty)
                    continue
                except errors.UserNotParticipantError:
                    print("User not part of group, skipping...")
                    continue
                except errors.ChatWriteForbiddenError:
                    print("Adding you to the group....")
                    async def main():
                        await client(f.channels.JoinChannelRequest(channel=Target_Gorup_ID))
                        await client(f.channels.JoinChannelRequest(channel=Members_From))

                    with client:
                        client.loop.run_until_complete(main())
                    continue
                except errors.PeerFloodError:
                    try:
                        async def main():
                            await client.kick_participant(Target_Gorup_ID, "me")
                            await client.kick_participant(Members_From, "me")
                        with client:
                            client.loop.run_until_complete(main())
                        print("your banned with bot")
                        print("changing bot...")
                        break
                    except errors.UserNotParticipantError:
                        break
                except errors.FloodWaitError:
                    try:
                        async def main():
                            await client.kick_participant(Target_Gorup_ID, "me")
                            await client.kick_participant(Members_From, "me")
                        with client:
                            client.loop.run_until_complete(main())
                        print("your banned with bot")
                        print("changing bot...")
                        break
                    except errors.UserNotParticipantError:
                        break
            #------------------------ END
