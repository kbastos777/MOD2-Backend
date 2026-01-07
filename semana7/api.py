from flask import Flask, request, Response, jsonify, g
from functools import wraps
from db import DB_Manager
from jwt_manager import JWT_Manager
from repositories import ContactsRepository, RolesRepository,UsersRepository,FruitsRepository,BillsRepository,BillsXfruitsRepository,LoginHistoryRepository

with open("private.pem", "rb") as file:
    private_key = file.read()

with open("public.pem", "rb") as file:
    public_key = file.read()

app = Flask("user-service")
db_manager = DB_Manager()
jwt_manager = JWT_Manager(private_key=private_key, public_key=public_key, algorithm="RS256")

def _get_auth():
    token = request.headers.get('Authorization')
    if not token:
        return None, Response("Missing token", status=403)
    token = token.replace("Bearer ", "")
    decoded = jwt_manager.decode(token)
    if decoded is None or 'id' not in decoded:
        return None, Response("Invalid token", status=403)
    user_id = decoded['id']
    user_repo = UsersRepository()
    user = user_repo.get_user_by_id(user_id)
    if user is None:
        return None, Response("User not found", status=404)
    role_repo = RolesRepository()
    role = role_repo.get_role_by_id(user['role'])
    return (user, role, user_id), None

def auth_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth, err = _get_auth()
        if err:
            return err
        user, role, user_id = auth
        g.current_user = user
        g.current_role = role
        g.current_user_id = user_id
        return f(*args, **kwargs)
    return wrapper

def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth, err = _get_auth()
        if err:
            return err
        user, role, user_id = auth
        if role is None or role.role_name.lower() != "admin":
            return Response("You are not authorized to perform this action", status=403)
        g.current_user = user
        g.current_role = role
        g.current_user_id = user_id
        return f(*args, **kwargs)
    return wrapper

def admin_or_user_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth, err = _get_auth()
        if err:
            return err
        user, role, user_id = auth
        if role is None or (role.role_name.lower() != "admin" and role.role_name.lower() != "user"):
            return Response("You are not authorized to perform this action", status=403)
        g.current_user = user
        g.current_role = role
        g.current_user_id = user_id
        return f(*args, **kwargs)
    return wrapper

@app.route("/liveness")
def liveness():
    return "<p>Hello, World!</p>"

# CREATE ROLES

@app.route('/register_role', methods=['POST']) #Before running enter the admin and users roles directly using PostgreSQL
@admin_required
def create_roles():
    try:
        data = request.get_json()
        if data.get('role_name') is None:
            return Response("You must provide a role name", status=400)

        role_repo = RolesRepository()
        result = role_repo.insert_role(data.get('role_name'))
        role_id = result[0]
        
        access_token = jwt_manager.encode({'id': role_id})
        refresh_token = jwt_manager.encode_refresh({'id': role_id})

        return jsonify(access_token=access_token, refresh_token=refresh_token)
    except Exception as e:
        print("Error:", e)
        return Response("Internal server error", status=500)

# CREATE USERS

@app.route('/register_user', methods=['POST'])
def create_user():
    data = request.get_json()
    if None in(data.get('username'), data.get('role'), data.get('password')):
        return Response("You must provide a username, role and password",status=400)
    else:
        user_repo = UsersRepository()
        result = user_repo.insert_user(data.get('username'), data.get('role'), data.get('password'))
        user_id = result[0]

        
        access_token = jwt_manager.encode({'id': user_id})
        refresh_token = jwt_manager.encode_refresh({'id': user_id})

        return jsonify(access_token=access_token, refresh_token=refresh_token)

# READ USER BY ID

@app.route('/find_user_by_id', methods=['GET'])
@admin_required
def find_user_by_id():
    try:
        data = request.get_json()
        user_id = data.get('id')

        if not user_id:
            return Response("You must provide a user id", status=400)

        user_repo = UsersRepository()
        result = user_repo.get_user_by_id(user_id)

        token = jwt_manager.encode({'id':user_id})

        if result is None:
            return Response("User not found", status=404)

        return jsonify(token=token)
    except Exception as e:
        print("Error:", e)
        return Response("Internal server error", status=500)

