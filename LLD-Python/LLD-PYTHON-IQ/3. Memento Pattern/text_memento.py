"""Memento Pattern - Text Memento

This file shows the Text Memento example in the Memento Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

class TextMemento:
    def __init__(self, text):
        self.__saved_text = text

    def get_saved_text(self):
        return self.__saved_text

# Revision summary:
# - Part of the Memento Pattern examples.
# - Shows the Text Memento example.
# - Use this file to review the pattern and understand its purpose.
