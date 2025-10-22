import random
import os
import discord
from  dotenv import load_dotenv

quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn't just find you. You have to go out and get it.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
    "Dream bigger. Do bigger.",
    "Don't stop when you're tired. Stop when you're done.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Do something today that your future self will thank you for.",
    "Little things make big days.",
    "It's going to be hard, but hard does not mean impossible.",
    "Don't wait for opportunity. Create it.",
    "Sometimes we're tested not to show our weaknesses, but to discover our strengths.",
    "The key to success is to focus on goals, not obstacles.",
    "Dream it. Believe it. Build it.",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. – Christian D. Larson",
    "Your only limit is your mind.",
    "Push yourself beyond your limits.",
    "Stay positive, work hard, make it happen.",
    "Don't limit your challenges. Challenge your limits.",
    "You are capable of amazing things.",
    "Believe in the power of yet.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "Everything you’ve ever wanted is on the other side of fear. – George Addair",
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
    "Opportunities don't happen. You create them. – Chris Grosser",
    "Don't be afraid to give up the good to go for the great. – John D. Rockefeller",
    "I find that the harder I work, the more luck I seem to have. – Thomas Jefferson",
    "Success is walking from failure to failure with no loss of enthusiasm. – Winston Churchill",
    "The only place where success comes before work is in the dictionary. – Vidal Sassoon",
    "If you are not willing to risk the usual, you will have to settle for the ordinary. – Jim Rohn",
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Don't let yesterday take up too much of today. – Will Rogers",
    "Whether you think you can or you think you can't, you're right. – Henry Ford",
    "Act as if what you do makes a difference. It does. – William James",
    "Success is not how high you have climbed, but how you make a positive difference to the world. – Roy T. Bennett",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. – Zig Ziglar",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn't just find you. You have to go out and get it.",
    ]

#Load token number
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#make a client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#Event: if bot goes online
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# when user interact with bot with !motivate
@client.event
async def on_message(message):

    print(f'Message from {message.author}: {message.content}')
    if message.author == client.user:
        return

    if message.content.startswith('!motivate'):
        response = random.choice(quotes)
        await message.channel.send(response)
        # await message.channel.send('Du kannst es schaffen!')

# starting bot
client.run(TOKEN)