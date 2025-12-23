from discord.ext import commands
from discord import app_commands
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import discord
import ssl
import os
from tabulate import tabulate


#       .o8                            .o8            oooo
#      "888                           "888            `888
#  .oooo888   .oooo.    .ooooo.   .oooo888   .oooo.    888  oooo  oooo   .oooo.o
# d88' `888  `P  )88b  d88' `88b d88' `888  `P  )88b   888  `888  `888  d88(  "8
# 888   888   .oP"888  888ooo888 888   888   .oP"888   888   888   888  `"Y88b.
# 888   888  d8(  888  888    .o 888   888  d8(  888   888   888   888  o.  )88b
# `Y8bod88P" `Y888""8o `Y8bod8P' `Y8bod88P" `Y888""8o o888o  `V88V"V8P' 8""888P'


# SPECIFY REMOTE HERE AND YOUR BOT Token HERE
remote = ''
bot_id = ''
empty_space = "	 󠁡 󠁡 󠁡 󠁡  󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡  	 󠁡 󠁡 󠁡 󠁡  󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡  	 󠁡 󠁡 󠁡 󠁡  󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡  	 󠁡 󠁡 󠁡 󠁡  󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡  󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡  󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡  󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡  󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡  󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡  󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡  󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 󠁡 "

# Setup bot with intents for Discord API v2+
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='d ', intents=intents)


def get_time():
	time = 'Score Reported at: {}'.format(datetime.now())
	return time


@client.event
async def on_ready():
	print('Daedalus is ready!')
	try:
		synced = await client.tree.sync()
		print(f"Synced {len(synced)} command(s)")
	except Exception as e:
		print(f"Failed to sync commands: {e}")


# Slash commands using app_commands
@client.tree.command(name="ping", description="Test the bot's responsiveness")
async def slash_ping(interaction: discord.Interaction):
	await interaction.response.send_message('Pong!')


@client.tree.command(name="server", description="Display the server location")
async def slash_server(interaction: discord.Interaction):
	message = 'Server is located at: {}'.format(remote)
	await interaction.response.send_message(message)


@client.tree.command(name="daedalus", description="Display ASCII art logo")
async def slash_daedalus(interaction: discord.Interaction):
	logo = '''```css

	.o8                            .o8            oooo
	"888                           "888            `888
.oooo888   .oooo.    .ooooo.   .oooo888   .oooo.    888  oooo  oooo   .oooo.o
d88' `888  `P  )88b  d88' `88b d88' `888  `P  )88b   888  `888  `888  d88(  "8
888   888   .oP"888  888ooo888 888   888   .oP"888   888   888   888  `"Y88b.
888   888  d8(  888  888    .o 888   888  d8(  888   888   888   888  o.  )88b
`Y8bod88P" `Y888""8o `Y8bod8P' `Y8bod88P" `Y888""8o o888o  `V88V"V8P' 8""888P'

```'''
	await interaction.response.send_message(logo)


@client.tree.command(name="help", description="Display all available commands")
async def slash_man(interaction: discord.Interaction):
	embed = discord.Embed(color=0x6393f)

	embed.title = 'Commands:'
	embed.add_field(name='`/ping`', value='Pong!', inline=True)
	embed.add_field(name='`/daedalus`', value='Display ASCII art', inline=True)
	embed.add_field(
		name='`/help`', value='Will display all commands and their uses', inline=False)
	embed.add_field(
		name='`/server`', value='Will display the server the bot is currently pulling scores from', inline=False)

	embed.add_field(
		name='`/top`', value='Will fetch the top 10 scores', inline=False)
	embed.add_field(name='`/team <team_name>`',
					value='Will fetch score details for the team specified', inline=False)
	embed.add_field(
		name='`/export`', value='Will fetch a file containing current scores', inline=False)
	embed.add_field(name='`/scoreboard <number>`',
					value='Will fetch the top <number> scores. If the message is too large to be sent on Discord, it will be sent as a text file', inline=False)
	embed.add_field(name='`/image <image_name> <number>`',
					value='Will fetch the top <number> scores for the image specified. If the message is too large to be sent on discord it will be sent as a text file', inline=False)
	embed.add_field(name='`/rank <image_name> <team_id>`',
					value='Will return the rank of the given ID for the given image if it exists', inline=False)
	await interaction.response.send_message(embed=embed)


