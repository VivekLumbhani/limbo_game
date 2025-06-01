# LIMBO: Console-based game for two players in Python

import random
import sys

# Constants
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
TARGET_SCORE = 200

# Card values
CARD_VALUES = {str(i): i for i in range(2, 11)}
CARD_VALUES.update({'J': 0, 'Q': 0, 'K': 0, 'A': 1})

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def value(self):
        return CARD_VALUES[self.rank]

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)

    def deal(self, num):
        return [self.cards.pop() for _ in range(num)]

    def draw(self):
        return self.cards.pop() if self.cards else None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def show_hand(self):
        for i, card in enumerate(self.hand):
            print(f"{i + 1}. {card}")

    def play_card(self, index):
        return self.hand.pop(index)

def reverse_digits(n):
    return int(str(n)[::-1]) if n > 9 else n

def get_valid_moves(player, count):
    valid_moves = []
    for i, card in enumerate(player.hand):
        if card.rank in 'JQK':
            if card.rank == 'Q':
                reversed_val = reverse_digits(count)
                if reversed_val < count:
                    valid_moves.append((i, card))
            elif card.rank == 'K':
                for d in range(2, count):
                    if count % d == 0:
                        valid_moves.append((i, card))
                        break
            else:
                valid_moves.append((i, card))
        else:
            val = card.value()
            if val == 0:
                continue
            if count % val == 0:
                valid_moves.append((i, card))
            elif count - val >= 0:
                valid_moves.append((i, card))
    return valid_moves

def calculate_score(winner, loser, count, starter_count, double_state):
    winner_score = 10 * starter_count
    loser_score = 10 * count
    if double_state == 2:
        winner_score *= 2
    elif double_state == 4:
        winner_score *= 4
    winner.score += winner_score
    loser.score += loser_score
    return winner_score, loser_score

def play_game():
    print("Welcome to LIMBO - Console Edition!")
    p1 = Player(input("Enter Player 1 name: "))
    p2 = Player(input("Enter Player 2 name: "))
    players = [p1, p2]
    turn = 0

    while p1.score < TARGET_SCORE and p2.score < TARGET_SCORE:
        deck = Deck()
        for player in players:
            player.hand = deck.deal(5)

        print("\nNew Round Begins!")
        print(f"{players[turn].name} is the dealer.")

        # Doubling logic
        double_state = 1
        response = input(f"{players[turn].name}, do you want to 'double'? (yes/no): ").lower()
        if response == 'yes':
            double_state = 2
            response = input(f"{players[1 - turn].name}, do you want to 'redouble'? (yes/no): ").lower()
        else :
            response = input(f"{players[1 - turn].name}, do you want to 'double'? (yes/no): ").lower()

        if response == 'yes':
            double_state = 4

        flag=True
        move_history = []  # Initialize move history list
        current_player = None  # Or 0, 1 — based on your logic


        while True:
            if flag:
                    
                starter_card = deck.draw()
                starter_val = starter_card.value() if starter_card.rank not in 'JQKA' else 0
                count = 101 - starter_val
                print(f"Starting card: {starter_card}, Count: {count}")
                move_history = [(starter_card, count)]
                current_player = 1 - turn
                flag=False



            player = players[current_player]
            print(f"\n{player.name}'s turn (Count: {count})")
            # player.show_hand()


            valid_moves = get_valid_moves(player, count)
            if not valid_moves:
                print(f"{player.name} has no valid moves. Game Over.")
                winner = players[1 - current_player]
                loser = player
                break
            while True:
                
                user_input = input(f"{player.name}, press Enter to play a card or type 'restart' to restart the game or to know the rules type 'rules': ").lower()
                print(f"\nCurrent Scores: {players[0].name}: {players[0].score}, {players[1].name}: {players[1].score}")

                if user_input == 'restart':
                    print("\nRestarting the game...\n")
                    return play_game()  # Restart the game
                elif user_input == 'rules':
                    print("\nRules of the game:\n")
                    print("- Each player plays one card per turn.")
                    print("- Cards reduce the total count based on their value.")
                    print("- Face cards (Jack, Queen, King) have special rules.")
                    print("- Game ends when count reaches zero or below.\n")
                    continue  
                else:

                    break  



            choice, card = random.choice(valid_moves)
            print(f"{player.name} played: {card}")




            card = player.play_card(choice)
            prev_card = move_history[-1][0]

            if card.rank == 'A':
                count -= 11 if count >= 11 else 1
            elif card.rank == 'J':
                if prev_card.rank == 'K':
                    count //= 2
                elif prev_card.rank == 'Q':
                    count = reverse_digits(count)
                else:
                    if prev_card.rank in 'JQK':
                        count = count
                    else:
                        prev_val = prev_card.value()
                        if count % prev_val == 0:
                            count //= prev_val
                        else:
                            count -= prev_val
            elif card.rank == 'Q':
                count = reverse_digits(count)
            elif card.rank == 'K':
                for d in range(2, count):
                    if count % d == 0:
                        count //= d
                        break
            else:
                val = card.value()
                if count % val == 0:
                    count //= val
                else:
                    count -= val

            move_history.append((card, count))
            if count <= 0 or len(player.hand) == 0:
                print(f"{player.name} played the last card: {card}, Count: {count}")
                winner = player
                loser = players[1 - current_player]
                break

            current_player = 1 - current_player

        win_points, lose_points = calculate_score(winner, loser, count, len(move_history), double_state)
        print(f"\n{winner.name} wins the round! Score: +{win_points}")
        print(f"{loser.name} score this round: +{lose_points}")
        print(f"Total Scores: {p1.name}: {p1.score}, {p2.name}: {p2.score}")

        turn = 1 - turn

    print(f"\nGame Over! Winner: {p1.name if p1.score >= TARGET_SCORE else p2.name}")

if __name__ == '__main__':
    play_game()
