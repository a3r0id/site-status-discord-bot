from config import data
import discord
from datetime import datetime, timezone
def embed_alert(body, alert_type):
    if alert_type == 0:
        alert = "General Notification"
        icon_ = "https://host-info.net/cdn/img/info_red.png"
    else:
        alert = "Error Notification"
        icon_ = "https://host-info.net/cdn/img/alert.png"
        
    embed = discord.Embed(
        title=data.bot_name,
        description=alert,
        url=data.my_url,
        color=data.embed_color
        )
    
    embed.set_thumbnail(url=icon_)
    now_utc = datetime.now(timezone.utc)
    
    embed.add_field(name="__Message:__", value=f"```css\n{body}\n```", inline=False)
    embed.add_field(name="__Time now:__", value="> UTC: \n> " + str(now_utc)+ "\n> Local: \n> " + str(datetime.now()), inline=False)
    embed.set_footer(text=f"Remote Website Monitoring For Discord | Admin Channel")
    return embed

