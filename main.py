import datetime

import settings
import discord
from discord.ext import commands


def main():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.messages = True
    intents.dm_messages = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    """Standard on_ready event für die Konsole"""
    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)

    """Willkommen message, noch in Bearbeitung"""

    @bot.event
    async def on_member_join(member):
        welcome = bot.get_channel(1183485812076187780)
        welcome_embed = discord.Embed(title="Willkommen",
                                      description=f"Willkommen {member}",
                                      color=0000000)
        await welcome.send(embed=welcome_embed)

    """Hier kommt die Magie. Die Bot message """

    @bot.event
    async def on_message(message):

        if message.author == bot.user:
            return

        if isinstance(message.channel, discord.DMChannel):
            dm_embed = discord.Embed(title="Jemand hat mir was zugeflüstert",
                                     description=message.content,
                                     color=0000000)
            """Ein Embed damit es gut aussieht"""
            dm_embed.set_footer(text="Flüstere mir etwas in den DM's zu")
            channel = bot.get_channel(1183485223497908274)
            dm_message = await channel.send(embed=dm_embed)
            """Message wird in den Channel geposted"""

            log_channel = bot.get_channel(1183485240891678731)
            log_embed = discord.Embed(title="Message Info",
                                      description=f"Autor: {message.author}\nZeitpunkt: {datetime.datetime.now().replace(microsecond=0)}\nNachricht: {message.content}",
                                      color=1234565
                                      )
            """Log-Daten werden erstellt"""

            jump_link = f"https://discord.com/channels/{dm_message.guild.id}/{dm_message.channel.id}/{dm_message.id}"

            """Anklickbares Element damit man zur dm_message springen kann."""

            log_embed.add_field(name="Nachricht anzeigen", value=f"[Klicke hier]({jump_link})", inline=False)

            await log_channel.send(embed=log_embed)

    bot.run(settings.DISCORD_API_SECRET)


if __name__ == '__main__':
    main()
