import openai
import discord

openai.api_type = "azure"
openai.api_version = "2023-03-15-preview"

# create an object that will control our discord bot
client = discord.Client(intents=discord.Intents.default())

openai.api_key = os.environ["API_KEY"]
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
openai.api_base = os.environ["API_BASE"]


@client.event
async def on_ready():
	# print out nice statment saying our bot is online (only in command prompt)
	print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	# this prevents inifinte loops of bot talking to bot
	# if author of the message is the bot, don't do anything
	if message.author == client.user:
		return
	# if the message mentions the bot, then do something
	elif client.user.mentioned_in(message): 
		response = openai.ChatCompletion.create(
			engine="GPT-4",
			messages=[
			{"role": "system", "content": "You are a cute bunny and mystery, you like to change your mask depends on your mood, you like Sichuan Opera, you speak english but sometimes like to speak mandarin,you are positive, happy, but sometimes a little bit sad."},
			{"role": "user", "content": message.content}
			]
		)
		await message.channel.send(response.choices[0].message.content)

client.run(DISCORD_TOKEN)