from pydantic import BaseModel


class DistributionEntry(BaseModel):
    player_index: int
    team_id: int


class Distribution(BaseModel):
    distributions: list[DistributionEntry] = []

    def __iter__(self):
        return iter(self.distributions)

    def add(self, entry: DistributionEntry) -> None:
        self.distributions.append(entry)
