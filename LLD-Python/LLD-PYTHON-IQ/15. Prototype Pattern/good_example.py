"""Prototype Pattern - Good Example

This file shows the good example implementation in the Prototype Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from typing import List
import copy


class ChessPiece:
    def __init__(self, name: str, position: str, color: str):
        self.name = name
        self.position = position
        self.color = color

    def display(self):
        return f"{self.color} {self.name} is at {self.position}"

    def clone(self):
        return copy.deepcopy(self)
        # return ChessPiece(self.name, self.position, self.color)


class ChessBoard:
    def __init__(self):
        self.pieces: List[ChessPiece] = []

    def add_piece(self, piece: "ChessPiece"):
        self.pieces.append(piece)

    def display_board(self):
        print("\nBoard State")
        for piece in self.pieces:
            print(f"   {piece.display()}")

    def clone(self):
        return copy.deepcopy(self)


piece1 = ChessPiece("King", "e2", "Black")
piece2 = ChessPiece("Queen", "a1", "Black")
piece3 = ChessPiece("King", "c3", "White")
piece4 = ChessPiece("Queen", "d2", "White")

chess_board = ChessBoard()
chess_board.add_piece(piece1)
chess_board.add_piece(piece2)
chess_board.add_piece(piece3)
chess_board.add_piece(piece4)

chess_board.display_board()


new_chess_board = chess_board.clone()


print("------------")
new_chess_board.add_piece(ChessPiece("Soldier", "d7", "black"))
new_chess_board.display_board()
chess_board.display_board()

# Revision summary:
# - Part of the Prototype Pattern examples.
# - Shows the good example implementation.
# - Use this file to review the pattern and understand its purpose.
