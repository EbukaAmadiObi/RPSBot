import random
import discord

def main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith('$startgame'):
            await message.channel.send("What will you choose? (🪨📄✂️)")

        global win_score
        winscore=3
        global bot_score
        bot_score = 0
        global score
        score = 0

        @client.event
        async def on_message(message):
            while True:
                global win_score
                global bot_score
                global score
                if message.author == client.user:
                    return
                throw = message.content.capitalize()
                list = ["Rock", "Paper", "Scissors"]
                if throw not in list:
                    await message.channel.send("Error: Invalid Choice.")
                    continue
                else:
                    bot_throw = random.choice(list)
                    if detect_win(throw,bot_throw) == "Win":
                        score+=1
                        await message.channel.send(f"""
\n🧑{to_emoji(throw)}  vs.{to_emoji(bot_throw)} 🤖\n
🫱     🫲
Win!
"You: {score} Robot: {bot_score}\n""")
                    elif detect_win(throw,bot_throw) == "Lose":
                        bot_score+=1
                        await message.channel.send(f"""
\n🧑{to_emoji(throw)}  vs.{to_emoji(bot_throw)} 🤖\n
🫱     🫲
Lose!
"You: {score} Robot: {bot_score}\n""")
                    else:
                        await message.channel.send(f"""
\n🧑{to_emoji(throw)}  vs.{to_emoji(bot_throw)} 🤖\n
🫱     🫲
Tie!
"You: {score} Robot: {bot_score}\n""")

                    if score == 3:

                        await message.channel.send(print_end("Win"))
                        break
                    elif bot_score == 3:
                        await message.channel.send(print_end("Lose"))
                        break

                    await client.send_message()

    client.run('INSERT KEY HERE')

def detect_win(player, bot):
    match[player, bot]:
        case["Rock", "Paper"]:
            return ("Lose")
        case["Rock", "Scissors"]:
            return ("Win")
        case["Paper", "Rock"]:
            return ("Win")
        case["Paper", "Scissors"]:
            return ("Lose")
        case["Scissors", "Paper"]:
            return ("Win")
        case["Scissors", "Rock"]:
            return ("Lose")
    if (player == bot):
        return "Tie"

def to_emoji(word):
    match word:
        case "Rock":
            return "🪨"
        case "Paper":
            return "📄"
        case "Scissors":
            return "✂️"

def print_end(state):
    if state == "Win":
        return "You win! thanks for playing!"
    elif state == "Lose":
        return "You lose! thanks for playing!"

main()