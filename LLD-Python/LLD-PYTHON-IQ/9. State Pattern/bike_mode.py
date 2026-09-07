"""State Pattern - Bike Mode

This file shows the Bike Mode example in the State Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from transport_mode import TransportMode


class BikeMode(TransportMode):
    def eta(self):
        print("Bike will take 15 mins")

    def directions(self):
        print("Go left to the road")

# Revision summary:
# - Part of the State Pattern examples.
# - Shows the Bike Mode example.
# - Use this file to review the pattern and understand its purpose.
