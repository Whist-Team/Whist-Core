from pydantic import BaseModel


class Rubber(BaseModel):
    max_games: int = 3
    _games_played = 0

    @property
    def games_played(self) -> int:
        return self._games_played

    @property
    def done(self) -> bool:
        return self.games_played == 3
