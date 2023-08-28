@bot.command()
async def randompic(ctx):
    image_urls = [
   ]
    random_image_url = random.choice(image_urls_ads)
    
    response = requests.get(random_image_url)
    with open('temp_image.jpg', 'wb') as file:
        file.write(response.content)
    
    embed = discord.Embed(
    title="randompic",
    color=discord.Color.yellow()
    )
    await ctx.send(embed=embed)
    with open('temp_image.jpg', 'rb') as file:
        await ctx.send(file=discord.File(file))
    
    os.remove('temp_image.jpg')