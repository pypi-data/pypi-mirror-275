from typing import Iterable
import chess

def sans2ucis(sans: Iterable[str]) -> Iterable[str]:
  board = chess.Board()
  for san in sans:
    move = board.parse_san(san)
    yield move.uci()
    board.push(move)

def ucis2sans(ucis: Iterable[str]) -> Iterable[str]:
  """Parses UCIs into SAN. Stops whenever it finds an illegal move."""
  board = chess.Board()
  try:
    for uci in ucis:
      move = chess.Move.from_uci(uci)
      board.push(move)
      yield board.san(move)
  except:
    ...