# CREATE FRUITS

@app.route('/register_fruit', methods=['POST'])
@admin_or_user_required
def create_fruit():
    try:
        data = request.get_json()
        if None in (data.get('name'), data.get('price'), data.get('entry_date'), data.get('quantity')):
            return Response("You must provide a name, price, entry_date and quantity", status=400)
        else:
            fruit_repo = FruitsRepository()
            result = fruit_repo.insert_fruit(data.get('name'), data.get('price'), data.get('entry_date'), data.get('quantity'))
            fruit_id = result[0]

            access_token = jwt_manager.encode({'id': fruit_id})
            refresh_token = jwt_manager.encode_refresh({'id': fruit_id})

            return jsonify(access_token=access_token, refresh_token=refresh_token)
    except Exception as e:
        print("Error:", e)
        return Response("Internal server error", status=500)

# FIND FRUIT BY ID
    
@app.route('/find_fruit_by_id', methods=['GET'])
@admin_required
def find_fruit_by_id():
    try:
        data = request.get_json()
        fruit_id = data.get('id')

        if not fruit_id:
            return Response("You must provide a fruit id", status=400)

        fruit_repo = FruitsRepository()
        result = fruit_repo.get_fruit_by_id(fruit_id)

        token = jwt_manager.encode({'id':fruit_id})

        if result is None:
            return Response("Fruit not found", status=404)

        return jsonify(token=token)
    except Exception as e:
        print("Error:", e)
        return Response("Internal server error", status=500)

# UPDATE FRUIT

@app.route('/update_fruit', methods=['PUT'])
@admin_required
def update_fruit():
    try:
        data = request.get_json()
        if None in (data.get('id'), data.get('name'), data.get('price'), data.get('entry_date'), data.get('quantity')):
            return Response("You must provide a name, price, entry_date and quantity", status=400)
        else:
            fruit_repo = FruitsRepository()
            result = fruit_repo.update_fruit(data.get('id'), data.get('name'), data.get('price'), data.get('entry_date'), data.get('quantity'))
            fruit_id = result[0]

            access_token = jwt_manager.encode({'id': fruit_id})
            refresh_token = jwt_manager.encode_refresh({'id': fruit_id})

            return jsonify(access_token=access_token, refresh_token=refresh_token)
    except Exception as e:
        print("Error:", e)
        return Response("Internal server error", status=500)

# DELETE FRUIT

@app.route('/delete_fruit', methods=['DELETE'])
@admin_required
def delete_fruit():
    try:
        data = request.get_json()
        if (data.get('id') == None):
            return Response("You must provide a fruit id", status=400)
        else:
            fruit_repo = FruitsRepository()
            result = fruit_repo.delete_fruit(data.get('id'))
            fruit_id = result[0]

            access_token = jwt_manager.encode({'id': fruit_id})
            refresh_token = jwt_manager.encode_refresh({'id': fruit_id})

            return jsonify(access_token=access_token, refresh_token=refresh_token)
    except Exception as e:
        print("Error:", e)
        return Response("Internal server error", status=500)

# CREATE BILLS

@app.route('/create_bill', methods=['POST'])
@admin_or_user_required
def create_bill():
    try:
        bill_repo = BillsRepository()
        result = bill_repo.insert_bill()
        bill_id = result[0]

        access_token = jwt_manager.encode({'id': bill_id})
        refresh_token = jwt_manager.encode_refresh({'id': bill_id})

        return jsonify(access_token=access_token, refresh_token=refresh_token)
    except Exception as e:
        print("Error:", e)
        return Response("Internal server error", status=500)


# FIND BILL BY ID

@app.route('/find_bill_by_id', methods=['GET'])
@admin_or_user_required
def find_bill_by_id():
    try:
        data = request.get_json()
        bill_id = data.get('id')

        if not bill_id:
            return Response("You must provide a bill id", status=400)

        bills_repo = BillsRepository()
        result = bills_repo.get_bill_by_id(bill_id)

        token = jwt_manager.encode({'id':bill_id})

        if result is None:
            return Response("Bill not found", status=404)

        return jsonify(token=token)
    except Exception as e:
        print("Error:", e)
        return Response("Internal server error", status=500)


