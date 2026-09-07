"""State Pattern - Main

This file shows the main runner for the example in the State Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from transport_Service import TransportService
from bike_mode import BikeMode

b = BikeMode()
transport_service = TransportService(b)
transport_service.eta()
transport_service.directions()

# Revision summary:
# - Part of the State Pattern examples.
# - Shows the main runner for the example.
# - Use this file to review the pattern and understand its purpose.
