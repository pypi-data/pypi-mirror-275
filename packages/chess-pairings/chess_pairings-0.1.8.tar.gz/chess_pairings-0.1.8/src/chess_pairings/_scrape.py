from typing import Any
from haskellian import Either
from .types import GroupPairings, PairingsSource

async def scrape_pairings(source: PairingsSource) -> Either[Any, GroupPairings]:
  match source.root.tag:
    case 'chess-results':
      from .chess_results import scrape_pairings
      return await scrape_pairings(source.root.db_key)