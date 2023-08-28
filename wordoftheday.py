@bot.command()
async def wordoftheday(ctx):
    data = load_data()
    current_date = datetime.now().strftime('%Y-%m-%d')

    if current_date in data:
        word_of_the_day = data[current_date]
    else:
        word_of_the_day = random.choice(word_list_daily)
        data[current_date] = word_of_the_day
        save_data(data)
    random_word = random.choice(word_list_daily)
    embed = discord.Embed(
        title="Today word of the day is:",
        color=discord.Color.yellow()

    )
    
    await ctx.send(embed=embed)
    await ctx.send(f"{word_of_the_day}")