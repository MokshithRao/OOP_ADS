class Movie:
    def __init__(self, movieID, title, duration):
        self.movieID = movieID
        self.title = title
        self.duration = duration

    def getTitle(self):
        return self.title


class Ticket:
    def __init__(self, ticketID, movieID, seatNumber, price):
        self.ticketID = ticketID
        self.movieID = movieID
        self.seatNumber = seatNumber
        self.price = price

    def getTicketInfo(self):
        return f"Ticket ID: {self.ticketID}, Movie ID: {self.movieID}, Seat: {self.seatNumber}, Price: {self.price}"


class Booking:
    def __init__(self, tickets=None):
        if tickets is None:
            tickets = []
        self.tickets = tickets

    def bookTicket(self, ticket):
        self.tickets.append(ticket)

    def cancelTicket(self, ticketID):
        for ticket in self.tickets:
            if ticket.ticketID == ticketID:
                self.tickets.remove(ticket)
                return True
        return False

    def getBookingDetails(self):
        return self.tickets


def main():
    # Create a movie and multiple tickets
    movie = Movie(1, "Inception", 148)
    ticket1 = Ticket(101, movie.movieID, "A10", 12.5)
    ticket2 = Ticket(102, movie.movieID, "A11", 12.5)
    
    booking = Booking()
    
    # Test booking tickets
    booking.bookTicket(ticket1)
    booking.bookTicket(ticket2)
    
    if len(booking.getBookingDetails()) != 2:
        print("Error: Tickets not booked correctly.")
    
    # Test ticket cancellation
    cancel_valid = booking.cancelTicket(101)
    print("Ticket 101 cancelled:", cancel_valid)
    
    cancel_invalid = booking.cancelTicket(999)
    print("Attempt cancellation of non-existent ticket:", cancel_invalid)
    
    # Final booking details
    print("Remaining tickets:")
    for t in booking.getBookingDetails():
        print(t.getTicketInfo())


if __name__ == '__main__':
    main()
