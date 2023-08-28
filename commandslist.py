@bot.command()
async def commands(ctx):
    embed = discord.Embed(
        title="title",
        description="description.",
        color=discord.Color.blue()
    )
    embed.add_field(name="commands", value="add your list of commands here", inline=True)
    
    await ctx.send(embed=embed)