from functions import detect_win, to_emoji, print_end

def test_detect_win():
    assert detect_win("Rock","Paper") == "Lose"
    assert detect_win("Paper","Rock") == "Win"

def test_to_emoji():
    assert to_emoji("Rock") == "🪨"
    assert to_emoji("Paper") == "📄"
    assert to_emoji("Scissors") == "✂️"

def test_print_end():
    assert print_end("Win") == "You win! thanks for playing!"
    assert print_end("Lose") == "You lose! thanks for playing!"