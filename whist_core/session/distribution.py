from pydantic import BaseModel


class DistributionEntry(BaseModel):
    player_index: int
    team_id: int


class Distribution(BaseModel):
    entries: list[DistributionEntry] = []

    def __iter__(self):
        return iter(self.entries)

    def __len__(self):
        return len(self.entries)

    def __getitem__(self, item):
        return self.entries[item]

    def add(self, entry: DistributionEntry) -> None:
        self.entries.append(entry)
