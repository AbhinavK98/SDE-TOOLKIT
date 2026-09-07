"""
Create a class Movie with the following:

Attributes:
movie_name —> name of the movie
total_seats —> total seats available in the theatre
ticket_price —> price per ticket
booked_seats —> starts at 0

Methods:
book_ticket(num_tickets) — books the given number of tickets. If enough seats are available,
confirm the booking and show the total amount to pay. If not,
show "Sorry, not enough seats available"

show_status() — displays movie name, seats available, and seats booked so far
"""


class Movie:
    def __init__(self, movie_name: str, total_seats: int, ticket_price: int):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0

    def book_tickets(self, num_of_tickets: int):
        if num_of_tickets > self.total_seats - self.booked_seats:
            print("Sorry, not enough seats available")
        else:
            self.booked_seats += num_of_tickets
            self.total_seats -= num_of_tickets  # 30
            print(f"Your ticket is booked")
            print(f"Total price = {self.ticket_price * num_of_tickets}\n")

    def show_status(self) -> None:
        print(f"Movie name = {self.movie_name}")
        print(f"Seats available = {self.total_seats}")
        print(f"Total booked = {self.booked_seats}\n")


movie = Movie("Krish", 100, 499)
movie.show_status()
movie.book_tickets(70)

movie.show_status()

movie.book_tickets(70)

# Revision summary:
# - Part of the Oops Recap examples.
# - Shows the Movie Project example.
# - Use this file to review the pattern and understand its purpose.
