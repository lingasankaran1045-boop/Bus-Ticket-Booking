from src.database import(
    search_bus_db,
    book_ticket_db,
    cancel_ticket_db,
    get_user_booking_db,
    get_available_seats_db
    )

class BookingPanel():

    def search_bus(self, source, destination, ):

        buses = search_bus_db(
            source,
            destination
        )

        if not buses:
            print("No buses found!!!")
            return
        
        for bus in buses:
            print(
                f"Bus ID : {bus[0]} | "
                f"Bus Name : {bus[1]} | "
                f"Route : {bus[2]} -> {bus[3]} | "
                f"Departure : {bus[4]} | "
                f"Seats : {bus[5]} | "
                f"Price : ₹ {bus[6]}"
            )

    def book_ticket(self, booking_id, user_id, bus_id, journey_date, seats,):

        book_ticket_db(
            booking_id,
            user_id,
            bus_id,
            journey_date,
            seats,
        )    
        print("Ticket booked successfully")    

    def cancel_ticket(self, booking_id):

        cancel_ticket_db(booking_id) 
        print("Ticket cancelled successfully")

    def view_my_booking(self, user_id):

        bookings = get_user_booking_db(user_id)

        if not bookings:
            print("No booking found!!!")
            return

        for booking in bookings:
            print(
                f"Booking ID : {booking[0]} | "
                f"User ID : {booking[1]} | "
                f"Bus ID : {booking[2]} | "
                f"Journey Date : {booking[3]} | "
                f"Seats : {booking[4]}"
            )

    def check_available_seats(self, bus_id):

        seats = get_available_seats_db(bus_id)
        print(f"Available seats : {seats}")