# CREATE BILLS AND FRUITS

@app.route('/register_bill_and_fruit', methods=['POST'])
@admin_or_user_required
def create_bill_and_fruit():
    try:
        data = request.get_json()
        if None in (data.get('fruit_id'), data.get('user_id'), data.get('bill_id')):
            return Response("You must provide a fruit id, user id and bill id", status=400)
        else:
            repo = BillsXfruitsRepository()
            try:
                result = repo.insert_bill_x_fruit(data.get('fruit_id'), data.get('user_id'), data.get('bill_id'))
                bill_and_fruit_id = result[0]

                access_token = jwt_manager.encode({'id': bill_and_fruit_id})
                refresh_token = jwt_manager.encode_refresh({'id': bill_and_fruit_id})

                return jsonify(access_token=access_token, refresh_token=refresh_token)
            except Exception as e:
                print("Error:", e)
                return Response("Internal server error", status=500)
    except Exception as e:
        print("Error:", e)
        return Response("Internal server error", status=500)

# FIND BILLS BY USER

@app.route('/find_bills_by_user_id', methods=['GET'])
@admin_or_user_required
def find_bill_by_user():
    try:
        user_id = g.current_user_id

        if not user_id:
            return Response("You must provide a user id", status=400)

        bills_repo = BillsXfruitsRepository()
        result = bills_repo.get_bills_by_user_id(user_id)

        token = jwt_manager.encode({'user_id':user_id})

        if result == []:
            return Response("Bills not found", status=404)

        return jsonify(token=token)
    except Exception as e:
        print("Error:", e)
        return Response("Internal server error", status=500)


# CREATE CONTACT

@app.route('/register_contact', methods=['POST'])
@admin_or_user_required
def create_contact():
    try:
        data = request.get_json()
        if None in (data.get('user_id'), data.get('name'), data.get('phone_number'), data.get('email')):
            return Response("You must provide a user id, name, phone number and email", status=400)
        else:
            contact_repo = ContactsRepository()
            result = contact_repo.insert_contact(data.get('user_id'), data.get('name'), data.get('phone_number'), data.get('email'))
            contact_id = result[0]

            access_token = jwt_manager.encode({'id': contact_id})
            refresh_token = jwt_manager.encode_refresh({'id': contact_id})

            return jsonify(access_token=access_token, refresh_token=refresh_token)
    except Exception as e:
        print("Error:", e)
        return Response("Internal server error", status=500)

# FIND CONTACT BY USER_ID

@app.route('/find_contacts_by_user_id', methods=['GET'])
@admin_or_user_required
def find_contact_by_user_id():
    try:
        user_id = g.current_user_id

        contact_repo = ContactsRepository()
        result = contact_repo.get_contacts_by_user_id(user_id) #For this endpoint there is no need to specify the user_id in the body in postman as this value is taken directly from the decoded information

        token = jwt_manager.encode({'id':user_id})

        if result == []:
            return Response("No contacts found", status=404)

        return jsonify(token=token)
    except Exception as e:
        print("Error:", e)
        return Response("Internal server error", status=500)


# LOGIN HISTORY (ADMIN ONLY)
@app.route('/login-history', methods=['GET'])
@admin_required
def login_history():
    try:
        data = request.get_json()
        target_user_id = data.get('user_id') if data else None

        if not target_user_id:
            return Response("You must provide an user id", status=400)

        login_repo = LoginHistoryRepository()
        history = login_repo.get_login_history_by_user_id(target_user_id)

        if history == []:
            return Response("No login history found",status=404)

        return jsonify(history=history)
    except Exception as e:
        print("Error:", e)
        return Response("Internal server error", status=500)

#DISPLAY ALL CONTACTS (FOR ADMIN USE ONLY)

@app.route('/show_all_contacts_by_user_id', methods=['GET'])
@admin_required
def get_all_contacts():
    try:
        contact_repo = ContactsRepository()
        result = contact_repo.get_all_contacts()
        token = jwt_manager.encode({'id':g.current_user_id})

        if result == []:
            return Response("No contacts found", status=404)

        return jsonify(token=token)
    except Exception as e:
        print("Error:", e)
        return Response("Internal server error", status=500)

