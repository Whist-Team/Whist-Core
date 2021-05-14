"""
Scores over several hands.
"""
from pydantic import BaseModel

from whist.core.player import Player
from whist.core.scoring.score import Score


class ScoreCard(BaseModel):
    """
    Collects the results of severals hands.
    """
    hands: list[Score] = []

    def __len__(self):
        return len(self.hands)

    def add_score(self, score: Score) -> None:
        """
        Add the score of one hand.
        :param score: Score after one hand played
        :type score: Score
        :return: None
        :rtype: None
        """
        self.hands.append(score)

    def num_against_opp(self, player: Player, opponent: Player) -> int:
        """
        Getter for how many hands have been played against one particular opponent.
        :param player: for whom to look
        :type player: Player
        :param opponent: against the player played
        :type opponent: Player
        :return: Amount of hands played against one opponent.
        :rtype: int
        """
        hand: Score
        return len([hand for hand in self.hands if player in hand and opponent in hand])

    def score_against_opp(self, player: Player, opponent: Player) -> int:
        """
        Getter for how many hands have been won against one particular opponent.
        :param player: for whom to look
        :type player: Player
        :param opponent: against the player played
        :type opponent: Player
        :return: Amount of hands won against one opponent.
        :rtype: int
        """
        hand: Score
        return len([hand for hand in self.hands if player in hand and opponent in hand and hand[
            player] > hand[opponent]])