@client.tree.command(name="top", description="Fetch the top 10 scores")
async def slash_top(interaction: discord.Interaction):
	await interaction.response.defer()
	
	data = requests.get(remote)
	content = data.content
	soup = BeautifulSoup(content, 'html.parser')

	scores = soup.find_all('tr')
	top_comp = [[" ════ ", " ", " ════ ", " ", " ════ ", " ", " ════ "]]
	header =   ['Rank',' ', 'Team', ' ', 'Time', ' ', 'Score']
	for team in scores[0:10]:
		team = team.find_all('a')
		team_info = [team[0].contents[0], team[1].contents[0],
					team[2].contents[0], team[3].contents[0], team[4].contents[0]]
		team_info_fixed = []
		for element in team_info:
			team_info_fixed.append(element.strip())
		top_comp.append([team_info_fixed[0], " ", team_info_fixed[1], " ", team_info_fixed[3], " ", team_info_fixed[4]])

	formatted = "```" + tabulate(top_comp, header, stralign="left", numalign="left", tablefmt="plain") + "```"

	h_find = soup.find_all('h4')
	round_title = h_find[0].text

	embed = discord.Embed(color=0x36393f)
	embed.title = round_title
	embed.set_footer(text=empty_space + "\n" + get_time() + "\n" + empty_space)
	embed.add_field(name="\u200b", value=formatted, inline=False)

	await interaction.followup.send(embed=embed)


@client.tree.command(name="scoreboard", description="Fetch the top N scores")
async def slash_scoreboard(interaction: discord.Interaction, num: int = 10):
	await interaction.response.defer()
	
	data = requests.get(remote)
	content = data.content
	soup = BeautifulSoup(content, 'html.parser')

	h_find = soup.find_all('h4')
	round_title = h_find[0].text

	scores = soup.find_all('tr')
	top_comp = [[" ════ ", " ", " ════ ", " ", " ════ ", " ", " ════ "]]
	header =   ['Rank',' ', 'Team', ' ', 'Time', ' ', 'Score']
	for team in scores[0:num]:
		team = team.find_all('a')
		team_info = [team[0].contents[0], team[1].contents[0],
					team[2].contents[0], team[3].contents[0], team[4].contents[0]]
		team_info_fixed = []
		for element in team_info:
			team_info_fixed.append(element.strip())
		top_comp.append([team_info_fixed[0], " ", team_info_fixed[1], " ", team_info_fixed[3], " ", team_info_fixed[4]])

	formatted = "```" + tabulate(top_comp, header, stralign="left", numalign="left", tablefmt="plain") + "```"

	embed = discord.Embed(color=0x36393f)
	embed.title = round_title
	embed.set_footer(text=empty_space + "\n" + get_time() + "\n" + empty_space)
	embed.add_field(name="\u200b", value=formatted, inline=False)

	try:
		await interaction.followup.send(embed=embed)
	except:
		fle = open('scoreboard.txt', 'w+')
		formatted_split = formatted.split('```')
		fle.write(formatted_split[1])
		fle.close()
		await interaction.followup.send(file=discord.File('scoreboard.txt'))


@client.tree.command(name="team", description="Fetch score details for a specific team")
async def slash_team(interaction: discord.Interaction, team_name: str):
	await interaction.response.defer()
	
	global remote
	url = '{}/team/{}'.format(remote, str(team_name))
	team_data = requests.get(url)
	content = team_data.content
	soup = BeautifulSoup(content, 'html.parser')
	scores = soup.find_all(
		'table', {"class": "table table-borderless table-dark table-striped"})
	image_tags = soup.find('tbody')
	tds = []

	image_scores_bad = image_tags[1]
	try_to_fix_image_scores = image_scores_bad.find_all('td')
	for score in try_to_fix_image_scores.find_all('a'):
		print(score)

	for thing in scores:
		tds.append(thing.find_all('tr'))

	general_tags = tds[0]
	temp = []

	for gentag in general_tags:
		gentemp = gentag.find_all('td')

	for j, gentag in enumerate(gentemp):
		gentemp[j] = '`{}`'.format(gentag.text)

	for tag in image_tags:
		temp.append(tag.find_all('td'))

	for list in temp:
		for i, tag in enumerate(list):
			list[i] = tag.text

	report = []

	for list in temp:
		message = '''Image: {} 	Time: {} Score: ({}/{}) {}'''.format(
			list[0], list[1], list[2], list[3], list[4])
		report.append(message)

	formatted = '\n'
	formatted = formatted.join(report)
	formatted = '```' + formatted + '```'

	title = 'Scores for {}:'.format(team_name)

	embed = discord.Embed(color=0x36393f)
	embed.title = title
	embed.add_field(name="Elapsed Time", value=gentemp[0], inline=False)
	embed.add_field(name="Play Time", value=gentemp[1], inline=False)
	embed.add_field(name="Total Score", value=gentemp[2], inline=False)
	embed.add_field(name="Current Image Scores", value=formatted, inline=False)
	embed.add_field(name="Time", value=get_time(), inline=False)
	embed.add_field(name="Link", value=url, inline=False)

	await interaction.followup.send(embed=embed)


