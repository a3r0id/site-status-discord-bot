from config import data
import discord
from datetime import datetime,timezone
def embed_content(stuff):
    # If malformed url, swap to avoid discord error.
    url = data.my_url
    if "http" not in data.my_url:
        url = "https://host-info.net"
    embed = discord.Embed(
        title=data.bot_name,
        description=f"**Current Status For `{data.my_url.replace('https://', '').replace('http://', '').replace('/', '')}`**",
        url=url,
        color=data.embed_color
        )
    embed.set_thumbnail(
        url=data.thumbnail_url
        )
    now_utc = datetime.now(timezone.utc)
    embed.add_field(name="__Status:__", value="> " + str(stuff['status']), inline=False)
    embed.add_field(name="__Response Code:__", value="> " + str(stuff['status_code']), inline=False)
    embed.add_field(name="__Response Time:__", value="> " + str(stuff['request_time']) + " Seconds", inline=False)
    embed.add_field(name="__Port Used:__", value="> " + str(stuff['port_used']), inline=False)
    embed.add_field(name="__Time now:__", value="> UTC: \n> " + str(now_utc)+ "\n> Local: \n> " + str(datetime.now()), inline=False)
    embed.set_footer(text=f"Remote Website Monitoring For Discord | Next Check: {data.interval_time} sec/s.")
    return embed

