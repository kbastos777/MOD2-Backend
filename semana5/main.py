from database.db import PgManager
from repositories.user_repository import UserRepository
from repositories.car_repository import CarRepository
from repositories.rent_repository import RentRepository
from flask import Flask
from flask import request,jsonify
from datetime import datetime


db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="Bold2024",
    host="localhost"
)


app = Flask(__name__)

#USER APIs

@app.route("/users", methods=["POST"])
def register_user():
    try:    
        users_repo = UserRepository(db_manager)
        name = request.form.get("name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        birthdate = request.form.get("birthdate")
        account_state = request.form.get("account_state")
        if any([users_repo.get_by_username(username),users_repo.get_by_email(email)]):
            raise ValueError("This username or email already exists")
        elif not all([name,username,email,password,birthdate,account_state]):
                raise ValueError("Please make sure you enter all the required fields")
        elif "@" not in email:
            raise ValueError("Invalid format for email, please enter the following format: example@example.com")
        elif account_state not in ["active","inactive","debtor"]:
            raise ValueError("Please make sure you enter active, inactive or debtor on the account_state field")
        try:
            datetime.strptime(birthdate, "%Y-%m-%d")
        except ValueError:
                raise ValueError("Invalid date format, please enter yyyy-mm-dd")
        users_repo.create_new_user(name,username,email,password,birthdate,account_state)
        return jsonify(message="User has been successfully created"), 201
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/users", methods=["PUT"])
def update_user():
    try:
        users_repo = UserRepository(db_manager)
        user_id = request.form.get("id")
        name = request.form.get("name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        birthdate = request.form.get("birthdate")
        account_state = request.form.get("account_state")
        if any([users_repo.get_by_username(username),users_repo.get_by_email(email)]):
            raise ValueError("This username or email already exists")
        elif not all([user_id,name,username,email,password,birthdate,account_state]):
                raise ValueError("Please make sure you enter all the required fields")
        elif not users_repo.get_by_id(user_id):  
                raise ValueError("Unable to update user, please check if id field is correct or does exist")
        elif "@" not in email:
            raise ValueError("Invalid format for email, please enter the following format: example@example.com")
        users_repo.update(user_id,name,username,email,password,birthdate,account_state)
        try:
            datetime.strptime(birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format, please enter yyyy-mm-dd")
        return jsonify(message="User has been successfully updated"), 201
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/users", methods=["DELETE"])
def delete_user():
    try:
        users_repo = UserRepository(db_manager)
        user_id = request.form.get("id")
        if not users_repo.get_by_id(user_id):  
            raise ValueError("Unable to delete user, please check if id field is correct or does exist")
        users_repo.delete(user_id)
        return jsonify(message="User has been successfully deleted"), 201
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/users")
def get_all_users():
    try:
        users_repo = UserRepository(db_manager)
        user_id = request.form.get("id")
        name = request.form.get("name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        birthdate = request.form.get("birthdate")
        account_state = request.form.get("account_state")
        if not all([user_id,name,username,email,password,birthdate,account_state]):
            raise ValueError("Please make sure to enter all the required fields")
        return users_repo.get_all_users()
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/users/id")
def get_user_by_id():
    try:
        users_repo = UserRepository(db_manager)
        user_id = request.form.get("id")
        if "id" not in request.form:
            raise ValueError("id field is missing")
        elif not users_repo.get_by_id(user_id):
            raise ValueError("ID does not exist in records")
        return users_repo.get_by_id(user_id)
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/users/name")
def get_user_by_name():
    try:
        users_repo = UserRepository(db_manager)
        name = request.form.get("name")
        if "name" not in request.form:
            raise ValueError("Missing name")
        elif not users_repo.get_by_name(name):
            raise ValueError("Name does not exist in records")
        return users_repo.get_by_name(name)
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/users/username")
def get_user_by_username():
    try:
        users_repo = UserRepository(db_manager)
        username = request.form.get("username")
        if "username" not in request.form:
            raise ValueError("Missing username")
        elif not users_repo.get_by_username(username):
            raise ValueError("Username does not exist in records")
        return users_repo.get_by_username(username)
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
            return jsonify(message=str(err)), 500


@app.route("/users/email")
def get_user_by_email():
    try:
        users_repo = UserRepository(db_manager)
        email = request.form.get("email")
        if "email" not in request.form:
            raise ValueError("Email is missing")
        elif "@" not in email:
            raise ValueError("Invalid format for email, please enter the following format: example@example.com")
        elif not users_repo.get_by_email(email):
            raise ValueError("Email does not exist in records")
        return users_repo.get_by_email(email)
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/users/password")
def get_user_by_password():
    try:
        users_repo = UserRepository(db_manager)
        password = request.form.get("password")
        return users_repo.get_by_password(password)
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/users/birthdate")
def get_user_by_birthdate():
    try:
        users_repo = UserRepository(db_manager)
        birthdate = request.form.get("birthdate")
        if "birthdate" not in request.form:
            raise ValueError("Missing birthdate")
        try:
            datetime.strptime(birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format, please enter yyyy-mm-dd")
        if not users_repo.get_by_birthdate(birthdate):
            raise ValueError("Birthdate does not exist in records")
        return users_repo.get_by_birthdate(birthdate)
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/users/accounts")
def get_user_by_account_state():
    try:
        users_repo = UserRepository(db_manager)
        account = request.form.get("account_state")
        if "account_state" not in request.form:
            raise ValueError("Missing account state")
        elif not users_repo.get_by_account_state(account):
            raise ValueError("Account state is not valid, please enter active or inactive")
        return users_repo.get_by_account_state(account)
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


#CAR APIs

@app.route("/cars", methods=["POST"])
def register_car():
    try:    
        cars_repo = CarRepository(db_manager)
        brand = request.form.get("brand")
        model = request.form.get("model")
        year = request.form.get("year")
        state = request.form.get("state")
        if not all([brand,model,year,state]):
            raise ValueError("Please make sure you enter all the required fields")
        elif not year.isdigit() or len(year)!=4:
            raise ValueError("Invalid format for year, please enter the following format: yyyy")
        elif state not in ["Available","Rented"]:
            raise ValueError("Please make sure you enter Available or Rented on the state field")
        cars_repo.create_new_car(brand,model,year,state)
        return jsonify(message="Car has been successfully created"), 201
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/cars", methods=["PUT"])
def update_car():
    try:
        cars_repo = CarRepository(db_manager)
        car_id = request.form.get("id")
        brand = request.form.get("brand")
        model = request.form.get("model")
        year = request.form.get("year")
        state = request.form.get("state")
        if not all([car_id,brand,model,year,state]):
            raise ValueError("Please make sure you enter all the required fields")
        elif not cars_repo.get_by_id(car_id):  
            raise ValueError("Unable to update car, please check if the id field is correct or does exist")
        elif not year.isdigit() or len(year)!=4:
            raise ValueError("Invalid format for year, please enter the following format: yyyy")
        elif state not in ["Available","Rented"]:
            raise ValueError("Please make sure you enter Available or Rented on the state field")
        cars_repo.update(car_id,brand,model,year,state)
        return jsonify(message="Car has been successfully updated"), 201
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/cars", methods=["DELETE"])
def delete_car():
    try:
        cars_repo = CarRepository(db_manager)
        car_id = request.form.get("id")
        if not cars_repo.get_by_id(car_id):  
            raise ValueError("Unable to delete car, please check if the id field is correct or does exist")
        cars_repo.delete(car_id)
        return jsonify(message="Car has been successfully deleted"), 201
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/cars")
def get_all_cars():
    try:
        cars_repo = CarRepository(db_manager)
        car_id = request.form.get("id")
        brand = request.form.get("brand")
        model = request.form.get("model")
        year = request.form.get("year")
        state = request.form.get("state")
        if not all([car_id,brand,model,year,state]):
            raise ValueError("Please make sure to enter all the required fields")
        return cars_repo.get_all_cars()
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/cars/id")
def get_car_by_id():
    try:
        cars_repo = CarRepository(db_manager)
        car_id = request.form.get("id")
        if "id" not in request.form:
            raise ValueError("id field is missing")
        elif not cars_repo.get_by_id(car_id):
            raise ValueError("ID does not exist in records")
        return cars_repo.get_by_id(car_id)
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/cars/brand")
def get_car_by_brand():
    try:
        cars_repo = CarRepository(db_manager)
        brand = request.form.get("brand")
        if "brand" not in request.form:
            raise ValueError("The brand field is missing")
        elif not cars_repo.get_by_brand(brand):
            raise ValueError("This brand does not exist in records")
        return cars_repo.get_by_brand(brand)
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/cars/model")
def get_car_by_model():
    try:
        cars_repo = CarRepository(db_manager)
        model = request.form.get("model")
        if "model" not in request.form:
            raise ValueError("The model field is missing")
        elif not cars_repo.get_by_model(model):
            raise ValueError("This model does not exist in records")
        return cars_repo.get_by_model(model)
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/cars/year")
def get_car_by_year():
    try:
        cars_repo = CarRepository(db_manager)
        year = request.form.get("year")
        if "year" not in request.form:
            raise ValueError("The year field is missing")
        elif not year.isdigit() or len(year)!=4:
            raise ValueError("Invalid format for year, please enter the following format: yyyy")
        elif not cars_repo.get_by_year(year):
            raise ValueError("This year does not exist in records")
        return cars_repo.get_by_year(year)
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/cars/state")
def get_car_by_state():
    try:
        cars_repo = CarRepository(db_manager)
        state = request.form.get("state")
        if "state" not in request.form:
            raise ValueError("The state field is missing")
        elif state not in ["Available","Rented"]:
            raise ValueError("Please make sure you enter Available or Rented on the state field")
        return cars_repo.get_by_state(state)
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


#CarXUser (Rents) APIs


@app.route("/rents", methods=["POST"])
def register_rent():
    try:    
        rents_repo = RentRepository(db_manager)
        user_id = request.form.get("userid")
        car_id = request.form.get("carid")
        state = request.form.get("state")
        date = request.form.get("rent_date")
        if not all([user_id,car_id,date,state]):
            raise ValueError("Please make sure you enter all the required fields")
        elif not car_id.isdigit() or not user_id.isdigit():
            raise ValueError("Please enter a number value only in carid and userid fields")
        elif state not in ["Completed","Ongoing","Denied","Pending","Unavailable"]:
            raise ValueError("Please make sure you enter Completed, Ongoing, Denied, Pending or Unavailable on the state field")
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
                raise ValueError("Invalid date format, please enter yyyy-mm-dd")
        rents_repo.create_new_rent(user_id,car_id,date,state)
        return jsonify(message="Rent has been successfully created"), 201
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/rents", methods=["PUT"])
def update_rent():
    try:
        rents_repo = RentRepository(db_manager)
        rent_id = request.form.get("id")
        user_id = request.form.get("userid")
        car_id = request.form.get("carid")
        state = request.form.get("state")
        date = request.form.get("rent_date")
        if not all([rent_id,user_id,car_id,date,state]):
            raise ValueError("Please make sure you enter all the required fields")
        elif not rents_repo.get_by_id(rent_id):  
            raise ValueError("Unable to update rent, please check if the id field is correct or does exist")
        elif not car_id.isdigit() or not user_id.isdigit():
            raise ValueError("Please enter a number value only in carid and userid fields")
        elif state not in ["Completed","Ongoing","Denied","Pending","Unavailable"]:
            raise ValueError("Please make sure you enter Completed, Ongoing, Denied, Pending or Unavailable on the state field")
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
                raise ValueError("Invalid date format, please enter yyyy-mm-dd")
        rents_repo.update(rent_id,user_id,car_id,date,state)
        return jsonify(message="Rent has been successfully updated"), 201
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/rents", methods=["DELETE"])
def delete_rent():
    try:
        rents_repo = RentRepository(db_manager)
        rent_id = request.form.get("id")
        if not rents_repo.get_by_id(rent_id):  
            raise ValueError("Unable to delete rent, please check if the id field is correct or does exist")
        rents_repo.delete(rent_id)
        return jsonify(message="Rent has been successfully deleted"), 201
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/rents")
def get_all_rents():
    try:
        rents_repo = RentRepository(db_manager)
        rent_id = request.form.get("id")
        user_id = request.form.get("userid")
        car_id = request.form.get("carid")
        state = request.form.get("state")
        rent_date = request.form.get("rent_date")
        if not all([rent_id,user_id,car_id,rent_date,state]):
            raise ValueError("Please make sure to enter all the required fields")
        return rents_repo.get_all_rents()
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/rents/id")
def get_rent_by_id():
    try:
        rents_repo = RentRepository(db_manager)
        rent_id = request.form.get("id")
        if "id" not in request.form:
            raise ValueError("id field is missing")
        elif not rents_repo.get_by_id(rent_id):
            raise ValueError("ID does not exist in records")
        return rents_repo.get_by_id(rent_id)
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/rents/userid")
def get_rent_by_user_id():
    try:
        rents_repo = RentRepository(db_manager)
        userid = request.form.get("userid")
        if "userid" not in request.form:
            raise ValueError("userid field is missing")
        elif not userid.isdigit():
            raise ValueError("Please enter a number value only in the userid field")
        elif not rents_repo.get_by_user_id(userid):
            raise ValueError("User ID does not exist in records")
        return rents_repo.get_by_user_id(userid)
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/rents/carid")
def get_rent_by_car_id():
    try:
        rents_repo = RentRepository(db_manager)
        carid = request.form.get("carid")
        if "carid" not in request.form:
            raise ValueError("Car id field is missing")
        elif not carid.isdigit():
            raise ValueError("Please enter a number value only in the carid field")
        elif not rents_repo.get_by_car_id(carid):
            raise ValueError("Car id does not exist in records")
        return rents_repo.get_by_car_id(carid)
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/rents/rentdate")
def get_rent_by_rent_date():
    try:
        rents_repo = RentRepository(db_manager)
        date = request.form.get("rent_date")
        if "rent_date" not in request.form:
            raise ValueError("Rent date field is missing")
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
                raise ValueError("Invalid date format, please enter yyyy-mm-dd")
        if not rents_repo.get_by_rent_date(date):
            raise ValueError("Rent date does not exist in records")
        return rents_repo.get_by_rent_date(date)
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/rents/state")
def get_rent_by_state():
    try:
        rents_repo = RentRepository(db_manager)
        state = request.form.get("state")
        if "state" not in request.form:
            raise ValueError("Rent state field is missing")
        elif state not in ["Completed","Ongoing","Denied","Pending","Unavailable"]:
            raise ValueError("Please make sure you enter Completed, Ongoing, Denied, Pending or Unavailable on the state field")
        elif not rents_repo.get_by_rent_state(state):
            raise ValueError("Rent state does not exist in records")
        return rents_repo.get_by_rent_state(state)
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


if __name__ == "__main__":
    app.run(host="localhost", debug=True)