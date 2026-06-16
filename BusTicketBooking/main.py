from src.admin import AdminPanel
from src.user import UserPanel
from src.bookings import BookingPanel 
from src.database import create_tables

def main():

    create_tables()
    admin = AdminPanel()
    user = UserPanel()
    booking = BookingPanel() 

    while True:
        print("---------------------------------------")
        print("-----Welcome to Bus Ticket Booking-----")
        print("----------------------------------------")
        print("Choose an option")
        print("1. Admin Panel")
        print("2. User Panel")
        print("3. Booking Panel")
        print("4. Exit Booking")
        user_input = input("Enter your choice 1/2/3/4 :")

        if user_input == "1":
            while True:
                print("--------------------------------")
                print("Welcome to Admin Panel")
                print("--------------------------------")
                print("1. Add Bus")
                print("2. View all Bus")
                print("3. Update Bus")
                print("4. Delete Bus")
                print("5. Exit Admin Panel")
                admin_choice = input("Enter your choice 1/2/3/4/5 :")
                if admin_choice == "1":
                    try:
                        bus_id = input("Enter bus ID :")
                        bus_name = input("Enter bus name :")
                        source = input("Enter source :")
                        destination = input("Enter destination :")
                        departure_time = input("Enter departure time :")
                        total_seats = int(input("Enter total seats :"))
                        price = float(input("Enter price :"))
                        admin.add_bus(
                                bus_id,
                                bus_name,
                                source,
                                destination,
                                departure_time,
                                total_seats,
                                price
                                )
                    except ValueError as v :
                        print("Invalid seats or price!")    
                    
                elif admin_choice == "2":
                    admin.view_all_buses()

                elif admin_choice == "3":
                    try:
                        bus_id = input("Enter bus ID :")
                        available_seats = int(input("Enter available seats :"))
                        admin.update_bus(bus_id, available_seats)
                    except ValueError:
                        print("Available seats must be a number!")    

                elif admin_choice == "4":
                    bus_id = input("Enter bus ID :")
                    admin.delete_bus(bus_id)

                elif admin_choice == "5":
                    print("Exiting Admin Panel.......")
                    break

                else:
                    print("Invalid input, Try again")    

        elif user_input == "2":
            while True:
                print("------------------------------")   
                print("Welcome to User Panel")
                print("------------------------------")
                print("1. Register")
                print("2. View User Details")
                print("3. Exit User Panel")  
                user_choice = input("Enter your choice 1/2/3 :")

                if user_choice == "1":
                    try:
                        user_id = input("Enter User ID : ")
                        name = input("Enter Name : ")
                        age = int(input("Enter Age : "))
                        mobile_number = input("Enter Mobile Number :")
                        user.register(user_id, name, age, mobile_number)
                    except ValueError as v:
                        print("Age should be in number!")
                        
                elif user_choice == "2":
                    user_id = input("Enter User ID : ")
                    user.view_user_details(user_id)

                elif user_choice == "3":
                    print("Exiting User Panel........")    
                    break
                else:
                    print("Invalid input, Try again")    

        elif user_input == "3":
            while True:
                print("-------------------------------")
                print("Welcome to Booking panel")
                print("-------------------------------")
                print("\n===== BOOKING PANEL =====")
                print("1. Search Bus")
                print("2. Book Ticket")
                print("3. Cancel Ticket")
                print("4. View My Bookings")
                print("5. Check Available Seats")
                print("6. Exit Booking Panel")     
                booking_choice = input("Enter your choice 1/2/3/4/5/6 :")
                if booking_choice == "1":
                    source = input("Enter your source :")
                    destination = input("Enter your destination :")
                    booking.search_bus(source, destination)
                    
                elif booking_choice == "2":
                    try:
                        booking_id = input("Enter your booking ID :")
                        user_id = input("Enter your user ID :")
                        bus_id = input("Enter your bus ID :")
                        journey_date = input("Enter your journey date (DD-MM-YYYY) : ")
                        seats = int(input("Enter number of seats :"))
                        booking.book_ticket(booking_id, user_id, bus_id, journey_date, seats,)
                    except ValueError as v:
                        print("Seats should be in number !!!")

                elif booking_choice == "3":
                    booking_id = input("Enter your booking ID :")
                    booking.cancel_ticket(booking_id)

                elif booking_choice == "4":
                    user_id = input("Enter your user ID :")
                    booking.view_my_booking(user_id)
                    
                elif booking_choice == "5":
                    bus_id = input("Enter your bus ID :")
                    booking.check_available_seats(bus_id)

                    
                elif booking_choice == "6":
                    print("Exiting Booking Panel........")
                    break

                else:
                    print("Invalid input, Try again") 

        elif user_input == "4":
            print("Thank you for using Bus Ticket Booking System. Exiting........") 
            break 
                    
        else:
            print("Invalid input, Try again")
main()          