import discord
from discord.ext import commands

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
        # Disable all buttons in this view
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
            "🔒 **Oxygen Dev Network Rules**\n\n"
            "1️⃣ Be respectful and kind to all members.\n"
            "2️⃣ No spamming, advertising, or self-promotion outside designated channels.\n"
            "3️⃣ Use channels for their intended topics to keep discussions organized.\n"
            "4️⃣ Keep conversations professional and avoid offensive language.\n"
            "5️⃣ Help others when you can, and ask for help when needed.\n"
            "6️⃣ Respect moderators and staff decisions.\n"
            "7️⃣ Protect everyone’s privacy—no sharing personal info without consent.\n\n"
            "🚨 Violations may lead to warnings, mutes, kicks, or bans depending on severity.\n"
            "🙏 Thanks for helping keep our community positive and productive!"
        )
        await channel.send(rules_message)


async def send_goals_message():
    channel = bot.get_channel(GOALS_CHANNEL_ID)
    if channel:
        goals_message = (
            "🔒 **Oxygen Dev Network Goals**\n\n"
            "🎯 Our Vision:\n"
            "To build a thriving, inclusive community where passionate learners and developers come together to master Python, bot development, and automation.\n\n"
            "🌟 What We Aim To Achieve:\n"
            "1️⃣ Foster a supportive learning environment.\n"
            "2️⃣ Promote collaboration and networking.\n"
            "3️⃣ Provide quality resources and guidance.\n"
            "4️⃣ Host events and workshops.\n"
            "5️⃣ Encourage innovation and problem solving.\n"
            "6️⃣ Build a positive and respectful community culture.\n"
            "7️⃣ Support career growth and development.\n\n"
            "🚀 Together, we’ll learn, build, and innovate — one line of code at a time!"
        )
        await channel.send(goals_message)


async def send_start_here_message():
    channel = bot.get_channel(START_HERE_CHANNEL_ID)
    if channel:
        start_here_message = (
            "🔒 **Welcome to Oxygen Dev Network!**\n\n"
            "👋 **New here? This is a great place to begin your journey!**\n\n"
            f"1️⃣ **Read our rules in <#{RULES_CHANNEL_ID}>** — helps keep our community respectful and safe.\n"
            f"2️⃣ **Introduce yourself in <#{INTRODUCTIONS_CHANNEL_ID}>** — say hi and tell us about yourself!\n"
            f"3️⃣ **Discover our vision in <#{GOALS_CHANNEL_ID}>** — see what we’re building together.\n\n"
            "✨ **Tips for a great start:**\n"
            "- Engage with the community and ask questions.\n"
            "- Join events and collaborate on projects.\n"
            "- Share your progress and help others when you can.\n\n"
            "🚀 **Let’s make coding and automation fun and rewarding!**\n\n"
            "**Choose your learning focus below:**"
        )
        await channel.send(start_here_message, view=RoleButtonsView())


@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")


@bot.event
async def on_member_join(member):
    # Send welcome message in introductions channel
    intro_channel = bot.get_channel(INTRODUCTIONS_CHANNEL_ID)
    if intro_channel:
        welcome_message = (
            f"🎉 **Welcome {member.mention} to Oxygen Dev Network!** \n\n"
            "✨ We're thrilled to have you here! ✨\n\n"
            "💬 **Please introduce yourself:**  \n"
            "Tell us your name, your interests, and what you're excited to learn or build with us.\n\n"
            "Let's grow, create, and code together in this amazing community!\n\n"
            "If you need any help, don’t hesitate to ask. Welcome aboard!"
        )
        await intro_channel.send(welcome_message)

    # Send other messages
    await send_rules_message()
    await send_goals_message()
    await send_start_here_message()

# Replace with your Bot Token
bot.run("YOUR_BOT_TOKEN")