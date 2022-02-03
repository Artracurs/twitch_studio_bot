import win32com.client as comclt
from twitchio.ext import commands

wsh = comclt.Dispatch("WScript.Shell")

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token='ACCESS_TOKEN', prefix='!', initial_channels=['...'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    @commands.command()
    async def tv(self, ctx: commands.Context):
        wsh.AppActivate("TWITCH STUDIO")
        wsh.SendKeys("^K")
        await ctx.send(f'{ctx.author.name} вывел видео на весь экран')

    @commands.command()
    async def back(self, ctx: commands.Context):
        wsh.AppActivate("TWITCH STUDIO")
        wsh.SendKeys("^L")
        await ctx.send(f'{ctx.author.name} вернул обратно в общий режим')



bot = Bot()
bot.run()


