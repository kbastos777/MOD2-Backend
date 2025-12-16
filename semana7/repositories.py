from sqlalchemy import insert, select, update, delete, join, func
from db import DB_Manager,engine

db_manager = DB_Manager()

class RolesRepository:
    def __init__(self):
        self.engine = engine


    def insert_role(self, role_name):
        stmt = insert(db_manager.role_table).returning(db_manager.role_table.c.id).values(role_name=role_name)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]


    def get_role_by_id(self, role_id):
        stmt = select(db_manager.role_table).where(db_manager.role_table.c.id == role_id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            role = result.fetchone()
            if role is None:
                return None
            else:
                return role

class UsersRepository:

    def __init__(self):
        self.engine = engine


    def insert_user(self, username, role, password):
        with self.engine.connect() as conn:
            stmt = insert(db_manager.user_table).returning(db_manager.user_table.c.id).values(username=username, role=role, password=password)
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]


    def get_user(self, username, password):
        stmt = select(db_manager.user_table).where(db_manager.user_table.c.username == username).where(db_manager.user_table.c.password == password)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()

            if(len(users)==0):
                return None
            else:
                return users[0]


    def get_user_by_username(self, username):
        stmt = select(db_manager.user_table).where(db_manager.user_table.c.username == username)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            user = result.fetchone()

            if user is None:
                return None
            else:
                return {
                    "id": user.id,
                    "username": user.username,
                    "role": user.role,
                    "password": user.password
                }


    def get_user_by_id(self, user_id):
        stmt = select(
            db_manager.user_table
        ).where(db_manager.user_table.c.id == user_id)

        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            user = result.fetchone()

            if user is None:
                return None
            else:
                return {
                    "id": user.id,
                    "username": user.username,
                    "role": user.role,
                    "password": user.password
                }

class FruitsRepository:

    def __init__(self):
        self.engine = engine

    def insert_fruit(self, name, price, entry_date, quantity):
        stmt = insert(db_manager.fruit_table).returning(db_manager.fruit_table.c.id).values(name=name, price=price,entry_date=entry_date, quantity=quantity)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]


    def get_fruit(self, name, price, entry_date, quantity):
        stmt = select(db_manager.fruit_table).where(db_manager.fruit_table.c.name == name).where(db_manager.fruit_table.c.price == price).where(db_manager.fruit_table.c.entry_date == entry_date).where(db_manager.fruit_table.c.quantity == quantity)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            fruits = result.all()

            if(len(fruits)==0):
                return None
            else:
                return fruits[0]


    def get_fruit_by_id(self, fruit_id):
        stmt = select(
            db_manager.fruit_table
        ).where(db_manager.fruit_table.c.id == fruit_id)

        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            fruit = result.fetchone()

            if fruit is None:
                return None
            else:
                return {
                    "id": fruit.id,
                    "name": fruit.name,
                    "price": fruit.price,
                    "entry_date": fruit.entry_date,
                    "quantity": fruit.quantity
                }



    def update_fruit(self, fruit_id, name, price, entry_date, quantity):
        stmt = update(db_manager.fruit_table).where(
            db_manager.fruit_table.c.id == fruit_id
        ).values(
            name=name,
            price=price,
            entry_date=entry_date,
            quantity=quantity
        ).returning(db_manager.fruit_table.c.id)

        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()

        return result.fetchone()



    def delete_fruit(self,fruit_id):
        stmt = delete(db_manager.fruit_table).where(db_manager.fruit_table.c.id == fruit_id).returning(db_manager.fruit_table.c.id) 
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.fetchone()


class BillsRepository:

    def __init__(self):
        self.engine = engine

    def insert_bill(self):
        stmt = insert(db_manager.bill_table).returning(db_manager.bill_table.c.id).values(total=0.0)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]


    def get_bill(self,total):
        stmt = select(db_manager.bill_table).where(db_manager.bill_table.c.total == total)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            bills = result.all()

            if(len(bills)==0):
                return None
            else:
                return bills[0]


    def get_bill_by_id(self, bill_id):
        stmt = select(
            db_manager.bill_table
        ).where(db_manager.bill_table.c.id == bill_id)

        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            bill = result.fetchone()

            if bill is None:
                return None
            else:
                return {
                    "id": bill.id,
                    "total":bill.total,
                }

    def update_bill(self,total):
        stmt = update(db_manager.bill_table).where(db_manager.bill_table.c.total == "uva").values(total=total)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]


