class Vehicle:
    def __init__(self, vehicleID, model, rentalRate, isRented) -> None:
        self.vehicleID = vehicleID
        self.model = model
        self.rentalRate = rentalRate
        self.isRented = isRented


    def rentVehicle(self):
        if self.isRented == False:
            self.isRented = True
            return True
        else:
            return False
    
    def returnVehicle(self):
        self.isRented = False


class Rental:
    def __init__(self, rentalID, vehicleID, customerName, rentalDuration) -> None:
        self.rentalID = rentalID
        self.vehicleID = vehicleID
        self.customerName = customerName
        self.rentalDuration = rentalDuration

    def getRentalDetails(self):
        return f"{self.rentalID}, {self.vehicleID}, {self.customerName}, {self.rentalDuration}"
    

class RentalService:
    def __init__(self, vehicles, rentals) -> None:
        self.vehicles = vehicles
        self.rentals = rentals
    
    def createRental(self, rental):
        for vehicle in self.vehicles:
            if vehicle.vehicleID == rental.vehicleID and not vehicle.isRented:
                vehicle.rentVehicle()
            self.rentals.append(rental)
            return True
        return False
   
    def endRental(self, rentalID):
        for rental in self.rentals:
            if rental.rentalID == rentalID:
                for vehicle in self.vehicles:
                    if vehicle.vehicleID == rental.vehicleID:
                        vehicle.returnVehicle()
                        self.rentals.remove(rental)
                        return True
        return False













def main():
    # Create a vehicle and test rental and return
    vehicle = Vehicle(1, "Sedan", 40.0, False)
    print("Vehicle rented (should be True):", vehicle.rentVehicle())
    print("Vehicle rented again (should be False):", vehicle.rentVehicle())
    vehicle.returnVehicle()
    print("Vehicle available after return:", not vehicle.isRented)

    # Create a rental record and service
    rental = Rental(1, vehicle.vehicleID, "Anna", 3)
    service = RentalService([vehicle], [])
    created = service.createRental(rental)
    print("Rental created:", created)

    # End the rental and verify
    ended = service.endRental(1)
    print("Rental ended:", ended)
    print("Vehicle available after ending rental:", not vehicle.isRented)

if __name__ == '__main__':
    main()