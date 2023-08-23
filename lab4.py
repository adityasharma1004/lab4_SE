class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        matching_flights = []
        for flight in self.flights:
            if flight.source == city or flight.destination == city:
                matching_flights.append(flight)
        return matching_flights

    def search_by_source_destination(self, source, destination):
        matching_flights = []
        for flight in self.flights:
            if flight.source == source and flight.destination == destination:
                matching_flights.append(flight)
        return matching_flights

    def print_flights(self, flight_list):
        if not flight_list:
            print("No flights found.")
        else:
            print("Flight ID  From  To    Price")
            print("----------------------------")
            for flight in flight_list:
                print(f"{flight.flight_id}  {flight.source}  {flight.destination}  {flight.price}")

def main():
    flight_table = FlightTable()

    flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    while True:
        print("\nSearch options:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            city = input("Enter the city: ")
            matching_flights = flight_table.search_by_city(city)
            flight_table.print_flights(matching_flights)
        elif choice == 2:
            source = input("Enter the source city: ")
            matching_flights = flight_table.search_by_city(source)
            flight_table.print_flights(matching_flights)
        elif choice == 3:
            source = input("Enter the source city: ")
            destination = input("Enter the destination city: ")
            matching_flights = flight_table.search_by_source_destination(source, destination)
            flight_table.print_flights(matching_flights)
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
