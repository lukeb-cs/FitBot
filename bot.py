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
tree = bot.tree

class LocationMenu(discord.ui.View):
    @discord.ui.select(
        placeholder="[SELECT]",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label="At Home", description="Simple bodyweight exercises"),
            discord.SelectOption(label="At a Gym", description="Free weight and machine exercises"),
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        selection = select.values[0]
        if selection == "At Home":
            await interaction.response.edit_message(content="Which muscle group are you focusing on?", view=HomeMenu())
        elif selection == "At a Gym":
            await interaction.response.edit_message(content="Which muscle group are you focusing on?", view=GymMenu())

class HomeMenu(discord.ui.View):
    @discord.ui.select(
        placeholder="[SELECT]",
        min_values=1,
        max_values=10,
        options=[
            discord.SelectOption(label="Shoulders", description="Anterior, Lateral, and Posterior Deltoids"),
            discord.SelectOption(label="Chest", description="Clavicular and Sternal Heads"),
            discord.SelectOption(label="Back", description="Trapezius, Latissimus, Rhomboids, and Teres Major/Minor"),
            discord.SelectOption(label="Biceps", description="Biceps Brachii and Brachialis"),
            discord.SelectOption(label="Triceps", description="Triceps Brachii"),
            discord.SelectOption(label="Abs", description="Transversus Abdominis and Internal/External Obliques"),
            discord.SelectOption(label="Glutes", description="Gluteus Maximus, Medius and Minimus"),
            discord.SelectOption(label="Quads", description="Rectus Femoris, Vastus Lateralis, and Vastus Intermedius/Lateralis"),
            discord.SelectOption(label="Hamstrings", description="Biceps Femoris, Semitendinosus, and Semimembranosus"),
            discord.SelectOption(label="Calves", description="Gastrocnemius and Soleus"),
        ]
    )
    async def home_select(self, interaction: discord.Interaction, select: discord.ui.Select):
        selections = select.values
        home_list = ", ".join(f"**{group}**" for group in selections)
        lines = [f"You selected: {home_list}"]
        for group in selections:
            match group:
                case "Shoulders":
                    lines.append("\nShoulder Exercises")
                    lines.extend([
                        "1. Moon Goddess",
                        "2. Decline Push-up",
                        "3. Pike Push-up",
                    ])
                case "Chest":
                    lines.append("\nChest Exercises")
                    lines.extend([
                        "1. Incline Push-up",
                        "2. Decline Push-up",
                        "3. Push-up",
                    ])
                case "Back":
                    lines.append("\nBack Exercises")
                    lines.extend([
                        "1. Inverted Row",
                        "2. Pull-up",
                        "3. Chin-up",
                    ])
                case "Biceps":
                    lines.append("\nBicep Exercises")
                    lines.extend([
                        "1. Reverse Grip Inverted Row",
                        "2. Backpack Curl",
                        "3. Chin-up",
                    ])
                case "Triceps":
                    lines.append("\nTricep Exercises")
                    lines.extend([
                        "1. Triangle Push-up",
                        "2. Bodyweight Dip",
                        "3. Bodyweight Tricep Extension",
                    ])
                case "Abs":
                    lines.append("\nAb Exercises")
                    lines.extend([
                        "1. Sit-up",
                        "2. Plank",
                        "3. Hanging Leg Raise",
                    ])
                case "Glutes":
                    lines.append("\nGlute Exercises")
                    lines.extend([
                        "1. Glute Bridge",
                    ])
                case "Quads":
                    lines.append("\nQuad Exercises")
                    lines.extend([
                        "1. Bodyweight Squat",
                        "2. Lunges",
                        "3. Bulgarian Split Squat",
                    ])
                case "Hamstrings":
                    lines.append("\nHamstring Exercises")
                    lines.extend([
                        "1. Bulgarian Split Squat",
                        "2. Lunges",
                    ])
                case "Calves":
                    lines.append("\nCalf Exercises")
                    lines.extend([
                        "1. Bodyweight Calf Raise",
                        "2. Seated Calf Raise",
                    ])

        message = "\n".join(lines)
        await interaction.response.edit_message(
            content=message,
            view=None
        )

