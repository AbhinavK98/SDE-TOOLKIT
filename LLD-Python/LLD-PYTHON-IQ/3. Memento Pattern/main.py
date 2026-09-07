"""Memento Pattern - Main

This file shows the main runner for the example in the Memento Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from history import History
from text_editor import TextEditor
from text_memento import TextMemento

text_editor = TextEditor()
history = History()

text_editor.write("Hello")
text_editor.write(" World")
history.save_state(text_editor.save())
text_editor.write(" Good")
text_editor.write(" Bye")
history.save_state(text_editor.save())
print(text_editor.get_text())
print("-------")
text_editor.restore(history.undo())
print(text_editor.get_text())
text_editor.restore(history.undo())
print(text_editor.get_text())

# Revision summary:
# - Part of the Memento Pattern examples.
# - Shows the main runner for the example.
# - Use this file to review the pattern and understand its purpose.