@client.tree.command(name="export", description="Export current scores to a file")
async def slash_export(interaction: discord.Interaction):
	await interaction.response.defer()
	
	data = requests.get(remote)
	content = data.content
	soup = BeautifulSoup(content, 'html.parser')

	h_find = soup.find_all('h4')
	round_title = h_find[0].text

	scores = soup.find_all('tr')
	top_comp = []
	header =   ['Rank','Team','Images','Time','Score']
	for team in scores:
		team = team.find_all('a')
		team_info = [team[0].contents[0], team[1].contents[0],
					team[2].contents[0], team[3].contents[0], team[4].contents[0]]
		team_info_fixed = []
		for element in team_info:
			team_info_fixed.append(element.strip())
		top_comp.append(team_info_fixed)

	table = tabulate(top_comp, header)

	top_title = '''{} | Report Generated on {} | Server at {}'''.format(
		round_title, get_time(), remote)

	fle = open('scoreboard.txt', 'w+')
	fle.write(top_title + '\n')
	fle.write(table)
	fle.close()
	await interaction.followup.send(file=discord.File('scoreboard.txt'))


@client.tree.command(name="image", description="Fetch top N scores for a specific image")
async def slash_image(interaction: discord.Interaction, name: str, num: int = 10):
	await interaction.response.defer()
	
	url = '{}/image/{}'.format(remote, str(name))
	team_image_data = requests.get(url)
	content = team_image_data.content
	soup = BeautifulSoup(content, 'html.parser')

	h_find = soup.find_all('h4')
	round_title = h_find[0].text

	scores = soup.find_all('tr')
	comp = []
	header =   ['Rank','Team','Time','Score']
	for team in scores[0:num]:
		team = team.find_all('a')
		team_info = [team[0].contents[0],
					team[1].contents[0], team[2].contents[0], team[3].contents[0]]
		team_info_fixed = []
		for element in team_info:
			team_info_fixed.append(element.strip())

		comp.append(team_info_fixed)

	formatted = "```" + tabulate(comp, header) + "```"

	embed = discord.Embed(color=0x36393f)
	embed.title = round_title
	embed.add_field(name="Time", value=get_time(), inline=False)
	embed.description = formatted

	try:
		await interaction.followup.send(embed=embed)
	except:
		fle = open('scoreboard.txt', 'w+')
		formatted_split = formatted.split('```')
		fle.write(formatted_split[1] if len(formatted_split) > 1 else formatted)
		fle.close()
		await interaction.followup.send(file=discord.File('scoreboard.txt'))

@client.tree.command(name="rank", description="Get the rank of a team ID for a specific image")
async def slash_rank(interaction: discord.Interaction, image: str, team_id: str):
	await interaction.response.defer()
	
	url = '{}image/{}'.format(remote, str(image))
	team_image_data = requests.get(url)
	content = team_image_data.content
	soup = BeautifulSoup(content, 'html.parser')

	scores = soup.find_all('tr')

	rank = -1

	for score in scores:
		if str(score.find_all('a')[1].text).strip() == str(team_id).strip():
			rank = int(score.find_all('a')[0].text)
			break

	if rank == -1:
		embed = discord.Embed(color=0x36393f)
		embed.title ="ID not found for this image"
		await interaction.followup.send(embed=embed)
	else:
		embed = discord.Embed(color=0x36393f)
		embed.title = str(team_id) + "'s rank is " + str(rank)
		await interaction.followup.send(embed=embed)


client.run(bot_id)
