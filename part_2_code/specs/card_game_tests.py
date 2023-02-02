import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Spades",  5)
        self.card2 = Card("Heart", 8)
        self.card3 = Card("Clubs",  2)
        self.cards = [self.card1, self.card2, self.card3]
    
        

    def test_check_for_ace_in_card(self):
        output = CardGame.check_for_ace(self.card1)
        self.assertEqual(False, output)
    
    def test_highest_card(self):
        highest_card = CardGame.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, highest_card)

    def test_cards_total(self):
        total = CardGame.cards_total(self.cards)
        self.assertEqual("You have a total of 15", total)