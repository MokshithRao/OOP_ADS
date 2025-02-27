class Flight:
    def __init__(self, flightNumber, origin, destination, seatsAvailable):
        self.flightNumber = flightNumber
        self.origin = origin
        self.destination = destination
        self.seatsAvailable = seatsAvailable

    def reserveSeat(self):
        if self.seatsAvailable > 0:
            self.seatsAvailable -= 1
            return True
        return False


class Reservation:
    def __init__(self, reservationID, flightNumber, passengerName):
        self.reservationID = reservationID
        self.flightNumber = flightNumber
        self.passengerName = passengerName

    def getReservationDetails(self):
        return f"Reservation ID: {self.reservationID}, Flight: {self.flightNumber}, Passenger: {self.passengerName}"


class ReservationManager:
    def __init__(self, flights=None, reservations=None):
        if flights is None:
            flights = []
        if reservations is None:
            reservations = []
        self.flights = flights
        self.reservations = reservations

    def makeReservation(self, flightNumber, passengerName):
        for flight in self.flights:
            if flight.flightNumber == flightNumber and flight.reserveSeat():
                reservation = Reservation(len(self.reservations) + 1, flightNumber, passengerName)
                self.reservations.append(reservation)
                return reservation
        return None

    def cancelReservation(self, reservationID):
        for reservation in self.reservations:
            if reservation.reservationID == reservationID:
                self.reservations.remove(reservation)
                return True
        return False


def main():
    # Create a flight with limited seats
    flight = Flight("FL123", "New York", "London", 2)
    
    # Reserve seats until flight is full
    print("Seat reservation 1:", flight.reserveSeat())
    print("Seat reservation 2:", flight.reserveSeat())
    print("Seat reservation 3 (should fail):", flight.reserveSeat())
    
    # Create reservations
    reservation1 = Reservation(1, flight.flightNumber, "John Smith")
    reservation2 = Reservation(2, flight.flightNumber, "Jane Doe")
    
    # Create ReservationManager and add the flight
    rm = ReservationManager([flight], [])
    rm.makeReservation(flight.flightNumber, "John Smith")
    rm.makeReservation(flight.flightNumber, "Jane Doe")
    
    # Display and cancel reservation
    print("Reservation details for ID 1:", reservation1.getReservationDetails())
    cancelled = rm.cancelReservation(1)
    print("Reservation 1 cancelled:", cancelled)


if __name__ == '__main__':
    main()
