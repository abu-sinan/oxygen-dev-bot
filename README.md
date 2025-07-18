[Oxygen Dev Network Bot](https://github.com/abu-sinan/oxygen-dev-bot/blob/main/thumbnail.png)
# Oxygen Dev Network Bot 🤖🚀

A custom Python Discord bot for the **Oxygen Dev Network**, designed to automate onboarding and guide new members with interactive role buttons, custom rules, goals, and welcome messages.

---

## 📋 Features

- 🎉 Auto welcome message (styled) when a new member joins.
- 📜 Auto-sends detailed server rules.
- 🎯 Posts community goals in a clear, professional style.
- 📚 “Start Here” guide with clickable buttons.
- 🔘 Interactive role selection with Python, Bot Dev, and Automation buttons.
- ⏳ Buttons automatically disable after selection.
- ✉️ Ephemeral (private) guidance after choosing a focus area.

---

## 🚀 Setup Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/abu-sinan/oxygen-dev-bot.git
cd oxygen-dev-bot
```

---

### 2️⃣ Install Requirements

```bash
pip install discord.py python-dotenv
```

---

### 3️⃣ Configuration

- Create a file named `.env`:

```.env
DISCORD_TOKEN=your-bot-token-here
```

- Ensure your bot token stays **secret** (it’s ignored by Git via `.gitignore`).

---

### 4️⃣ Run the Bot

```bash
python bot.py
```

The bot will:

- Automatically send the welcome, rules, goals, and start-here messages.

- Allow new members to choose their learning focus via interactive buttons.

---

## 📂 File Structure

```
oxygen-dev-bot/
├── bot.py
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Required Bot Permissions

- Server Members Intent (enabled in Discord Developer Portal).

- Permission to manage messages and send messages in target channels.

---

## 📄 License

[MIT License](https://github.com/abu-sinan/oxygen-dev-bot/blob/main/LICENSE)

---

## 🙌 Contributing

Pull requests, feature ideas, and feedback are welcome!
Feel free to open an issue or contribute via fork and PR.

---

## 💬 Questions?

For help or suggestions, join the Oxygen Dev Network Discord Server.

---

Let’s grow, build, and code together! 💻🌱
