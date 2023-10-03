import random

'''
    Open your command prompt or terminal.

    Navigate to the directory where you saved script.py.

    Run the unit tests by executing the Python script:

    Copy code
    python3
    script.py

    The unit tests will be executed.
'''

# Task 1
def create_shuffled_deck():
    deck = [str(i) for i in range(1, 11)] * 4
    random.shuffle(deck)
    half_size = len(deck) // 2
    player1_draw_pile = deck[:half_size]
    player2_draw_pile = deck[half_size:]
    return player1_draw_pile, player2_draw_pile, [], []

# Task 2
def draw_card(player, player1_draw_pile, player2_draw_pile, player1_discard_pile, player2_discard_pile):
    draw_pile = player1_draw_pile if player == 1 else player2_draw_pile
    discard_pile = player1_discard_pile if player == 1 else player2_discard_pile

    if not draw_pile:
        random.shuffle(discard_pile)
        draw_pile.extend(discard_pile)
        discard_pile.clear()

    card = draw_pile.pop()
    return card

# Task 3
def play_turn(player1_draw_pile, player2_draw_pile, player1_discard_pile, player2_discard_pile):
    player1_card = draw_card(1, player1_draw_pile, player2_draw_pile, player1_discard_pile, player2_discard_pile)
    player2_card = draw_card(2, player1_draw_pile, player2_draw_pile, player1_discard_pile, player2_discard_pile)

    print(f"Player 1 (20 cards): {player1_card}")
    print(f"Player 2 (20 cards): {player2_card}")

    if player1_card > player2_card:
        print("Player 1 wins this round")
        player1_discard_pile.extend([player1_card, player2_card])
    elif player2_card > player1_card:
        print("Player 2 wins this round")
        player2_discard_pile.extend([player1_card, player2_card])
    else:
        print("No winner in this round")

# Task 4
def play_game():
    player1_draw_pile, player2_draw_pile, player1_discard_pile, player2_discard_pile = create_shuffled_deck()

    while True:
        play_turn(player1_draw_pile, player2_draw_pile, player1_discard_pile, player2_discard_pile)
        if not player1_draw_pile and not player1_discard_pile:
            print("Player 2 wins the game!")
            break
        elif not player2_draw_pile and not player2_discard_pile:
            print("Player 1 wins the game!")
            break

# Unit tests
def test_create_shuffled_deck():
    player1_draw_pile, player2_draw_pile, _, _ = create_shuffled_deck()
    assert len(player1_draw_pile) == 20
    assert len(player2_draw_pile) == 20

def test_draw_card():
    player1_draw_pile, player2_draw_pile, player1_discard_pile, player2_discard_pile = create_shuffled_deck()
    card = draw_card(1, player1_draw_pile, player2_draw_pile, player1_discard_pile, player2_discard_pile)
    assert card in player1_draw_pile or card in player1_discard_pile

def test_play_turn():
    player1_draw_pile, player2_draw_pile, player1_discard_pile, player2_discard_pile = create_shuffled_deck()
    play_turn(player1_draw_pile, player2_draw_pile, player1_discard_pile, player2_discard_pile)

def test_play_game():
    play_game()

if __name__ == "__main__":
    test_create_shuffled_deck()
    test_draw_card()
    test_play_turn()
    test_play_game()
