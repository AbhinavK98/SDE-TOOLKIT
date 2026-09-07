"""Observer Pattern - Tv

This file shows the Tv example in the Observer Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from observer import Observer


class TVDisplay(Observer):
    def update(self, temp):
        print(f"TV temprature updated to {temp}")

# Revision summary:
# - Part of the Observer Pattern examples.
# - Shows the Tv example.
# - Use this file to review the pattern and understand its purpose.
