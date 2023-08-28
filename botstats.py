@bot.command()
async def stats(ctx):
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    network = psutil.net_io_counters()

    embed = discord.Embed(
    title="botstats",
    description="description",
    color=discord.Color.blue()
    )
    embed.add_field(name="cpu:", value=f"{cpu_percent:.2f}%")
    embed.add_field(name="ram:", value=f"{memory.percent:.2f}%")
    embed.add_field(name="packet send", value=f"{network.bytes_sent / 1e9:.2f} GB")
    embed.add_field(name="packet recivied:", value=f"{network.bytes_recv / 1e9:.2f} GB")

    await ctx.send(embed=embed)