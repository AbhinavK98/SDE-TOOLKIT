"""State Pattern - Transport Service

This file shows the Transport Service example in the State Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from transport_mode import TransportMode


class TransportService:
    def __init__(self, mode: TransportMode):
        self.__mode: TransportMode = mode

    def set_mode(self, new_mode: TransportMode):
        self.__mode: TransportMode = new_mode

    def eta(self):
        self.__mode.eta()

    def directions(self):
        self.__mode.directions()

# Revision summary:
# - Part of the State Pattern examples.
# - Shows the Transport Service example.
# - Use this file to review the pattern and understand its purpose.
