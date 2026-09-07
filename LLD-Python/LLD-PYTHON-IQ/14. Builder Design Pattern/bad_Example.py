"""Builder Design Pattern - Bad Example

This file shows the bad example implementation in the Builder Design Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

class Laptop:
    def __init__(
        self,
        processor: str,
        ram: str,
        graphic_card: str = None,
        color: str = None,
        screen_size: str = None,
    ):
        self.processor = processor
        self.ram = ram
        self.graphic_card = graphic_card
        self.color = color
        self.screen_size = screen_size

    def display_specs(self):
        print(f"Processor = {self.processor}")
        print(f"Ram = {self.ram}GB")
        if self.graphic_card:
            print(f"Graphic Card = {self.graphic_card}")
        if self.color:
            print(f"Color = {self.color}")
        if self.screen_size:
            print(f"Screen Size = {self.screen_size}")


laptop1 = Laptop("i5-3232", "6")
laptop1.display_specs()

laptop2 = Laptop("i5-3232", "6", None, "Black", None)
laptop2.display_specs()

# Revision summary:
# - Part of the Builder Design Pattern examples.
# - Shows the bad example implementation.
# - Use this file to review the pattern and understand its purpose.
