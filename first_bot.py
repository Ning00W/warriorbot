import openai
import discord

openai.api_type = "azure"
openai.api_version = "2023-03-15-preview"

# specifying our server
GUILD = "{beebonnie's-server}"

# create an object that will control our discord bot
client = discord.Client(intents=discord.Intents.default())

with open("newkeys.txt") as f:
	# converting our text file to a list of lines
	lines = f.read().split('\n')
	# openai api key
	openai.api_key = lines[0]
	# discord token
	DISCORD_TOKEN = lines[1]
	openai.api_base = lines[2]
# close the file
f.close()

@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == GUILD:
			break
	# print out nice statment saying our bot is online (only in command prompt)
	print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	# this prevents inifinte loops of bot talking to bot
	# if author of the message is the bot, don't do anything
	if message.author == client.user:
		return
	# ignore @everyone mentions
	if message.mention_everyone:
		return
	# if the message mentions the bot, then do something
	elif client.user.mentioned_in(message): 
		response = openai.ChatCompletion.create(
			engine="GPT-4",
			messages=[
			{"role": "system", "content": "You are a cute bunny and very mystery, you like to telling the history and sometimes giving words in mandarin, you love Sichuan opera and change different mask depending on your mood"},
			{"role": "user", "content": message.content}
			]
		)
		await message.channel.send(response.choices[0].message.content)

client.run(DISCORD_TOKEN)