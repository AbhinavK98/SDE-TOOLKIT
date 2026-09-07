"""State Pattern - Walk Mode

This file shows the Walk Mode example in the State Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from transport_mode import TransportMode


class WalkMode(TransportMode):
    def eta(self):
        print("Walk will take 30 mins")

    def directions(self):
        print("Walk right to the road and then left")

# Revision summary:
# - Part of the State Pattern examples.
# - Shows the Walk Mode example.
# - Use this file to review the pattern and understand its purpose.
