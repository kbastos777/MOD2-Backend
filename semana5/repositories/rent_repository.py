class RentRepository:
    def __init__(self,db_manager):
        self.db_manager = db_manager


    def _format_rent(self,rent_record):
        return {
            "id": rent_record[0],
            "userid": rent_record[1],
            "carid": rent_record[2],
            "rent_date": rent_record[3],
            "state": rent_record[4]
        }


    def get_all_rents(self):
        try:
            results = self.db_manager.execute_query("SELECT * FROM lyfter_car_rental.CarXuser ORDER BY id ASC;")
            formatted_results = [self._format_rent(result) for result in results]
            return formatted_results
        except Exception as err:
            print("Error getting all rents from the database: ", err)
            return False


    def get_by_id(self,_id):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.CarXuser WHERE id = %s;",_id
            )
            formatted_result = self._format_rent(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting a rent id from the database: ", error)
            return False


    def get_by_user_id(self,_userid):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.CarXuser WHERE userid = %s;",_userid
            )
            formatted_results = [self._format_rent(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting a user id from the database: ", error)
            return False


    def get_by_car_id(self,_carid):
            try:
                results = self.db_manager.execute_query(
                    "SELECT * FROM lyfter_car_rental.CarXuser WHERE carid = %s;",_carid
                )
                formatted_results = [self._format_rent(result) for result in results]
                return formatted_results
            except Exception as error:
                print("Error getting a car id from the database: ", error)
                return False


    def get_by_rent_date(self,_rent_date):
            try:
                results = self.db_manager.execute_query(
                    "SELECT * FROM lyfter_car_rental.CarXuser WHERE rent_date = %s;",_rent_date
                )
                formatted_results = [self._format_rent(result) for result in results]
                return formatted_results
            except Exception as error:
                print("Error getting rent date from the database: ", error)
                return False


    def get_by_rent_state(self,_state):
            try:
                results = self.db_manager.execute_query(
                    "SELECT * FROM lyfter_car_rental.CarXuser WHERE state = %s;",_state
                )
                formatted_results = [self._format_rent(result) for result in results]
                return formatted_results
            except Exception as error:
                print("Error getting rent state from the database: ", error)
                return False


    def create_new_rent(self,userid,carid,rent_date,state):
            try:
                self.db_manager.execute_query("INSERT INTO lyfter_car_rental.Carxuser (userid,carid,rent_date,state) VALUES (%s,%s,%s,%s);",userid,carid,rent_date,state)
                print("Rent created successfully")
                return True
            except Exception as error:
                print("Error creating new rent: ", error)
                return False


    def update(self,_id,userid,carid,rent_date,state):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.CarXuser SET (userid,carid,rent_date,state) = (%s,%s,%s,%s) WHERE ID = %s",userid,carid,rent_date,state,_id
            )
            print("Rent updated successfully")
            return True
        except Exception as error:
            print("Error updating a rent from the database: ", error)
            return False


    def delete(self, _id):
        try:
            self.db_manager.execute_query(
                "DELETE FROM lyfter_car_rental.CarXuser WHERE id = (%s)", _id
            )
            print("Rent deleted successfully")
            return True
        except Exception as error:
            print("Error deleting a rent from the database: ", error)
            return False