import json
from unittest import TestCase

from whist.core.cards.card import Card, Suit, Rank
from whist.core.cards.card_container import OrderedCardContainer, UnorderedCardContainer


class OrderedCardContainerTestCase(TestCase):
    def setUp(self) -> None:
        self.spades_king = Card(suit=Suit.SPADES, rank=Rank.K)
        self.king_hearts = Card(suit=Suit.HEARTS, rank=Rank.K)
        self.ace_hearts = Card(suit=Suit.HEARTS, rank=Rank.A)
        self.seven_clubs = Card(suit=Suit.CLUBS, rank=Rank.NUM_7)
        self.ten_diamonds = Card(suit=Suit.DIAMONDS, rank=Rank.NUM_10)
        self.cc4 = OrderedCardContainer.with_cards(self.king_hearts, self.ace_hearts, self.seven_clubs, self.ten_diamonds)

    def test_not_equal(self):
        first = OrderedCardContainer.with_cards(Card(suit=Suit.HEARTS, rank=Rank.NUM_2), Card(suit=Suit.HEARTS, rank=Rank.NUM_4))
        second = OrderedCardContainer.with_cards(Card(suit=Suit.HEARTS, rank=Rank.NUM_4), Card(suit=Suit.HEARTS, rank=Rank.NUM_2))
        self.assertNotEqual(first, second)

    def test_empty_manual(self):
        cc = OrderedCardContainer(cards=())
        self.assertEqual(0, len(cc))

    def test_empty(self):
        cc = OrderedCardContainer.empty()
        self.assertEqual(0, len(cc))

    def test_full(self):
        cc = OrderedCardContainer.full()
        self.assertEqual(52, len(cc))

    def test_pop_random(self):
        full_cc = OrderedCardContainer.full()
        popped_card = full_cc.pop_random()
        self.assertIsInstance(popped_card, Card)
        self.assertNotIn(popped_card, full_cc)

    def test_json_empty(self):
        cc = OrderedCardContainer.empty()
        self.assertEqual({'cards': []}, json.loads(cc.json()))

    def test_json_empty_load(self):
        cc = OrderedCardContainer.empty()
        self.assertEqual(cc, OrderedCardContainer(**json.loads(cc.json())))

    def test_json_some_cards(self):
        cc = OrderedCardContainer.with_cards(
            Card(suit=Suit.HEARTS, rank=Rank.NUM_2),
            Card(suit=Suit.HEARTS, rank=Rank.NUM_4)
        )
        self.assertEqual({'cards': [
            {'suit': 'hearts', 'rank': '2'},
            {'suit': 'hearts', 'rank': '4'}
        ]}, json.loads(cc.json()))

    def test_json_some_cards_load(self):
        cc = OrderedCardContainer.with_cards(
            Card(suit=Suit.HEARTS, rank=Rank.NUM_2),
            Card(suit=Suit.HEARTS, rank=Rank.NUM_4)
        )
        self.assertEqual(cc, OrderedCardContainer(**json.loads(cc.json())))

    def test_json_full_load(self):
        cc = OrderedCardContainer.full()
        self.assertEqual(cc, OrderedCardContainer(**json.loads(cc.json())))

    def test_contains(self):
        cc = OrderedCardContainer.with_cards(self.spades_king)
        self.assertEqual(1, len(cc))
        self.assertIn(self.spades_king, cc)

    def test_add(self):
        cc = OrderedCardContainer.empty()
        cc.add(self.spades_king)
        self.assertEqual(1, len(cc))
        self.assertIn(self.spades_king, cc)

    def test_add_duplicate(self):
        cc = OrderedCardContainer.empty()
        cc.add(self.spades_king)
        with self.assertRaises(ValueError):
            cc.add(self.spades_king)

    def test_add_none(self):
        cc = OrderedCardContainer.empty()
        with self.assertRaises(ValueError):
            cc.add(None)

    def test_add_wrong_type(self):
        cc = OrderedCardContainer.empty()
        with self.assertRaises(ValueError):
            cc.add('ace of spades')

    def test_remove(self):
        cc = OrderedCardContainer.full()
        cc.remove(self.spades_king)
        self.assertNotIn(self.spades_king, cc)

    def test_remove_no_contain(self):
        cc = OrderedCardContainer.empty()
        with self.assertRaises(ValueError):
            cc.remove(self.spades_king)

    def test_remove_none(self):
        cc = OrderedCardContainer.full()
        with self.assertRaises(ValueError):
            cc.remove(None)

    def test_remove_wrong_type(self):
        cc = OrderedCardContainer.full()
        with self.assertRaises(ValueError):
            cc.remove('ace of spades')

    def test_iter(self):
        queen_diamonds = Card(suit=Suit.DIAMONDS, rank=Rank.Q)
        cards = {self.spades_king, queen_diamonds}
        cc = OrderedCardContainer.with_cards(cards)
        self.assertEqual(cards, {card for card in cc})

    def test_contains_suit(self):
        cc = OrderedCardContainer.with_cards(self.spades_king)
        self.assertTrue(cc.contains_suit(Suit.SPADES))

    def test_not_contains_suit(self):
        cc = OrderedCardContainer.with_cards(self.spades_king)
        self.assertFalse(cc.contains_suit(Suit.HEARTS))
        self.assertFalse(cc.contains_suit(Suit.CLUBS))
        self.assertFalse(cc.contains_suit(Suit.DIAMONDS))

    def test_first(self):
        self.assertEqual(self.king_hearts, self.cc4.first)

    def test_first_empty(self):
        cc = OrderedCardContainer.empty()
        self.assertIsNone(cc.first)

    def test_last(self):
        self.assertEqual(self.ten_diamonds, self.cc4.last)

    def test_last_empty(self):
        cc = OrderedCardContainer.empty()
        self.assertIsNone(cc.last)

    def test_get_turn(self):
        self.assertEqual(0, self.cc4.get_turn(self.king_hearts))
        self.assertEqual(1, self.cc4.get_turn(self.ace_hearts))
        self.assertEqual(2, self.cc4.get_turn(self.seven_clubs))
        self.assertEqual(3, self.cc4.get_turn(self.ten_diamonds))

    def test_get_turn_exception(self):
        with self.assertRaises(ValueError):
            self.cc4.get_turn(self.spades_king)

    def test_winner_card_suit(self):
        self.assertEqual((1, self.ace_hearts), self.cc4.get_turn_and_winner_card(Suit.SPADES))

    def test_winner_card_trump(self):
        self.assertEqual((2, self.seven_clubs), self.cc4.get_turn_and_winner_card(Suit.CLUBS))


