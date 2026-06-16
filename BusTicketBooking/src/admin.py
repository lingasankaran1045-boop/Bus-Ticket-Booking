from src.database import (
    add_bus_db,
    get_all_buses,
    update_bus_db,
    delete_bus_db
)

class AdminPanel():
    def add_bus(self, bus_id, bus_name, source, 
                destination, departure_time, 
                total_seats, price):
        
        add_bus_db(
            bus_id,
            bus_name,
            source,
            destination,
            departure_time,
            total_seats,
            price
            )
        print("Bus added successfully")

    def view_all_buses(self):
        buses = get_all_buses() 

        if not buses:
            print("No buses available")
            return
        
        for bus in buses:
            print(
                f"Bus ID : {bus[0]} | "
                f"Bus Name : {bus[1]} | "
                f"Route : {bus[2]} -> {bus[3]} | "
                f"Departure : {bus[4]} | "
                f"Seats : {bus[5]} | "
                f"Price : ₹{bus[6]}"
            )

    def update_bus(self, bus_id, available_seats):
        update_bus_db(
            bus_id,
            available_seats
        )         
        print("Bus updated sucessfully")

    def delete_bus(self, bus_id):
        delete_bus_db(
            bus_id
        )    
        print("Bus deleted sucessfully")