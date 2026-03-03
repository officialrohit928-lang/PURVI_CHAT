# Don't remove This Line From Here.
# Telegram :- @ll_ALPHA_BABY_lll

import requests
from pyrogram import filters
from pyrogram.types import Message
from RAUSHAN import dev

API_URL = "https://tg-2-num-api-org.vercel.app/api/search?userid="

@dev.on_message(filters.command("search") & ~filters.bot)
async def search_user(client, message: Message):

    if len(message.command) < 2:
        return await message.reply_text(
            "❌ Usage:\n/search 123456789"
        )

    user_id = message.command[1]

    msg = await message.reply_text("🔎 Searching... Please wait")

    try:
        response = requests.get(API_URL + user_id, timeout=10)
        data = response.json()

        country = data.get("country", "India (+91)")
        number = data.get("number", "Not Found")
        expiry = data.get("expiry", "April 6, 2026")
        remaining = data.get("remaining", "Unknown")
        balance = data.get("balance", "9")

        await msg.edit_text(f"""
✅ Search Results

🌍 Country: {country}
📞 Number: {number}

⏳ Validity Info:
📅 Expires on: {expiry}
🕒 Remaining: {remaining}

💰 Your balance: {balance} credits
""")

    except Exception as e:
        await msg.edit_text("❌ API Error or Invalid User ID")
