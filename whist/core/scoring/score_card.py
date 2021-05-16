"""
Scores over several hands.
"""
from pydantic import BaseModel

from whist.core.scoring.score import Score
from whist.core.scoring.team import Team


class ScoreCard(BaseModel):
    """
    Collects the results of several hands.
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

    def score(self, team: Team) -> int:
        """
        Getter for how many hands have been won by a team.
        :param team: for whom to look
        :type team: Team
        :return: Amount of hands won.
        :rtype: int
        """
        hand: Score
        return len([hand for hand in self.hands if hand.won(team)])

    def won(self, team):
        """
        Check if the team won more hands.
        :param team: Team for which to check.
        :type team: Team
        :return: 1 if the team won more hands. 0 if they lost as many as they won. -1 if the lost
        more games than won.
        :rtype: int
        """
        score = self.score(team)
        games = len(self.hands)
        if score > games / 2:
            return 1
        if score == games / 2:
            return 0
        return -1
