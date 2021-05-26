import discord
from discord.ext import commands
from style_wraps import code_block
from db_engine import db_from_scratch

if __name__ == '__main__':
    db_from_scratch()

    from commands.hero_commands import hero_commands

    # Bot configuration and routing
    bot = commands.Bot(command_prefix='pn ')
    hero_commands(bot)

    @bot.command()
    async def ping(ctx):
        """Checks if the bot is ALIVE!"""
        await ctx.send(code_block('pong'))

    bot.run('ODQ1ODg2ODQxMDM4NTY5NTAy.YKnfgg.LhaesFIaiWhYo2b6GZHp2fJTGKI')
