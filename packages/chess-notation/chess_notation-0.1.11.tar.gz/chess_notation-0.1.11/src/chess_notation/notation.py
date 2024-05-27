from typing import NamedTuple, get_args, Sequence
import random
import chess
from .language import Language, LANGUAGES, translate
from .styles import Styles, Check, Mate, Castle, PawnCapture, PieceCapture, style, CapturedPiece

class Notation(NamedTuple):
  language: Language
  styles: Styles

def random_notation() -> Notation:
  lang = random.choice(LANGUAGES)
  check = random.choice(get_args(Check))
  mate = random.choice(get_args(Mate))
  castle = random.choice(get_args(Castle))
  pawn = random.choice(get_args(PawnCapture))
  piece = random.choice(get_args(PieceCapture))
  styles = Styles(castle=castle, check=check, mate=mate, pawn_capture=pawn, piece_capture=piece)
  return Notation(language=lang, styles=styles)

def simple_styled(sans: Sequence[str], notation: Notation) -> Sequence[str]:
  return [translate(style(move, notation.styles), notation.language) for move in sans]

def captured_piece(board: chess.Board, move: chess.Move) -> CapturedPiece | None:
  """The piece captured by `move` on `board` (or `None`)"""
  type = board.piece_type_at(move.to_square)
  if type is not None:
    return chess.piece_symbol(type).upper() # type: ignore

def validated_styled(sans: Sequence[str], notation: Notation) -> Sequence[str]:
  output = []
  board = chess.Board()
  for san in sans:
    move = board.parse_san(san)
    type = board.piece_type_at(move.to_square)
    piece = captured_piece(board, move)
    output.append(translate(style(san, notation.styles, piece), notation.language))
    board.push(move)
  return output

def styled(sans: Sequence[str], notation: Notation) -> Sequence[str]:
  if notation.styles.pawn_capture == 'PxN' or notation.styles.piece_capture == 'NxN':
    return validated_styled(sans, notation)
  else:
    return simple_styled(sans, notation)