# UPDATE CONTACT

@app.route('/edit_contact', methods=['PUT'])
@admin_or_user_required
def update_contact():
    try:
        data = request.get_json()

        if None in (data.get('id'), data.get('name'), data.get('phone_number'), data.get('email')):
            return Response("Please make sure all required fields are submitted",status=400)

        contact_repo = ContactsRepository()
        contact_id = contact_repo.get_contact_by_id(data.get('id'))

        if contact_id is None:
            return Response("Contact not found", status=404)

        if contact_id.user_id != g.current_user_id and g.current_role.role_name.lower() != "admin":
            return Response("Unable to update this contact. Not found", status=404)
        
        contact_repo.update_contact(
            contact_id=contact_id[0],
            name=data['name'],
            phone_number=data['phone_number'],
            email=data['email']
        )

        access_token = jwt_manager.encode({'id': contact_id[0]})
        refresh_token = jwt_manager.encode_refresh({'id': contact_id[0]})

        return jsonify(access_token=access_token, refresh_token=refresh_token)

    except Exception as e:
        print("Error:", e)
        return Response("Internal server error", status=500)


# DELETE CONTACT

@app.route('/remove_contact', methods=['DELETE'])
@admin_or_user_required
def delete_contact():
    try:
        data = request.get_json()
        contact_repo = ContactsRepository()
        contact_id = contact_repo.get_contact_by_id(data.get('id'))
        if contact_id is None:
            return Response("Contact not found", status=404)

        if contact_id.user_id != g.current_user_id and g.current_role.role_name.lower() != "admin":
            return Response("Unable to delete this contact. Not found", status=404)
        
        if (data.get('id') == None):
            return Response("You must provide a contact id", status=400)
        else:
            contact_repo = ContactsRepository()
            contact_repo.delete_contact(contact_id=contact_id[0])

            access_token = jwt_manager.encode({'id': contact_id[0]})
            refresh_token = jwt_manager.encode_refresh({'id': contact_id[0]})

            return jsonify(access_token=access_token, refresh_token=refresh_token)
    except Exception as e:
        print("Error:", e)
        return Response("Internal server error", status=500)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if(data.get('username') == None or data.get('password') == None):
        return Response("You must provide a username and password", status=400)
    else:
        user_repo = UsersRepository()
        result = user_repo.get_user(data.get('username'), data.get('password'))

        if(result == None):
            # record failed login attempt if username exists
            try:
                existing_user = user_repo.get_user_by_username(data.get('username'))
                if existing_user is not None:
                    login_repo = LoginHistoryRepository()
                    login_repo.insert_login_history(existing_user['id'], request.remote_addr or "", False)
            except Exception:
                pass
            return Response("Invalid credentials", status=403)
        else:
            user_id = result[0]
            # record successful login
            try:
                login_repo = LoginHistoryRepository()
                login_repo.insert_login_history(user_id, request.remote_addr or "", True)
            except Exception:
                pass

            access_token = jwt_manager.encode({'id': user_id}, expires_in_minutes=15)
            refresh_token = jwt_manager.encode_refresh({'id': user_id})

            return jsonify(access_token=access_token, refresh_token=refresh_token)

@app.route('/refresh-token', methods=['POST'])
def refresh_token():
    try:
        token = request.get_json().get("refresh_token")

        if not token:
            return Response("Missing refresh token", status=400)

        decoded = jwt_manager.decode(token)

        if decoded is None:
            return Response("Invalid refresh token", status=403)

        if decoded.get("type") != "refresh":
            return Response("Invalid token type", status=403)

        user_id = decoded['id']

        new_access_token = jwt_manager.encode({'id': user_id}, expires_in_minutes=15)

        return jsonify(access_token=new_access_token)

    except Exception as e:
        print("Error:", e)
        return Response("Internal server error", status=500)


@app.route('/me')
@auth_required
def me():
    try:
        user = g.current_user
        return jsonify(id=g.current_user_id, username=user['username'])
    except Exception as e:
        return Response("Internal server error", status=500)


if __name__ == "__main__":
    app.run(host="localhost",port=5000, debug=True)
