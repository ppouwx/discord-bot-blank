@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    activity = discord.Activity(type=discord.ActivityType.listening, name="/commands")
    await bot.change_presence(activity=activity)