class UnorderedCardContainerTestCase(TestCase):
    def setUp(self) -> None:
        self.spades_king = Card(suit=Suit.SPADES, rank=Rank.K)

    def test_equal(self):
        first = UnorderedCardContainer.with_cards(Card(suit=Suit.HEARTS, rank=Rank.NUM_2), Card(suit=Suit.HEARTS, rank=Rank.NUM_4))
        second = UnorderedCardContainer.with_cards(Card(suit=Suit.HEARTS, rank=Rank.NUM_4), Card(suit=Suit.HEARTS, rank=Rank.NUM_2))
        self.assertEqual(first, second)

    def test_not_equal(self):
        first = UnorderedCardContainer.with_cards(Card(suit=Suit.HEARTS, rank=Rank.NUM_2))
        second = UnorderedCardContainer.with_cards(Card(suit=Suit.HEARTS, rank=Rank.NUM_4))
        self.assertNotEqual(first, second)

    def test_empty_manual(self):
        cc = UnorderedCardContainer(cards=())
        self.assertEqual(0, len(cc))

    def test_empty(self):
        cc = UnorderedCardContainer.empty()
        self.assertEqual(0, len(cc))

    def test_full(self):
        cc = UnorderedCardContainer.full()
        self.assertEqual(52, len(cc))

    def test_pop_random(self):
        full_cc = UnorderedCardContainer.full()
        popped_card = full_cc.pop_random()
        self.assertIsInstance(popped_card, Card)
        self.assertNotIn(popped_card, full_cc)

    def test_json_empty(self):
        cc = UnorderedCardContainer.empty()
        self.assertEqual({'cards': []}, json.loads(cc.json()))

    def test_json_empty_load(self):
        cc = UnorderedCardContainer.empty()
        self.assertEqual(cc, UnorderedCardContainer(**json.loads(cc.json())))

    def test_json_some_cards(self):
        cc = UnorderedCardContainer.with_cards(
            Card(suit=Suit.HEARTS, rank=Rank.NUM_2),
            Card(suit=Suit.HEARTS, rank=Rank.NUM_4)
        )
        self.assertEqual({'cards': [
            {'suit': 'hearts', 'rank': '2'},
            {'suit': 'hearts', 'rank': '4'}
        ]}, json.loads(cc.json()))

    def test_json_some_cards_load(self):
        cc = UnorderedCardContainer.with_cards(
            Card(suit=Suit.HEARTS, rank=Rank.NUM_2),
            Card(suit=Suit.HEARTS, rank=Rank.NUM_4)
        )
        self.assertEqual(cc, UnorderedCardContainer(**json.loads(cc.json())))

    def test_json_full_load(self):
        cc = UnorderedCardContainer.full()
        self.assertEqual(cc, UnorderedCardContainer(**json.loads(cc.json())))

    def test_contains(self):
        cc = UnorderedCardContainer.with_cards(self.spades_king)
        self.assertEqual(1, len(cc))
        self.assertIn(self.spades_king, cc)

    def test_add(self):
        cc = UnorderedCardContainer.empty()
        cc.add(self.spades_king)
        self.assertEqual(1, len(cc))
        self.assertIn(self.spades_king, cc)

    def test_add_duplicate(self):
        cc = UnorderedCardContainer.empty()
        cc.add(self.spades_king)
        with self.assertRaises(ValueError):
            cc.add(self.spades_king)

    def test_add_none(self):
        cc = UnorderedCardContainer.empty()
        with self.assertRaises(ValueError):
            cc.add(None)

    def test_add_wrong_type(self):
        cc = UnorderedCardContainer.empty()
        with self.assertRaises(ValueError):
            cc.add('ace of spades')

    def test_remove(self):
        cc = UnorderedCardContainer.full()
        cc.remove(self.spades_king)
        self.assertNotIn(self.spades_king, cc)

    def test_remove_no_contain(self):
        cc = UnorderedCardContainer.empty()
        with self.assertRaises(ValueError):
            cc.remove(self.spades_king)

    def test_remove_none(self):
        cc = UnorderedCardContainer.full()
        with self.assertRaises(ValueError):
            cc.remove(None)

    def test_remove_wrong_type(self):
        cc = UnorderedCardContainer.full()
        with self.assertRaises(ValueError):
            cc.remove('ace of spades')

    def test_iter(self):
        queen_diamonds = Card(suit=Suit.DIAMONDS, rank=Rank.Q)
        cards = {self.spades_king, queen_diamonds}
        cc = UnorderedCardContainer.with_cards(cards)
        self.assertEqual(cards, {card for card in cc})

    def test_contains_suit(self):
        cc = UnorderedCardContainer.with_cards(self.spades_king)
        self.assertTrue(cc.contains_suit(Suit.SPADES))

    def test_not_contains_suit(self):
        cc = UnorderedCardContainer.with_cards(self.spades_king)
        self.assertFalse(cc.contains_suit(Suit.HEARTS))
        self.assertFalse(cc.contains_suit(Suit.CLUBS))
        self.assertFalse(cc.contains_suit(Suit.DIAMONDS))
