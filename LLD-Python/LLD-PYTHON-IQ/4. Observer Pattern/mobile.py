"""Observer Pattern - Mobile

This file shows the Mobile example in the Observer Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from observer import Observer


class MobileDisplay(Observer):
    def update(self, temp):
        print(f"Mobile temprature updated to {temp}")

# Revision summary:
# - Part of the Observer Pattern examples.
# - Shows the Mobile example.
# - Use this file to review the pattern and understand its purpose.
