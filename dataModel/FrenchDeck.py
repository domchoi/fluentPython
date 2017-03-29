'''
Created on Mar 12, 2017

@author: J001684

Objectives:
    Demonstrate special functions:
        __len__
        __getitem__
        
    By implementing these 2 functions, function len, [] array operator,
    random.choice, slicing, iterable, reverse
'''
from collections import namedtuple
from random import choice

Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    '''
    classdocs
    '''
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        '''
        Constructor
        '''
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
        
     
    
'''
Examples
'''
beer_card = Card('7', 'diamonds')
print('beer_card:')
print(beer_card)
deck = FrenchDeck()
print('len function of deck returns ', len(deck))
print('deck[0]:')
print(deck[0])
print('deck[-1]:')
print(deck[-1])
print('choice(deck):')
print(choice(deck))
print('choice(deck):')
print(choice(deck))
print('choice(deck):')
print(choice(deck))
# Because of __getitem__ we can slice, iterate
print('deck[:13]:')
print(deck[:13])
print('deck[12::13]:')
print(deck[12::13])
print('iteration:')
for card in deck:
    print(card)
for card in reversed(deck):
    print(card)
print('sorted cards:')
def ranking(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    return rank_value + suit_values[card.suit] * len(FrenchDeck.ranks)
for card in sorted(deck, key=ranking):
    print(card)