class GymMenu(discord.ui.View):
    @discord.ui.select(
        placeholder="[SELECT]",
        min_values=1,
        max_values=10,
        options=[
            discord.SelectOption(label="Shoulders", description="Anterior, Lateral, and Posterior Deltoids"),
            discord.SelectOption(label="Chest", description="Clavicular and Sternal Heads"),
            discord.SelectOption(label="Back", description="Trapezius, Latissimus, Rhomboids, and Teres Major/Minor"),
            discord.SelectOption(label="Biceps", description="Biceps Brachii and Brachialis"),
            discord.SelectOption(label="Triceps", description="Triceps Brachii"),
            discord.SelectOption(label="Abs", description="Transversus Abdominis and Internal/External Obliques"),
            discord.SelectOption(label="Glutes", description="Gluteus Maximus, Medius and Minimus"),
            discord.SelectOption(label="Quads", description="Rectus Femoris, Vastus Lateralis, and Vastus Intermedius/Lateralis"),
            discord.SelectOption(label="Hamstrings", description="Biceps Femoris, Semitendinosus, and Semimembranosus"),
            discord.SelectOption(label="Calves", description="Gastrocnemius and Soleus"),
        ]
    )
    async def gym_select(self, interaction: discord.Interaction, select: discord.ui.Select):
        selections = select.values
        gym_list = ", ".join(f"**{group}**" for group in selections)
        lines = [f"You selected: {gym_list}"]
        for group in selections:
            match group:
                case "Shoulders":
                    lines.append("\nShoulder Exercises")
                    lines.extend([
                                "1. Dumbbell Shoulder Press",
                                "2. Dumbbell Lateral Raise",
                                "3. Barbell Upright Row",
                                "4. Barbell Military Press",
                                "5. Cable Lateral Raise",
                    ])
                case "Chest":
                    lines.append("\nChest Exercises")
                    lines.extend([
                                "1. Incline Bench Press",
                                "2. Flat Bench Press",
                                "3. Cable Chest Fly",
                                "4. Machine Pec-Dec Fly",
                                "5. Machine Chest Press",
                                "6. Push-up",
                    ])
                case "Back":
                    lines.append("\nBack Exercises")
                    lines.extend([
                                "1. Machine Row",
                                "2. Barbell Row",
                                "3. Dumbbell Row",
                                "4. Machine Lat Pull-down",
                                "5. Cable Lat Pullover",
                                "6. Assisted/Non-assisted Pull-up",
                                "7. Dumbbell Shrugs",
                                "8. Machine Pec-Dec Reverse Fly",
                                "9. Cable Reverse Fly",
                    ])
                case "Biceps":
                    lines.append("\nBicep Exercises")
                    lines.extend([
                                "1. Seated Preacher Curl",
                                "2. Dumbbell Curl",
                                "3. Barbell Curl",
                                "4. Dumbbell Hammer Curl",
                                "5. Cable Curl",
                                "6. Machine Reverse-Grip Lat Pull-down",
                    ])
                case "Triceps":
                    lines.append("\nTricep Exercises")
                    lines.extend([
                                "1. Cable Straight-bar Tricep Pushdown",
                                "2. Barbell Skull Crusher",
                                "3. Dumbbell Single-arm Extension",
                                "4. Cable Rope Tricep Pushdown",
                                "5. Cable Overhead Extension",
                    ])
                case "Abs":
                    lines.append("\nAb Exercises")
                    lines.extend([
                                "1. Decline Crunch",
                                "2. Stationary Leg Raise",
                                "3. Sit-up",
                                "4. Cable Crunch",
                                "5. Plank",
                                "6. Hanging Leg Raise",
                    ])
                case "Glutes":
                    lines.append("\nGlute Exercises")
                    lines.extend([
                                "1. Barbell Hip Thrust",
                                "2. Machine Hip Thrust",
                                "3. Barbell Romanian Deadlift",
                                "4. Barbell Conventional Deadlift",
                    ])
                case "Quads":
                    lines.append("\nQuad Exercises")
                    lines.extend([
                                "1. Barbell Squat",
                                "2. Dumbbell Goblet Squat",
                                "3. Machine Leg Extension",
                                "4. Dumbbell Bulgarian Split Squats",
                                "5. Dumbbell Lunges",
                                "6. Machine Leg Press",
                                "7. Machine Hack Squat",
                    ])
                case "Hamstrings":
                    lines.append("\nHamstring Exercises")
                    lines.extend([
                                "1. Barbell Deadlift",
                                "2. Barbell Romanian Deadlift",
                                "3. Dumbbell Romanian Deadlift",
                                "4. Machine Hamstring Curl",
                                "5. Bulgarian Split Squat",
                                "6. Dumbbell Lunges",
                    ])
                case "Calves":
                    lines.append("\nCalf Exercises")
                    lines.extend([
                                "1. Bodyweight Calf Raise",
                                "2. Machine Calf Raise",
                                "3. Seated Calf Raise",
                    ])

        message = "\n".join(lines)
        await interaction.response.edit_message(
            content=message,
            view=None
        )


