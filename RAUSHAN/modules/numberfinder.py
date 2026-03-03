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
        return await message.reply_text("❌ Usage:\n/search 123456789")

    user_id = message.command[1]
    msg = await message.reply_text("🔎 Searching... Please wait")

    try:
        response = requests.get(API_URL + user_id, timeout=10)
        result = response.json()

        if result.get("status") != "success":
            return await msg.edit_text("❌ API Failed")

        data = result.get("data", {})
        validity = result.get("validity", {})

        if not data.get("found"):
            return await msg.edit_text("❌ Number Not Found")

        country = data.get("country")
        code = data.get("country_code")
        number = data.get("number")

        expiry = validity.get("expires_on")
        days = validity.get("days_remaining")
        hours = validity.get("hours_remaining")

        await msg.edit_text(f"""
✅ Search Results

🌍 Country: {country} ({code})
📞 Number: {number}

⏳ Validity Info:
📅 Expires on: {expiry}
🕒 Remaining: {days} days, {hours} hours
""")

    except Exception:
        await msg.edit_text("❌ API Error")
