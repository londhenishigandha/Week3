"""Extend the above program to create a Player Object having Deck of Cards,
 and having ability to Sort by Rank and maintain the cards"""


from enum import Enum # enum is module it used to declare the Enum

class Suit(Enum): # Suit is new class and Enum is base class
    Spade = 1
    Heart = 2
    Diamond = 3
    Club = 4

    def __str__(self):
       return self.name # name is keyword it is used to display the name enum members.
class Rank(Enum):
    R1 = 1
    R2 = 2
    R3 = 3
    R4 = 4
    R5 = 5
    R6 = 6
    R7 = 7
    R8 = 8
    R9 = 9
    Ace = 10
    Jack = 11
    Queen = 12
    King = 13

    def __str__(self):
        if self.value <= 10:
            return str(self.value)  # value and name is accessing mode in python
        return self.name

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __str__(self):
        return '{} {}'.format(self.suit, self.number)


cards = [Card (suit,number) for suit in Suit for number in Rank] # list Comprehension method is used

for card in cards:
    print(card)

