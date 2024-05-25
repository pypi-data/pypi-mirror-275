from typing import Literal
from pydantic import BaseModel, RootModel, Field

class ChessResultsPairings(BaseModel):
  tag: Literal['chess-results'] = 'chess-results'
  db_key: int

class PairingsSource(RootModel):
  root: ChessResultsPairings = Field(discriminator='tag')