@bot.event
async def on_ready():
    await tree.sync()
    print('Awaiting Server Input...')

@tree.command(name="workout", description="Find exercises that suit your workout")
async def workout(interaction: discord.Interaction):
    await interaction.response.send_message("Where will your workout take place?", view=LocationMenu(), ephemeral=True)

@tree.command(name="info", description="List of possible commands")
async def info(interaction: discord.Interaction):
    await interaction.response.send_message("\n\n"
                   "Commands:\n"
                   ".tips\n"
                   "-> some simple exercise advice\n"
                   ".workout\n"
                   "depending on your setting, discover what exercises are effective for each muscle\n"
                   ".ppl\n"
                   "-> description of push, pull, legs workout split\n"
                   ".ul\n"
                   "-> description of upper lower workout split\n"
                   ".split\n"
                   "-> other recommended split\n"
                   "    ", ephemeral=True)

@tree.command(name="tips", description="Helpful information about common workout practices")
async def tips(interaction: discord.Interaction):
    await interaction.response.send_message("\n\n"
                   "Workout Tips:\n"
                   "1. Make sure each exercise is performed for 2-4 sets.\n"
                   "2. Each set should be between 6-15 reps.\n"
                   "3. Take short breaks inbetween sets.\n"
                   "4. If you don't feel a given exercise in its intended muscle, feel free to change exercises once the current set is done.\n"
                   "5. For information about how to perform each exercise, consult images on machines around your gym or google the phrase provided in the .workout section.\n"
                   "6. Perform a workout 4-6 days each week for best results."
                   "    ", ephemeral=True)

@tree.command(name="ppl", description="Example Push, Pull, Legs Split")
async def ppl(interaction: discord.Interaction):
    await interaction.response.send_message("\n\n"
                   "Push, Pull, Legs Split:\n"
                   "Day 1\n"
                   "-> 18-22 Sets\n"
                   "-> Focus on Tricep, Shoulder, and Chest exercises\n"
                   "Day 2\n"
                   "-> 15-20 Sets\n"
                   "-> Focus on Back and Bicep exercises\n"
                   "Day 3\n"
                   "-> 18-22 Sets\n"
                   "-> Focus on Quad, Hamstring, Glute, Ab, and Calf exercises\n"
                   "Day 4\n"
                   "-> Rest\n"
                   "Day 5\n"
                   "-> Rest again or Start from Day 1\n"
                   "    ", ephemeral=True)

@tree.command(name="ul", description="Example Upper, Lower Split")
async def ul(interaction: discord.Interaction):
    await interaction.response.send_message("\n\n"
                   "Upper, Lower Split:\n"
                   "Day 1\n"
                   "-> 20-30 Sets\n"
                   "-> Focus on Tricep, Bicep, Back, Shoulder, and Chest exercises\n"
                   "Day 2\n"
                   "-> 20-30 Sets\n"
                   "-> Focus on Quad, Hamstring, Glute, Ab, and Calf exercises\n"
                   "Day 3\n"
                   "-> Rest\n"
                   "Day 4\n"
                   "-> Rest again or Start from Day 1\n"
                   "    ", ephemeral=True)

@tree.command(name="split", description="Other Example Workout Split")
async def split(interaction: discord.Interaction):
    await interaction.response.send_message("\n\n"
                   "Other Split:\n"
                   "Day 1\n"
                   "-> 15-20 Sets\n"
                   "-> Focus on Shoulder and Chest exercises\n"
                   "Day 2\n"
                   "-> 15-20 Sets\n"
                   "-> Focus on Back exercises\n"
                   "Day 3\n"
                   "-> 15-20 Sets\n"
                   "-> Focus on Tricep and Bicep exercises\n"
                   "Day 4\n"
                   "-> Rest\n"
                   "Day 5\n"
                   "-> 15-20 Sets\n"
                   "-> Focus on Quad, Hamstring, Glute, Ab, and Calf exercises\n"
                   "Day 5\n"
                   "-> Rest\n"
                   "Day 6\n"
                   "-> Start from Day 1\n"
                   "    ", ephemeral=True)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
