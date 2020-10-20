# Name: Joseph Liu
# Email: kelpabc123@gmail.com
# Filename: coursebot.py
# File: Discord bot outputting course information

import discord
from course import MyCourse
import copy
import cscraper


client = discord.Client()

# Constant value
TOKEN = "Insert token here"
BOT_PREFIX = "!"
COURSE_PATH = "data/courses.csv"
CSV_ERROR = "Failed to populate .csv"
FIND_COURSE_USAGE="Usage example (title): !findCourse flag 'keyword'"
FIND_COURSE_DESC="""Searches the UCSD course catalog and returns all matching courses,
 with the first argument being the flag to determine what to search by 
 (title/course code/description), which are t/n/d respectively, and the second argument being
 the search term."""
FIND_COURSE_WRONG_ARGS="""Incorrect number/format of arguments entered. Pleace enter t, n or d as the
 first argument to search by title, course ID (Like COGS 108) or description respectively, 
 followed by the search term"""

#initialization

bot = commands.Bot(command_prefix=BOT_PREFIX)
resultMap = dict()

#Event implementations
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

#To find courses
@bot.command(name="findCourse",
            description=FIND_COURSE_DESC,
            brief=FIND_COURSE_USAGE)
async def findCourse(ctx,args):
    if(len(args)<=1):
        ctx.send(FIND_COURSE_WRONG_ARGS)
        return
    key = copy.deepcopy(args)
    " ".join(key)
    flag = args[0]
    args = args[1:]
    " ".join(args)
    queryList = []
    if(flag.startswith('t')):
        queryList = cscraper.findCoursebyTitle(args)
    elif (flag.startswith('n')):
        queryList = cscraper.findCourseByID(args)
    elif (flag.startswith('d')):
        queryList = cscraper.findCoursebyDesc(args)
    else:
        ctx.send(FIND_COURSE_WRONG_ARGS)
        return
        



# Page wrapper

# Updates
@bot.command(name="refreshMaster",
            description="Queries the UCSD course page and gets an updated list of courses",
            brief="!refreshMaster")
async def refreshMaster(ctx,args):
    cscraper.updateCSV()

# Startup
client.run(token)