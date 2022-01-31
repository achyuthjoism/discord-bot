import os
import string
import random
import sys
from discord.ext import commands
import json
import time

with open('token.json') as f:
    data = json.load(f)

application_path = os.path.dirname(sys.executable)
token = data['token']
words = ["pls dig", "pls fish", "pls hunt", "pls beg"]


def randomTxt():
    N = 4
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=N))
    return str(res)

# <@743409920396754965>


async def spamRandom():
    channelId = int(input("Enter channel ID to spam: "))
    numberM = int(input("Enter the number of message -1 for infinity: "))
    channel = bot.get_channel(channelId)
    count = 0
    print("Spamming....")
    if numberM == -1:
        while True:
            msg = await channel.send(randomTxt())
            time.sleep(1)
    else:
        while count != numberM:
            msg = await channel.send(randomTxt())
            count += 1
            time.sleep(1)
    print("Spamming complete")


async def spamMessage():
    channelId = int(input("Enter channel ID to spam: "))
    numberM = int(input("Enter the number of message -1 for infinity: "))
    message = input("Enter the message to spam: ")
    channel = bot.get_channel(channelId)
    count = 0
    print("Spamming....")
    if numberM == -1:
        while True:
            msg = await channel.send(message)
            time.sleep(1)
    else:
        while count != numberM:
            msg = await channel.send(message)
            count += 1
            time.sleep(1)
    print("Spamming complete")


async def pingg():
    victimChannel = int(input("Enter channel ID to spam: "))
    channel = bot.get_channel(victimChannel)
    print("Spamming....")
    while True:
        for word in words:
            msg = await channel.send(word)
            time.sleep(1)

        print("Sleeping")
        time.sleep(40)


async def main():
    m = """
1. Spam a random message in discord
2. Spam a specific message in discord
3. Get rich in Dank memer bot
4. Exit
"""
    print(m)
    choice = int(input("Enter your choice: "))
    while choice != 4:
        if choice == 1:
            await spamRandom()
        elif choice == 2:
            await spamMessage()
        elif choice == 3:
            await pingg()
        else:
            print("Enter a valid choice")
        print(m)
        choice = int(input("Enter your choice: "))


bot = commands.Bot(command_prefix="*!*", self_bot=True)


@bot.event
async def on_ready():
    await main()

bot.run(token, bot=False)
