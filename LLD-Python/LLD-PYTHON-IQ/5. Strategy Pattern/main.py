"""Strategy Pattern - Main

This file shows the main runner for the example in the Strategy Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from discount_service import DiscountService
from diawli import DiwaliStrategy
from holi import HoliStrategy


diwali_strategy = DiwaliStrategy()
holi_strategy = HoliStrategy()

discount_service = DiscountService(diwali_strategy)
discount_service.process()

discount_service.set_strategy(holi_strategy)
discount_service.process()

# Revision summary:
# - Part of the Strategy Pattern examples.
# - Shows the main runner for the example.
# - Use this file to review the pattern and understand its purpose.
