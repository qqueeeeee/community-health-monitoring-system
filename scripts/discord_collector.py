import discord
import pandas as pd
import asyncio
from datetime import datetime, timedelta, timezone

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = "CHANNEL_ID"
BATCH_SIZE = 1000

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    cutoff = datetime.now(timezone.utc) - timedelta(days=60)

    rows = []
    count = 0

    async for message in channel.history(limit=None, after=cutoff, oldest_first=True):
        if message.author.bot:
            continue

        rows.append({
            "event_type": "message_sent",
            "user_id": message.author.id,
            "channel_id": message.channel.id,
            "guild_id": message.guild.id,
            "event_time": message.created_at.isoformat(),
            "content_length": len(message.content),
            "has_embed": bool(message.embeds),
            "has_attachment": bool(message.attachments),
            "is_interaction_command": message.interaction is not None
        })

        count += 1

        if count % BATCH_SIZE == 0:
            pd.DataFrame(rows).to_csv(
                "discord_60d_messages.csv",
                mode="a",
                header=(count == BATCH_SIZE),
                index=False
            )
            rows.clear()
            await asyncio.sleep(1.5)

    if rows:
        pd.DataFrame(rows).to_csv(
            "discord_60d_messages.csv",
            mode="a",
            header=(count <= BATCH_SIZE),
            index=False
        )

    await client.close()

client.run(BOT_TOKEN)
