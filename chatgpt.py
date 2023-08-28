openai.api_key = openai.api_key

def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0.7,
        max_tokens=1999,
        n=1,
        stop=None
    )

    try:
        total_tokens = len(response.choices[0].text)
        max_tokens_limit = 90000

        if total_tokens > max_tokens_limit:
            response = response.choices[0].text[:max_tokens_limit]
        else:
            response = response.choices[0].text
    except IndexError:
        response = response.choices[0].text

    return response.strip()

@bot.event
async def on_message(message):
    if message.channel.id == chat_gpt_id and not message.author.bot:
        async with message.channel.typing():
            query = message.content[len("! "):]  # Remove the "!t " prefix from the message
            response = generate_response(query)
            embed = discord.Embed(title="Ответ ИИ", description=response, color=discord.Color.green())
            await message.channel.send(embed=embed)

    await bot.process_commands(message)