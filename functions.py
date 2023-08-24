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