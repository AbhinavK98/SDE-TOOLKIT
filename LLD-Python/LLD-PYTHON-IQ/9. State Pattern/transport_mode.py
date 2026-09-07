"""State Pattern - Transport Mode

This file shows the Transport Mode example in the State Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from abc import ABC, abstractmethod


class TransportMode(ABC):
    @abstractmethod
    def eta(self):
        pass

    @abstractmethod
    def directions(self):
        pass

# Revision summary:
# - Part of the State Pattern examples.
# - Shows the Transport Mode example.
# - Use this file to review the pattern and understand its purpose.
