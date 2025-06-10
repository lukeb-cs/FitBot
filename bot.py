import discord
import logging
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.dm_messages = True
intents.emojis = True

bot = commands.Bot(command_prefix='.', intents=intents)

compliment_list = [
                    "Psst, I love you. :flushed:",
                    "I didn't realize how beautiful you were until just now.",
                    ":heart:",
                    "Wanna grab a drink sometime?",
                    "Did it hurt when you fell from heaven?",
                    "I didn't know they made girls as beautiful as you. :thinking:",
                    "Roses are red, sunflowers are yellow, you look like a nice fellow.",
                    "Hey there.",
                    ":man_dancing::dancer: Dance with me!",
                    "If beauty were time, you’d be an eternity.",
                    "Can you stop being so pretty? It's distracting.",
                    "Are you French? Because Eiffel for you. :relieved:",
                    "You're like Wi-Fi; I'm feeling a strong connection.",
                    "Your hand looks heavy... can I hold it for you?",
                    "Do you have a map? I keep getting lost in your eyes.",
                    "You're the reason my heart has a beat drop. :musical_note:",
                    "You must be a magician, because whenever I look at you, everyone else disappears.",
                    "You're so sweet, you're giving me a toothache. :lollipop:",
                    "Are you made of copper and tellurium? Because you’re Cu-Te.",
                    "Can I follow you home? Because my parents always told me to follow my dreams.",
                    "Do you have a Band-Aid? I just scraped my knee falling for you.",
                    ]

pic_compliment_list = [
                    "Not just a pretty face. :smile:",
                    "I wish I looked that good. :rolling_eyes:",
                    "Wowza!",
                    "Wow, can she get any more beautiful?",
                    "Her boyfriend must be a lucky guy. :angry:",
                    "I'm gonna be staring at this for a while!",
                    "You’re out here making angels jealous. :innocent:",
                    "Delete this please, it’s illegal to be this pretty. :police_car:",
                    "This isn’t fair to the rest of us. :sob:",
                    "Is this photoshopped? Be honest. :face_with_monocle:",
                    "Is this a filter or are you just naturally this photogenic?",
                    "Just when I thought my day couldn’t get better...",
                    "I'm setting this as my phone wallpaper.",
                    "You're the reason stock photo models are out of business.",
                    "This picture should come with a warning label.",
                    "Is it getting hot in here? :hot_face:",
                    "This is getting out of hand!",
                    ]


@bot.event
async def on_ready():
    print('Awaiting Server Input...')

# may not be working entirely
@bot.event
async def on_member_join(member):
    await member.send("Hey girl...")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        if message.content.lower() != ".pic":
            compliment = random.choice(compliment_list)
            await message.author.send(compliment)
    await bot.process_commands(message)


@bot.command()
async def pic(ctx):
    pic_compliment = random.choice(pic_compliment_list)
    await ctx.send(pic_compliment)
    images = [f for f in os.listdir('./images')]
    if not images:
        print("Error Locating Images.")
        return

    chosen_image = random.choice(images)
    image_path = os.path.join('./images', chosen_image)

    await ctx.send(file=discord.File(image_path))

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
