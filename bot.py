from pyrogram import Client, filters
import re
import os

# Fetch bot credentials from environment variables
API_ID = int(os.getenv("API_ID"))  
API_HASH = os.getenv("API_HASH")  
BOT_TOKEN = os.getenv("BOT_TOKEN")  

# Fetch channel usernames from environment variables
SOURCE_CHANNEL = os.getenv("SOURCE_CHANNEL")  
DEST_CHANNEL = os.getenv("DEST_CHANNEL")  

# Predefined caption template
CAPTION_TEMPLATE = """✅ Key Updated Successfully!

♻️Esᴘ - ❕
♻️Tᴏᴜᴄʜ-Aɪᴍʙᴏᴛ Bʀᴜᴛᴛᴛᴀʟ - 👽
♻️Nᴏ ʀᴇᴄᴏɪʟ - ⭕️
♻️Iɢɴᴏʀᴇ Kɴᴏᴄᴋᴇᴅ / Vɪsɪʙɪʟɪᴛʏ Cʜᴇᴄᴋ⚠️
♻️Oɴʟɪɴᴇ Bʏᴘᴀss Sʏsᴛᴇᴍ - 🌀

Key - {}

𝗗𝗶𝗿𝗲𝗰𝘁 𝗟𝗼𝗴𝗶𝗻 𝗠𝗮𝗶𝗻 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 ☠

𝗝𝗼𝗶𝗻 𝗦𝗵𝗮𝗿𝗲 & 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 🤩
https://t.me/LocalCheat
https://t.me/LocalCheat

𝗡𝗼𝘁𝗲 :
𝗢𝗻𝗹𝘆 𝗦𝗮𝗳𝗲 𝗛𝗮𝗰𝗸𝘀 𝗣𝗿𝗼𝘃𝗶𝗱𝗶𝗻𝗴 ✅
  𝗨𝘀𝗲𝗹𝗲𝘀𝘀 𝗹𝗼𝗮𝗱𝗲𝗿 𝗼𝗿 𝗠𝗼𝗱𝘀🚫
     𝗜𝗮𝗺 𝗡𝗼𝘁 𝗣𝗿𝗼𝘃𝗶𝗱𝗶𝗻𝗴 ❎

𝗥𝘂𝗹𝗲𝘀 : https://t.me/LocalCheat/153

   𝗪𝗮𝗻𝘁 𝗕𝘂𝘆 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 ❕
     @LocalxCheats 👽
"""

# Initialize bot
bot = Client("apk_forward_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.channel & filters.document & filters.chat(SOURCE_CHANNEL))
async def forward_apk(client, message):
    # Extract the key from the source channel
    caption_text = message.caption or ""  # Ensure caption is a string
    key_match = re.search(r"Key\s*-\s*(\S+)", caption_text)
    extracted_key = key_match.group(1) if key_match else "Unknown"

    # Format the key for One-Tap Copy (Mono Text)
    formatted_key = f"`{extracted_key}`"  # Single backticks for Telegram Mono Text

    # Create the final caption with the formatted key
    formatted_caption = CAPTION_TEMPLATE.format(formatted_key)

    # Forward the APK without forward tags
    await client.send_document(
        chat_id=DEST_CHANNEL,
        document=message.document.file_id,
        caption=formatted_caption
    )

    print(f"APK forwarded with key: {extracted_key}")

# Start bot
print("Bot is running...")
bot.run()
