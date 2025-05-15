import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, bindparam, insert, delete, update, select
from sqlalchemy.schema import CreateSchema

DB_URI = 'postgresql://postgres:Bold2024@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)
metadata_obj = MetaData()
schema_name = "ORM_schema"

with engine.connect() as conn:
        conn.execute(CreateSchema(schema_name))
        print(f"schema created successfully.")
        conn.commit()

user_table = Table(
		"users",
		metadata_obj,
		Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
		Column("name", String(30), ),
        schema=schema_name
)

directions_table = Table(
		"directions",
		metadata_obj,
		Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
		Column("description", String(200), nullable=False),
        Column("user_id", ForeignKey(f"{schema_name}.users.id"), nullable=False),
        schema=schema_name
)

cars_table = Table(
		"cars",
		metadata_obj,
		Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
		Column("model", String(200), nullable=False),
        Column("user_id", ForeignKey(f"{schema_name}.users.id"), nullable=True),
        schema=schema_name
)

metadata_obj.create_all(engine) #Here, the tables will be created

with engine.connect() as conn:
    users_result = conn.execute(
        insert(user_table),
        [
            {"name": "Kevin Bastos"},
            {"name": "Natalia Chacon"},
            {"name": "Pau Rodriguez"},
            {"name": "Michael Jackson"}
        ],
    )

    directions_result = conn.execute(
        insert(directions_table),[
            {"description" : "Desamparados, San Jose", "user_id" : 1},
            {"description" : "Coyol, Alajuela", "user_id" : 3},
            {"description" : "Sabana, San Jose", "user_id" : 2},
            {"description" : "San Pablo, Heredia", "user_id" : 4},
        ],
    )

    cars_result = conn.execute(
        insert(cars_table),[
            {"model" : "Toyota", "user_id" : 1},
            {"model" : "Nissan", "user_id" : 3},
            {"model" : "Rolls-Royse","user_id":None},
            {"model" : "Ferrari", "user_id" : 4},
        ],
    )
    conn.commit()

####UPDATE####

#Users

update_users = (
    update(user_table)
    .where(user_table.c.name == bindparam("oldname"))
    .values(name=bindparam("newname"))
)
with engine.begin() as conn:
    conn.execute(
        update_users,
        [
            {"oldname": "Pau Rodriguez", "newname": "Mitchell Alvarado"},
            {"oldname": "Michael Jackson", "newname": "Cloud Strife"},
        ],
    )

#Directions

update_directions = (
    update(directions_table)
    .where(directions_table.c.description == bindparam("old_direction"))
    .values(description=bindparam("new_direction"))
)
with engine.begin() as conn:
    conn.execute(
        update_directions,
        [
            {"old_direction": "Desamparados, San Jose", "new_direction": "El Porvenir, San Jose"},
            {"old_direction": "Coyol, Alajuela", "new_direction": "Escazu, San Jose"},
        ],
    )

#Cars

update_cars = (
    update(cars_table)
    .where(cars_table.c.model == bindparam("old_car"))
    .values(model=bindparam("new_car"))
)
with engine.begin() as conn:
    conn.execute(
        update_cars,
        [
            {"old_car": "Toyota", "new_car": "Alfa Romeo"},
            {"old_car": "Nissan", "new_car": "Bugatti"},
        ],
    )

####DELETE####

#Directions
delete_direction = delete(directions_table).where(directions_table.c.description == "Escazu, San Jose")
with engine.begin() as conn:
    result = conn.execute(delete_direction)
    conn.commit()

#Cars
delete_car = delete(cars_table).where(cars_table.c.model == "Bugatti")
with engine.begin() as conn:
    result = conn.execute(delete_car)
    conn.commit()

#Users
delete_user = delete(user_table).where(user_table.c.name == "Mitchell Alvarado")
with engine.begin() as conn:
    result = conn.execute(delete_user)
    conn.commit()

####SELECT####

#Users
select_all_users = select(user_table)
with engine.begin() as conn:
    result = conn.execute(select_all_users)
    print(select_all_users)
    conn.commit()

#Cars
select_all_cars = select(cars_table)
with engine.begin() as conn:
    result = conn.execute(select_all_cars)
    print(select_all_cars)
    conn.commit()

#Directions
select_all_directions = select(cars_table)
with engine.begin() as conn:
    result = conn.execute(select_all_directions)
    print(select_all_directions)
    conn.commit()