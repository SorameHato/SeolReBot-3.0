# coding: utf-8
import discord
from discord.ext import commands
global guild_ids
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from main import guild_ids

class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Short Input"))
        self.add_item(discord.ui.InputText(label="Long Input", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Modal Results")
        embed.add_field(name="Short Input", value=self.children[0].value)
        embed.add_field(name="Long Input", value=self.children[1].value)
        await interaction.response.send_message(embeds=[embed])

class MyView(discord.ui.View):
    @discord.ui.button(label="Send Modal")
    async def button_callback(self, button, interaction):
        await interaction.response.send_modal(MyModal(title="Modal via Button"))

class modal(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.slash_command(guild_ids=guild_ids)
    async def modal_slash(self, ctx: discord.ApplicationContext):
        """Shows an example of a modal dialog being invoked from a slash command."""
        modal = MyModal(title="Modal via Slash Command")
        await ctx.send_modal(modal)
    
    @commands.slash_command(guild_ids=guild_ids)
    async def send_modal(self,ctx):
        await ctx.respond(view=MyView())

def setup(bot):
    bot.add_cog(modal(bot))