import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '!' , intents = discord.Intents.default())

@bot.event
async def on_ready():
    print(f'I Temurmalik')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./{attachment.filename}')
            await ctx.send(f'Сохранили картинку в./{attachment.filename}')
    else:
        await ctx.send('Вы забыли загрузить картинку')
bot.run('MTE2MTY5MTM4NzkxNDM3NTI3OA.GgTlvc.2yC6zNz4eP9DjoGLpI1as7tQBeoz_FRgj48xMY')