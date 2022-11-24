# 2. In this exercise you will make an English Deck class made of Card classes the Card class should represent each of the cards
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.

import random

class Card:
    
    def _init_(self, suit, value):
        self.suit = suit
        self.value = value


# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades and values: 
# A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K. 
# It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit and value. 
# When a card is drawn, the card should be removed from the deck.

class Deck:
    
    def _init_(self):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = []
        for i in range(len(suits)):
            for j in range(len(values)):
                self.cards.append(Card(suits[i], values[j]))
        
    def shuffle(self):
        total_cards = len(self.cards)
        for i in range(total_cards):
            j = random.randrange(i, total_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
        
    def draw(self):
        card = self.cards.pop()
        result = card.suit, card.value
        return f'The card drawn is: {result[1]} of {result[0]}.'