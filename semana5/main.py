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


@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
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
        users_repo.update(user_id,name,username,email,password,birthdate,account_state)
        return jsonify(message="User has been successfully updated"), 201
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        users_repo = UserRepository(db_manager)
        if not users_repo.get_by_id(user_id):  
            raise ValueError("Unable to delete user, please check if id field is correct or does exist")
        users_repo.delete(user_id)
        return jsonify(message="User has been successfully deleted"), 201
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/users")
def get_users():
    try:
        users_repo = UserRepository(db_manager)
        filtered_shows = users_repo.get_all_users()
        if request.args.get("id"):
            if not users_repo.get_by_id(request.args.get("id")):
                raise ValueError(f"This id:{request.args.get("id")}, does not exist in records")
            filtered_shows = users_repo.get_by_id(request.args.get("id"))

        elif request.args.get("name"):
            if not users_repo.get_by_name(request.args.get("name")):
                raise ValueError(f"This name:{request.args.get("name")}, does not exist in records")
            filtered_shows = users_repo.get_by_name(request.args.get("name"))

        elif request.args.get("username"):
            if not users_repo.get_by_username(request.args.get("username")):
                raise ValueError(f"This username:{request.args.get("username")}, does not exist in records")
            filtered_shows = users_repo.get_by_username(request.args.get("username"))

        elif request.args.get("email"):
            if '@' not in request.args.get("email"):
                raise ValueError(f"This email:{request.args.get("email")}, does not include '@'")
            if not users_repo.get_by_email(request.args.get("email")):
                raise ValueError(f"This email:{request.args.get("email")}, does not exist in records")
            filtered_shows = users_repo.get_by_email(request.args.get("email"))

        elif request.args.get("password"):
            if not users_repo.get_by_password(request.args.get("password")):
                raise ValueError(f"This password:{request.args.get("password")}, does not exist in records")
            filtered_shows = users_repo.get_by_password(request.args.get("password"))
            
        elif request.args.get("birthdate"):
            try:
                datetime.strptime(request.args.get("birthdate"), "%Y-%m-%d")
            except ValueError:
                raise ValueError("Invalid date format, please enter yyyy-mm-dd")
            if not users_repo.get_by_birthdate(request.args.get("birthdate")):
                raise ValueError(f"This birthdate:{request.args.get("birthdate")}, does not exist in records")
            filtered_shows = users_repo.get_by_birthdate(request.args.get("birthdate"))

        elif request.args.get("account_state"):
            if not users_repo.get_by_account_state(request.args.get("account_state")):
                raise ValueError(f"This account state:{request.args.get("account_state")}, does not exist in records")
            filtered_shows = users_repo.get_by_account_state(request.args.get("account_state"))
        return filtered_shows
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


@app.route("/cars/<car_id>", methods=["PUT"])
def update_car(car_id):
    try:
        cars_repo = CarRepository(db_manager)
        brand = request.form.get("brand")
        model = request.form.get("model")
        year = request.form.get("year")
        state = request.form.get("state")
        if not all([brand,model,year,state]):
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


