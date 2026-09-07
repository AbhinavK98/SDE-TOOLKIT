"""Observer Pattern - Observer

This file shows the Observer example in the Observer Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, temp):
        pass

# Revision summary:
# - Part of the Observer Pattern examples.
# - Shows the Observer example.
# - Use this file to review the pattern and understand its purpose.
