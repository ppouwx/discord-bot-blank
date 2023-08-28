@bot.command()
async def rps(ctx):
    choices = ['rock', 'paper', 'scissors']

    embed = discord.Embed(title="Rock-Paper-Scissors", color=discord.Color.blue())
    embed.description = "Select your choice:"

    message = await ctx.send(embed=embed)
    for emoji in ['🪨', '✂️', '📜']:
        await message.add_reaction(emoji)

    def check(reaction, user):
        return user == ctx.author and reaction.message.id == message.id and str(reaction.emoji) in ['🪨', '✂️', '📜']

    try:
        reaction, user = await bot.wait_for("reaction_add", check=check, timeout=60)
        user_choice = str(reaction.emoji)

        bot_choice = random.choice(choices)

        result_embed = discord.Embed(title="Rock-Paper-Scissors", color=discord.Color.blue())
        result_embed.add_field(name="Your choice", value=user_choice, inline=True)
        result_embed.add_field(name="Bot choice", value=bot_choice, inline=True)

        if user_choice == '🪨' and bot_choice == 'scissors':
            result_embed.description = "You win!"
        elif user_choice == '✂️' and bot_choice == 'paper':
            result_embed.description = "You lose!"
        elif user_choice == '📜' and bot_choice == 'rock':
            result_embed.description = "You win!"
        elif user_choice == bot_choice:
            result_embed.description = "Tile!"
        else:
            result_embed.description = "Tile!"

        await ctx.send(embed=result_embed)

    except asyncio.TimeoutError:
        await message.clear_reactions()