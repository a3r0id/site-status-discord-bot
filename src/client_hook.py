from config import data
import discord
class logging:
    class load:
        def __init__(self, client):
            self.client = client
        def test_channels(self):
            this = {}
            admin = False
            public = False
            try:
                admin_channel = self.client.get_channel(
                    data.admin_log_channel_id
                    )
                this['admin'] = admin_channel.name
                this['admin_guild_name'] = admin_channel.guild.name
                this['admin_channel_name'] = admin_channel.name
                admin = True
            except Exception as e:
                this['admin'] = str(e)
            try:
                public_channel = self.client.get_channel(
                    data.public_update_channel_id
                    )
                this['public'] = admin_channel.name
                this['public_guild_name'] = public_channel.guild.name
                this['public_channel_name'] = public_channel.name
                public = True
            except Exception as e:
                this['public'] = str(e)
            if admin != True or public != True:
                this['result'] = None
            else:
               this['result'] = 1
            return this

        def admin_channel(self):
            return self.client.get_channel(
                data.admin_log_channel_id
                )

        def public_channel(self):
            return self.client.get_channel(
                data.public_update_channel_id
                )

