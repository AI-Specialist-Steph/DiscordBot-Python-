import discord
import os
from dotenv import load_dotenv
import requests
import json
import random
import csv
from nltk import WordNetLemmatizer



client = discord.Client()

#chatbot is case sensitive, if not capital letters try small letters
chats = ["hello", "hi", "greetings", "what's up", "how's it going", "Hey", "hey"]

starter_chats = [
 "Hello!",
 "Hey",
 "What can I do for you?"
]

goodbye_chats = ["see ya", "bye", "goodbye", "talk to you later", "that's all"]

starter_goodbye_chats = [
    "Sad to see you go:(",
    "Goodbye",
    "Have a lovely day",
    "Till later"
]

complimentary_chats = ["how are you?", "How are you?", "how are you", "How are you"]

starter_complimentary_chats = [
    "splendid"
]
convo_chats = ["I'm bored", "Could you please recommend a movie", "Give me a list of top rated movies","could you please recommend a movie",
               "I would like to watch a movie", "recommend movies", "Recommend movies", "I am bored", "Can you recommend a movie for me", "give me a list of top rated movies/series"]

starter_convo_chats = [
    "Sure!, what is your current mood?"

]

mood_chats = ["sad", "moody", "frisky", "calm", "irritated", "anxious", "apathetic", "depressed", "frustrated"]
starter_mood_chats = [
    "UH OH:(!, please input #movies to get movie recommendations"
]

happy_chats = ["happy", "excited", "ecstatic", "content", "cheerful", "jolly", "ecstatic"]
starter_happy_chats = [
    "Same!;), please input #movies to make you even $HAPPIER$"
]

yourself = ["introduce yourself", "Introduce yourself", "what can you do?", "What can you do?", "what do you do?", "What do you do?", "are you human?", "Are you human?", "who are you?"]
starter_yourself = [
    "h-e-l-l-o, fellow human user!, you can call me edin50, I'm a movies4U bot and I'm here to recommend movies4U;) "
    "and movie theatres or cinemas for U "
]
coventry_theatres = ["I want to watch a movie in Coventry", "I'd like to see a movie in cov", "I would like to watch "
                                                                                              "a movie in Coventry",
                     "recommend movie theatres", "recommend cinemas"]
starter_coventry_theatres = [
    "Yessir!, please tap the link and choose a movie cinema that is closest or more appropriate for you-- https://www.google.com/search?q=cinemas+in+coventry&oq=cinemas+&aqs=chrome.1.69i57j35i39l2j0i433i457i512j0i402j0i512l5.5857j1j4&sourceid=chrome&ie=UTF-8 "
]
comp = ["thanks", "Thanks", "thank you"]
starter_comp = [
    "My pleasure!, do you want to watch a movie in the cinema?"
]
negative = ["no", "nah", "nope", "never", "of course not", "No", "Nah", "Nope", "Never"]
starter_negative = [
    "Okay BYE!, thanks for using movies4U"
]
positive = ["yes", "Yes", "Yup", "yup", "yasss", "yeah", "Yeah", "sure", "great", "of course", "yes please", "yes thanks"]
starter_positive = [
    "COOL:) tap the link and choose a movie cinema that is closest or more appropriate for you-- https://www.google.com/search?q=cinemas+in+coventry&oq=cinemas+&aqs=chrome.1.69i57j35i39l2j0i433i457i512j0i402j0i512l5.5857j1j4&sourceid=chrome&ie=UTF-8 "
]
lemmatizer = WordNetLemmatizer


def get_movies():
    response = requests.get("https://api.themoviedb.org/3/movie/550?api_key=3daa7452013acd7319afd0bf69020a7c")
    json_data = json.loads(response.text)
    movies = json_data
    return (movies)


@client.event
async def on_ready():
    print('movie4U logged in as {0.user} '.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('#movies'):
        movies = get_movies()
        await message.channel.send(movies)


    if any(word in message.content for word in chats):
        await message.channel.send(random.choice(starter_chats))

    if any(word in message.content for word in goodbye_chats):
        await message.channel.send(random.choice(starter_goodbye_chats))

    if any(word in message.content for word in complimentary_chats):
        await message.channel.send(random.choice(starter_complimentary_chats))

    if any(word in message.content for word in convo_chats):
        await message.channel.send(random.choice(starter_convo_chats))

    if any(word in message.content for word in mood_chats):
        await message.channel.send(random.choice(starter_mood_chats))

    if any(word in message.content for word in happy_chats):
        await message.channel.send(random.choice(starter_happy_chats))

    if any(word in message.content for word in coventry_theatres):
        await message.channel.send(random.choice(starter_coventry_theatres))

    if any(word in message.content for word in yourself):
        await message.channel.send(random.choice(starter_yourself))

    if any(word in message.content for word in comp):
        await message.channel.send(random.choice(starter_comp))

    if any(word in message.content for word in positive):
        await message.channel.send(random.choice(starter_positive))

    if any(word in message.content for word in negative):
        await message.channel.send(random.choice(starter_negative))

    if message.content == '$private':
        await message.author.send("Private chat or nothing")


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client.run(TOKEN)