class BillsXfruitsRepository:

    def __init__(self):
        self.engine = engine

    def insert_bill_x_fruit(self, fruit_id, user_id, bill_id):
        with self.engine.connect() as conn:
            
            stmt = insert(db_manager.bill_and_fruit_table).returning(db_manager.bill_and_fruit_table.c.id).values(
                fruit_id=fruit_id,
                user_id=user_id,
                bill_id=bill_id
            )
            result = conn.execute(stmt)
            
            
            fruit_stmt = select(db_manager.fruit_table.c.price).where(db_manager.fruit_table.c.id == fruit_id)
            fruit_result = conn.execute(fruit_stmt).fetchone()
            
            if fruit_result is None:
                conn.rollback()
                raise ValueError("There is no fruit with such id.")

            fruit_price = fruit_result.price
            print(f"Fruit price in this case is:{fruit_price}")

            
            update_bill_total_stmt = update(db_manager.bill_table).where(
                db_manager.bill_table.c.id == bill_id
            ).values(
                total=db_manager.bill_table.c.total + fruit_price
            )

            update_fruit_quantity_stmt = update(db_manager.fruit_table).where(
                db_manager.fruit_table.c.id == fruit_id
            ).values(
                quantity=db_manager.fruit_table.c.quantity - 1
            )

            conn.execute(update_bill_total_stmt)
            conn.execute(update_fruit_quantity_stmt)

            conn.commit()
            
        return result.all()[0]


    def get_bills_by_user_id(self, user_id):
        
        join_stmt = db_manager.bill_and_fruit_table.join(
            db_manager.fruit_table,
            db_manager.bill_and_fruit_table.c.fruit_id == db_manager.fruit_table.c.id
        ).join(
            db_manager.bill_table,
            db_manager.bill_and_fruit_table.c.bill_id == db_manager.bill_table.c.id
        ).join(
            db_manager.user_table,
            db_manager.bill_and_fruit_table.c.user_id == db_manager.user_table.c.id
        )

        
        stmt = select(
            db_manager.bill_and_fruit_table.c.bill_id,
            db_manager.user_table.c.username,
            db_manager.user_table.c.id.label("user_id"),
            db_manager.fruit_table.c.name,
            db_manager.fruit_table.c.price,
            db_manager.bill_table.c.total
        ).select_from(join_stmt).where(
            db_manager.bill_and_fruit_table.c.user_id == user_id
        )

        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            rows = result.fetchall()

            if not rows:
                return []

            bills_by_id = {}
            username = rows[0].username
            user_id = rows[0].user_id

            for row in rows:
                bill_id = row.bill_id

                if bill_id not in bills_by_id:
                    bills_by_id[bill_id] = {
                        "bill_id": bill_id,
                        "total": row.total,
                        "products": []
                    }

                bills_by_id[bill_id]["products"].append({
                    "product_name": row.name,
                    "price": row.price
                })

            return {
            "username": username,
            "user_id": user_id,
            "bills": list(bills_by_id.values())
        }

class ContactsRepository:

    def __init__(self):
        self.engine = engine


    def insert_contact(self, user_id, name, phone_number, email):
        stmt = insert(db_manager.contacts_table).returning(db_manager.contacts_table.c.id).values(
            user_id=user_id,
            name=name,
            phone_number=phone_number,
            email=email
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]
    

    def get_contact_by_id(self, contact_id):
        stmt = select(db_manager.contacts_table).where(
            db_manager.contacts_table.c.id == contact_id
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt).fetchone()
            return result

    def get_contacts_by_user_id(self, user_id):

        join_stmt = db_manager.contacts_table.join(
                    db_manager.user_table,
                    db_manager.contacts_table.c.user_id == db_manager.user_table.c.id
                )

        stmt = select(
            db_manager.contacts_table,
            db_manager.user_table.c.username
        ).select_from(join_stmt).where(db_manager.contacts_table.c.user_id == user_id)

        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            rows = result.fetchall()

            if not rows:
                return []

            contacts_by_user_id = {}
            username = rows[0].username
            user_id = rows[0].user_id

            for row in rows:
                contact_id = row.id

                if contact_id not in contacts_by_user_id:
                    contacts_by_user_id[contact_id] = {
                        "name": row.name,
                        "email": row.email,
                        "phone_number": row.phone_number
                    }
                    
            return {
            "username": username,
            "user_id": user_id,
            "List of contacts": list(contacts_by_user_id.values())
        }


    def get_all_contacts(self):# This is for admin use only

        join_stmt = db_manager.contacts_table.join(
                    db_manager.user_table,
                    db_manager.contacts_table.c.user_id == db_manager.user_table.c.id
                )

        stmt = select(
            db_manager.contacts_table,
            db_manager.user_table.c.username
        ).select_from(join_stmt)

        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            rows = result.fetchall()

            if not rows:
                return []

            contacts_by_id = {}

            for row in rows:
                contact_id = row.id

                if contact_id not in contacts_by_id:
                    contacts_by_id[contact_id] = {
                        "contact_owner": row.username,
                        "user_id": row.user_id,
                        "contact": {}
                    }

                contacts_by_id[contact_id]["contact"] = {
                    "name": row.name,
                    "email": row.email,
                    "phone_number":row.phone_number
                }

            return {
            "Contacts_list": list(contacts_by_id.values())
        }


    def update_contact(self, contact_id, name, phone_number, email):
        stmt = update(db_manager.contacts_table).where(
            db_manager.contacts_table.c.id == contact_id
        ).values(
            name=name,
            phone_number=phone_number,
            email=email
        ).returning(db_manager.contacts_table.c.id)

        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()

        return result.fetchone()


    def delete_contact(self, contact_id):
        stmt = delete(db_manager.contacts_table).where(db_manager.contacts_table.c.id == contact_id).returning(db_manager.contacts_table.c.id) 
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.fetchone()


class LoginHistoryRepository:
    def __init__(self):
        self.engine = engine

    def insert_login_history(self, user_id ,ip, successful_login):
        stmt = insert(db_manager.login_history_table).returning(db_manager.login_history_table.c.id).values(
            user_id=user_id,
            login_date=func.now(),
            ip=ip,
            successful_login=successful_login
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.fetchone()

    def get_login_history_by_user_id(self, user_id):
        stmt = select(db_manager.login_history_table).where(db_manager.login_history_table.c.user_id == user_id).order_by(db_manager.login_history_table.c.login_date.desc())
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            rows = result.fetchall()
            if not rows:
                return []
            history = []
            for row in rows:
                history.append({
                    "id": row.id,
                    "user_id": row.user_id,
                    "login_date": row.login_date.isoformat() if row.login_date is not None else None,
                    "ip": row.ip,
                    "successful_login": row.successful_login
                })
            return history