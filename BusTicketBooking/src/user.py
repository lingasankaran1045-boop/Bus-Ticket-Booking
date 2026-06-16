from src.database import (
    register_user_db,
    get_user_details_db
)

class UserPanel():

    def register(self, user_id, name,
                 age, mobile_number):
        
        register_user_db(
            user_id,
            name,
            age,
            mobile_number
        )
        print("User Register successfully")

    def view_user_details(self, user_id):

        user = get_user_details_db(user_id) 

        if not user:
            print("No user found")
            return

        print("\n User detials")
        print("---------------------------")
        print(f"User ID : {user[0]}")
        print(f"Name : {user[1]}")
        print(f"Age : {user[2]}")
        print(f"Mobile number : {user[3]}")   