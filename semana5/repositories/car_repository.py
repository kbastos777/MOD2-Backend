class CarRepository:
    def __init__(self,db_manager):
        self.db_manager = db_manager


    def _format_car(self,car_record):
        return {
            "id": car_record[0],
            "brand": car_record[1],
            "model": car_record[2],
            "year": car_record[3],
            "state": car_record[4]
        }


    def get_all_cars(self):
        try:
            results = self.db_manager.execute_query("SELECT * FROM lyfter_car_rental.Cars ORDER BY id ASC;")
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as err:
            print("Error getting all cars from the database: ", err)
            return False


    def get_by_id(self,_id):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.Cars WHERE id = %s;",_id
            )
            formatted_result = self._format_car(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting a car id from the database: ", error)
            return False


    def get_by_brand(self,_brand):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.Cars WHERE brand = %s;",_brand
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting a car(s) brand from the database: ", error)
            return False


    def get_by_model(self,_model):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.Cars WHERE model = %s;",_model
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting a car(s) model from the database: ", error)
            return False


    def get_by_year(self,_year):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.Cars WHERE year = %s;",_year
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting a car(s) year from the database: ", error)
            return False


    def get_by_state(self,_state):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.Cars WHERE state = %s;",_state
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting a car(s) state from the database: ", error)
            return False


    def create_new_car(self,brand,model,year,state):
        try:
            self.db_manager.execute_query("INSERT INTO lyfter_car_rental.Cars (brand,model,year,state) VALUES (%s,%s,%s,%s);",brand,model,year,state)
            print("Car created successfully")
            return True
        except Exception as error:
            print("Error creating new car: ", error)
            return False


    def update(self,_id,brand,model,year,state):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.Cars SET (brand,model,year,state) = (%s,%s,%s,%s) WHERE ID = %s",
                brand,model,year,state,_id
            )
            print("Car updated successfully")
            return True
        except Exception as error:
            print("Error updating a car from the database: ", error)
            return False


    def delete(self, _id):
        try:
            self.db_manager.execute_query(
                "DELETE FROM lyfter_car_rental.Cars WHERE id = (%s)", _id
            )
            print("Car deleted successfully")
            return True
        except Exception as error:
            print("Error deleting a Car from the database: ", error)
            return False