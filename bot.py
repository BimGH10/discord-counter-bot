import discord
import os

CHANNEL_ID = 1465855344944087305  # ID kênh

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

client = discord.Client(intents=intents)

message_count = 0

@client.event
async def on_ready():
    global message_count
    print(f"Đã đăng nhập: {client.user}")

    channel = client.get_channel(CHANNEL_ID)
    message_count = 0

    async for msg in channel.history(limit=None):
        if not msg.author.bot:
            message_count += 1

    await channel.edit(name=f"『🟢』vouches「{message_count}」")
    print("Đã cập nhật lần đầu")

@client.event
async def on_message(message):
    global message_count

    if message.channel.id == CHANNEL_ID and not message.author.bot:
        message_count += 1
        new_name = f"『🟢』vouches「{message_count}」"
        await message.channel.edit(name=new_name)
        print("Đã cập nhật:", new_name)

client.run(os.getenv("TOKEN"))
