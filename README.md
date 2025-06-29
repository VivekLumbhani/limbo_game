# limbo_game
LIMBO: Console-Based Card Game
LIMBO is a fun two-player terminal-based card game that involves strategy, math, and a bit of luck. Players take turns playing cards to reduce a countdown to zero using numerical values and special face card rules. The first player to reach 200 points wins.

Requirements
Python 3.6 or higher

Terminal or command prompt

How to Run
Save the game code into a file, e.g., limbo.py, in my case it's game_logic.py

Open a terminal and navigate to the directory where limbo.py is located.

Run the game using the following command:

bash
Copy
Edit
python limbo.py
Follow on-screen prompts to enter player names and start the game.

Gameplay Instructions
Each round, both players are dealt 5 cards.

Players take turns playing valid cards to reduce the count starting from 101.

Cards have different effects:

Number cards reduce the count.

J (Jack): Applies special effects based on the previous card.

Q (Queen): Reverses the count’s digits if it reduces the number.

K (King): Divides the count by a factor.

A (Ace): Reduces by 11 if possible, otherwise 1.

Players can choose to double or redouble scores at the start of each round.

The round ends when a player can't play or plays the last card.

Function & Class Explanations (2 lines each)
Classes:
Card
Represents a single card with rank and suit; computes its numerical value.

Deck
Creates and manages a shuffled 52-card deck with draw and deal functionalities.

Player
Holds player's name, hand, and score; includes methods to display hand and play cards.

Functions:
reverse_digits(n)
Reverses digits of a number if it has more than one digit, used in Queen and Jack rules.

get_valid_moves(player, count)
Returns list of playable cards based on current count and custom face card rules.

calculate_score(winner, loser, count, starter_count, double_state)
Computes and updates the winner’s and loser’s scores based on remaining count and multipliers.

play_game()
Main game loop that controls the game flow, scoring, and player turns.

Special Commands During Game
Type restart at any turn to restart the game.

Type rules to display game instructions in-game.

Winning the Game
The first player to reach a score of 200 or more wins!

Example Output
PS C:\xampp\htdocs\limbo_game> py .\game_logic.py
Welcome to LIMBO - Console Edition!
Enter Player 1 name: Vivek
Enter Player 2 name: Dummy player

New Round Begins!
Vivek is the dealer.
Vivek, do you want to 'double'? (yes/no): yes
Dummy player, do you want to 'redouble'? (yes/no): yes
Starting card: 3 of Spades, Count: 98

Dummy player's turn (Count: 98)
Dummy player, press Enter to play a card or type 'restart' to restart the game or to know the rules type 'rules': rules
....
Vivek wins the round! Score: +200
Dummy player score this round: +30
Vivek wins the round! Score: +200
Dummy player score this round: +30
Total Scores: Vivek: 200, Dummy player: 30

Dummy player score this round: +30
Total Scores: Vivek: 200, Dummy player: 30
