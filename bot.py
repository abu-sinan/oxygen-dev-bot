import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Replace with your actual channel IDs
RULES_CHANNEL_ID = 1395712126781231226
INTRODUCTIONS_CHANNEL_ID = 1395712192640192552
GOALS_CHANNEL_ID = 1395712311242653726
START_HERE_CHANNEL_ID = 1395712252275068948

PYTHON_HELP_CHANNEL_ID = 1395712668098363502
BOT_DEV_HELP_CHANNEL_ID = 1395712728953524384
AUTOMATION_HELP_CHANNEL_ID = 1395712810805235823


class RoleButtonsView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def disable_all_buttons(self, interaction: discord.Interaction):
        for child in self.children:
            child.disabled = True
        await interaction.message.edit(view=self)

    @discord.ui.button(label="🐍 Python", style=discord.ButtonStyle.primary)
    async def python_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            f"🐍 You chose **Python**! Visit your help channel here: <#{PYTHON_HELP_CHANNEL_ID}>",
            ephemeral=True
        )
        await self.disable_all_buttons(interaction)

    @discord.ui.button(label="🤖 Bot Dev", style=discord.ButtonStyle.success)
    async def botdev_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            f"🤖 You chose **Bot Development**! Visit your help channel here: <#{BOT_DEV_HELP_CHANNEL_ID}>",
            ephemeral=True
        )
        await self.disable_all_buttons(interaction)

    @discord.ui.button(label="⚙️ Automation", style=discord.ButtonStyle.secondary)
    async def automation_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            f"⚙️ You chose **Automation**! Visit your help channel here: <#{AUTOMATION_HELP_CHANNEL_ID}>",
            ephemeral=True
        )
        await self.disable_all_buttons(interaction)


async def send_rules_message():
    channel = bot.get_channel(RULES_CHANNEL_ID)
    if channel:
        rules_message = (
            "📜 **Oxygen Dev Network Rules**\n\n"
            "1️⃣ Be respectful and professional to everyone.\n"
            "2️⃣ No spam, ads, or self-promotion.\n"
            "3️⃣ Keep conversations in relevant channels.\n"
            "4️⃣ Use appropriate language and avoid offensive content.\n"
            "5️⃣ Help others, and ask questions politely.\n"
            "6️⃣ Respect staff decisions.\n"
            "7️⃣ Protect everyone’s privacy.\n\n"
            "🚨 Breaking rules may lead to warnings, mutes, kicks, or bans.\n\n"
            "Thanks for helping us build a positive and professional community! 🚀"
        )
        await channel.send(rules_message)


async def send_goals_message():
    channel = bot.get_channel(GOALS_CHANNEL_ID)
    if channel:
        goals_message = (
            "🎯 **Oxygen Dev Network Goals**\n\n"
            "🚀 **Our Mission:** Build a collaborative, supportive community for Python, bot development, and automation enthusiasts.\n\n"
            "**We aim to:**\n"
            "- Provide quality resources and guidance.\n"
            "- Help developers grow through collaboration.\n"
            "- Run community events and workshops.\n"
            "- Support project-based learning and real-world skills.\n"
            "- Foster a welcoming, respectful environment.\n"
            "- Create opportunities for networking and team building.\n"
            "- Encourage open sharing of knowledge and ideas.\n\n"
            "Together, we grow as developers. 💻🌱"
        )
        await channel.send(goals_message)


async def send_start_here_message():
    channel = bot.get_channel(START_HERE_CHANNEL_ID)
    if channel:
        start_here_message = (
            "📚 **Welcome to Oxygen Dev Network!**\n\n"
            "👋 **New here? Start here:**\n\n"
            f"1️⃣ **Read the rules** in <#{RULES_CHANNEL_ID}>.\n"
            f"2️⃣ **Introduce yourself** in <#{INTRODUCTIONS_CHANNEL_ID}>.\n"
            f"3️⃣ **See our goals** in <#{GOALS_CHANNEL_ID}>.\n\n"
            "💡 **Choose your learning focus below:**"
        )
        await channel.send(start_here_message, view=RoleButtonsView())


@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")


@bot.event
async def on_member_join(member):
    intro_channel = bot.get_channel(INTRODUCTIONS_CHANNEL_ID)
    if intro_channel:
        welcome_message = (
            f"🎉 **Welcome {member.mention} to _Oxygen Dev Network_!** 🚀\n\n"
            "✨ We're thrilled to have you here! ✨\n\n"
            "💬 **Please introduce yourself:**\n"
            "Tell us your name, your interests, and what you're excited to learn or build with us.\n\n"
            "🌱 Let's grow, create, and code together in this amazing community!\n\n"
            "If you need any help, don’t hesitate to ask. Welcome aboard! 🎈"
        )
        await intro_channel.send(welcome_message)

    await send_rules_message()
    await send_goals_message()
    await send_start_here_message()


bot.run(TOKEN)