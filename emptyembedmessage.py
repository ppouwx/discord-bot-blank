@bot.command()
async def embed(ctx):
    embed = discord.Embed(
        title="empty",
        description="empty",
        color=discord.Color.purple()
    )
    
    await ctx.send(embed=embed)