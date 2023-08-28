@bot.command()
async def hug(ctx, member: discord.Member = None):
    if member is None:
        error_embed = discord.Embed(
            title="Error",
            description="Tag user which you want to hug.",
            color=discord.Color.red()
        )
        await ctx.send(embed=error_embed)
        return
    
    action_embed = discord.Embed(
        title=f"{ctx.author.display_name} hugs {member.display_name} 🤗",
        color=discord.Color.yellow()
    )
    await ctx.send(embed=action_embed)

@bot.command()
async def kiss(ctx, member: discord.Member = None):
    if member is None:
        error_embed = discord.Embed(
            title="Error",
            description="Tag user which you want to kiss.",
            color=discord.Color.red()
        )
        await ctx.send(embed=error_embed)
        return
    
    action_embed = discord.Embed(
        title=f"{ctx.author.display_name} kiss {member.display_name} 😘",
        color=discord.Color.yellow()
    )
    await ctx.send(embed=action_embed)