@app.route("/cars/<car_id>", methods=["DELETE"])
def delete_car(car_id):
    try:
        cars_repo = CarRepository(db_manager)
        if not cars_repo.get_by_id(car_id):  
            raise ValueError("Unable to delete car, please check if the id field is correct or does exist")
        cars_repo.delete(car_id)
        return jsonify(message="Car has been successfully deleted"), 201
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/cars")
def get_cars():
    try:
        cars_repo = CarRepository(db_manager)
        filtered_shows = cars_repo.get_all_cars()
        if request.args.get("id"):
            if not cars_repo.get_by_id(request.args.get("id")):
                raise ValueError(f"This id:{request.args.get("id")}, does not exist in records")
            filtered_shows = cars_repo.get_by_id(request.args.get("id"))

        elif request.args.get("brand"):
            if not cars_repo.get_by_brand(request.args.get("brand")):
                raise ValueError(f"This brand:{request.args.get("brand")}, does not exist in records")
            filtered_shows = cars_repo.get_by_brand(request.args.get("brand"))

        elif request.args.get("model"):
            if not cars_repo.get_by_model(request.args.get("model")):
                raise ValueError(f"This model:{request.args.get("model")}, does not exist in records")
            filtered_shows = cars_repo.get_by_model(request.args.get("model"))

        elif request.args.get("year"):
            if not request.args.get("year").isdigit() or len(request.args.get("year"))!=4:
                raise ValueError("Invalid format for year, please enter the following format: yyyy")
            elif not cars_repo.get_by_year(request.args.get("year")):
                raise ValueError(f"This year:{request.args.get("year")}, does not exist in records")
            filtered_shows = cars_repo.get_by_year(request.args.get("year"))
        
        elif request.args.get("state"):
            if not cars_repo.get_by_state(request.args.get("state")):
                raise ValueError(f"This state:{request.args.get("state")}, does not exist in records, please enter Available, Rented or Unavailable")
            filtered_shows = cars_repo.get_by_state(request.args.get("state"))
        return filtered_shows
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


@app.route("/rents/<rent_id>", methods=["PUT"])
def update_rent(rent_id):
    try:
        rents_repo = RentRepository(db_manager)
        user_id = request.form.get("userid")
        car_id = request.form.get("carid")
        state = request.form.get("state")
        date = request.form.get("rent_date")
        if not all([user_id,car_id,date,state]):
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


@app.route("/rents/<rent_id>", methods=["DELETE"])
def delete_rent(rent_id):
    try:
        rents_repo = RentRepository(db_manager)
        if not rents_repo.get_by_id(rent_id):  
            raise ValueError("Unable to delete rent, please check if the id field is correct or does exist")
        rents_repo.delete(rent_id)
        return jsonify(message="Rent has been successfully deleted"), 201
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


@app.route("/rents")
def get_rents():
    try:
        rents_repo = RentRepository(db_manager)
        filtered_shows = rents_repo.get_all_rents()

        if request.args.get("id"):
                if not rents_repo.get_by_id(request.args.get("id")):
                    raise ValueError(f"This id:{request.args.get("id")}, does not exist in records")
                filtered_shows = rents_repo.get_by_id(request.args.get("id"))
        
        elif request.args.get("userid"):
                if not rents_repo.get_by_user_id(request.args.get("userid")):
                    raise ValueError(f"This user id:{request.args.get("userid")}, does not exist in records")
                filtered_shows = rents_repo.get_by_user_id(request.args.get("userid"))
        
        elif request.args.get("carid"):
                if not rents_repo.get_by_car_id(request.args.get("carid")):
                    raise ValueError(f"This car id:{request.args.get("carid")}, does not exist in records")
                filtered_shows = rents_repo.get_by_car_id(request.args.get("carid"))

        elif request.args.get("state"):
                if not rents_repo.get_by_rent_state(request.args.get("state")):
                    raise ValueError(f"This state:{request.args.get("state")}, does not exist in records")
                filtered_shows = rents_repo.get_by_rent_state(request.args.get("state"))

        elif request.args.get("rent_date"):
                try:
                    datetime.strptime(request.args.get("rent_date"), "%Y-%m-%d")
                except ValueError:
                    raise ValueError("Invalid date format, please enter yyyy-mm-dd")
                if not rents_repo.get_by_rent_date(request.args.get("rent_date")):
                    raise ValueError(f"This rent date:{request.args.get("rent_date")}, does not exist in records")
                filtered_shows = rents_repo.get_by_rent_date(request.args.get("rent_date"))
        return filtered_shows
    except ValueError as err:
        return jsonify(message=str(err)), 400
    except Exception as err:
        return jsonify(message=str(err)), 500


if __name__ == "__main__":
    app.run(host="localhost", debug=True)