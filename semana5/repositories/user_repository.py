

class UserRepository:
    def __init__(self,db_manager):
        self.db_manager = db_manager


    def _format_user(self, user_record):
        return {
        "id": user_record[0],
        "name": user_record[1],
        "username": user_record[2],
        "email": user_record[3],
        "password": user_record[4],
        "birthdate": user_record[5],
        "account_state": user_record[6]
    }


    def get_all_users(self):
        try:
            results = self.db_manager.execute_query("SELECT * FROM lyfter_car_rental.Users ORDER BY id ASC;")
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as err:
            print("Error getting all users from the database: ", err)
            return False


    def get_by_id(self,_id):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.Users WHERE id = %s;",_id
            )
            formatted_result = self._format_user(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting an user id from the database: ", error)
            return False


    def get_by_name(self,_name):
        try:
            print(f"Este es el valor de name:{_name}")
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.Users WHERE name = %s;",_name
            )
            formatted_result = self._format_user(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting an user name from the database: ", error)
            return False


    def get_by_username(self,_username):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.Users WHERE username = %s;",_username
            )
            formatted_result = self._format_user(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting an username from the database: ", error)
            return False


    def get_by_email(self,_email):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.Users WHERE email = %s;",_email
            )
            formatted_result = self._format_user(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting an user email from the database: ", error)
            return False


    def get_by_password(self,_password):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.Users WHERE password = %s;",_password
            )
            formatted_result = self._format_user(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting an user password from the database: ", error)
            return False


    def get_by_birthdate(self,_birthdate):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.Users WHERE birthdate = %s;",_birthdate
            )
            formatted_result = self._format_user(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting an user birthdate from the database: ", error)
            return False


    def get_by_account_state(self,_account_state):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.Users WHERE account_state like %s;",_account_state
            )
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting an user account state from the database: ", error)
            return False


    def create_new_user(self,name,username,email,password,birthdate,account_state):
        try:
            self.db_manager.execute_query("INSERT INTO lyfter_car_rental.Users (name,username,email,password,birthdate,account_state) VALUES (%s,%s,%s,%s,%s,%s);",name, username, email, password, birthdate, account_state)
            print("User created successfully")
            return True
        except Exception as error:
            print("Error creating new user: ", error)
            return False



    def update(self,_id,name,username,email,password,birthdate,account_state):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.Users SET (name,username,email,password,birthdate,account_state) = (%s, %s, %s,%s, %s, %s) WHERE ID = %s",
                name,username,email,password,birthdate,account_state,_id
            )
            print("User updated successfully")
            return True
        except Exception as error:
            print("Error updating a user from the database: ", error)
            return False


    def delete(self, _id):
        try:
            self.db_manager.execute_query(
                "DELETE FROM lyfter_car_rental.Users WHERE id = (%s)", _id
            )
            print("User deleted successfully")
            return True
        except Exception as error:
            print("Error deleting a user from the database: ", error)
            return False