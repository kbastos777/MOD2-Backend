from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, exc, Float, DateTime, ForeignKey,Boolean
from sqlalchemy.schema import CreateSchema

DB_URI = 'postgresql://postgres:Bold2024@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)
metadata_obj = MetaData()
schema_name = "Ejercicio_semana_7"

class DB_Manager:

    def __init__(self):
        self.engine = engine
        self.schema_name = schema_name
        self.metadata_obj = metadata_obj
        with self.engine.connect() as conn:
            try:
                conn.execute(CreateSchema(self.schema_name))
                print(f"Schema '{self.schema_name}' created successfully.")
                conn.commit()
            except exc.ProgrammingError as e:
                if 'already exists' in str(e):#This in case the schema already exists
                    print(f"Schema '{self.schema_name}' already exists. Continuing.")
                    conn.rollback()
                else:
                    raise

        self.role_table = Table(
        "Roles",
        self.metadata_obj,
        Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
        Column("role_name", String(10), nullable=False),
        schema=self.schema_name,
        extend_existing=True
        )

        self.user_table = Table(
            "Users",
            self.metadata_obj,
            Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
            Column("username", String(10), nullable=False),
            Column("role", ForeignKey(f"{self.schema_name}.Roles.id"), nullable=False),
            Column("password", String(10), nullable=False),
            schema=self.schema_name,
            extend_existing=True
        )

        self.fruit_table = Table(
            "Fruits",
            self.metadata_obj,
            Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
            Column("name", String(30), nullable=False),
            Column("price", Float, nullable=False),
            Column("entry_date", DateTime(timezone=True), nullable=False),
            Column("quantity", Integer, nullable=False),
            schema=self.schema_name,
            extend_existing=True
        )

        self.bill_table = Table(
            "Bills",
            self.metadata_obj,
            Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
            Column("total", Float, nullable=False),
            schema=self.schema_name,
            extend_existing=True
        )

        self.bill_and_fruit_table = Table(
            "BillsXFruits",
            self.metadata_obj,
            Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
            Column("fruit_id", ForeignKey(f"{self.schema_name}.Fruits.id"), nullable=False),
            Column("user_id", ForeignKey(f"{self.schema_name}.Users.id"), nullable=False),
            Column("bill_id", ForeignKey(f"{self.schema_name}.Bills.id"), nullable=False),
            schema=self.schema_name,
            extend_existing=True
        )

        self.contacts_table = Table(
            "Contacts",
            self.metadata_obj,
            Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
            Column("user_id", ForeignKey(f"{self.schema_name}.Users.id"), nullable=False),
            Column("name", String(30), nullable=False),
            Column("phone_number", String(12), nullable=False),
            Column("email", String(30), nullable=False),
            schema=self.schema_name,
            extend_existing=True
        )

        self.login_history_table = Table(
            "LoginHistory",
            self.metadata_obj,
            Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
            Column("user_id", ForeignKey(f"{self.schema_name}.Users.id"), nullable=False),
            Column("login_date", DateTime(timezone=True), nullable=False),
            Column("ip", String(15), nullable=False),
            Column("successful_login", Boolean, nullable=False),
            schema=self.schema_name,
            extend_existing=True
        )
        self.metadata_obj.create_all(self.engine)
