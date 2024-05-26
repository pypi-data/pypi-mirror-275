
# Poker Bot

## Overview
Poker Bot is a Python package designed for calculating poker hand equities and managing a poker game. This package includes functionalities for deck management, hand evaluation, equity calculation, and game management.

## Features
- **Deck Management**: Initialize, shuffle, draw, and reset a deck of cards.
- **Hand Evaluation**: Evaluate poker hands to determine their ranks.
- **Equity Calculation**: Calculate the probability of winning, losing, and tying for two-player No-Limit Hold'em.
- **Game Management**: Manage player buy-ins, rebuys, and cashouts in a poker game.

## Installation
To install the package, use:
\`\`\`sh
pip install pokerFunctions
\`\`\`

## Usage

### Deck Management
\`\`\`python
from pokerFunctions.equity import Deck

# Initialize a new deck
deck = Deck()

# Shuffle the deck
deck.shuffle()

# Draw cards
cards = deck.draw(5)
print(cards)

# Reset the deck
deck.reset()
\`\`\`

### Hand Evaluation
\`\`\`python
from pokerFunctions.equity import evaluate

hand = ['6s', '7s', '8s', '9s', 'ts']  # Straight flush
rank = evaluate(hand, Deck())
print(rank)  # Output: [9, 10]
\`\`\`

### Equity Calculation
\`\`\`python
from pokerFunctions.equity import equity

hero = ['as', 'ks']
villain = ['qd', 'qh']
board = ['2s', '3s', '4s']
result = equity(hero, villain, board, runs=1000)
print(result)  # Output: [win_percentage_hero, win_percentage_villain, tie_percentage]
\`\`\`

### Game Management
\`\`\`python
from pokerFunctions.gamebank import Game

# Initialize a new game
game = Game('host_name')

# Add players
game.add_player('player1', 100)
game.add_player('player2', 150)

# Player rebuys
game.rebuy('player1', 50)

# Remove a player (cash out)
game.remove_player('player2', 100)

# Get game status
print(game.gamestatus())
\`\`\`

## Development
To contribute to the development of Poker Bot, clone the repository and run the following commands to install the dependencies and run tests:
\`\`\`sh
git clone https://github.com/yourusername/pokerFunctions.git
cd pokerFunctions
pip install -r requirements.txt
python -m unittest discover
\`\`\`

## License
This project is licensed under the MIT License.

## Contact
For more information or support, contact [Jonah Aden](mailto:me@jonahaden.org).

---

*Note: This is a basic README template. Customize it according to your project's specifics and requirements.*
