"""
Cards module

Creates classes Card and Deck to be used to implement many different games.
Cards will be given values and some cards will have special names.
Our Deck class will not include a joker.

"""
from random import shuffle


class Card:
    """
    A representation of a single card in a deck.

    Attributes:
        suit (str): Suit of the card that could be initialized to "Clubs", "Diamonds", "Hearts", and "Spades"
        value (int): Value of the card, can be an integer between 2 and 14 or (2:15), since its inclusive
        name (str): Name of the card, depends on the value
    """
    def __init__(self, value, suit):
        """
        Initializes a card with a value and a suit

        Parameters:
            value (int): Value of the card, can be an integer between 2 and 14 or (2:15), since its inclusive
            suit (str): Suit of the card that could be initialized to "Clubs", "Diamonds", "Hearts", and "Spades"
        """
        self.suit = suit
        self.value = value

        if 2 <= value <= 10:
            self.name = str(value)
        elif value == 11:
            self.name = 'Jack'
        elif value == 12:
            self.name = 'Queen'
        elif value == 13:
            self.name = 'King'
        elif value == 14:
            self.name = 'Ace'
        else:
            raise ValueError('unknown card value error')

    def __str__(self):
        """
        Returns:
            a string representation of the card in the format of <name> of <suit>
        """
        return f"{self.name} of {self.suit}"


class Deck:
    """
    A representation of a deck of cards.

    Attributes:
        cards (list): a list of cards representing a deck, begins with 52 card objects.
    """
    def __init__(self):
        """
        Initializes a deck with 52 cards
        """
        self.cards = []
        for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
            for value in range(2, 15):
                card = Card(value, suit)
                self.cards.append(card)
        shuffle(self.cards)

    def draw(self):
        """
        Draws a card from the deck

        Returns:
            a card from a deck and raises an error if the deck is empty or 0
        """
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            raise RuntimeError('empty deck error')
