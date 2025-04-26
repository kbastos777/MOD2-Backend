SET search_path TO transactions;


CREATE TABLE IF NOT EXISTS Users
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(30) NOT NULL,
    username VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL,
    PRIMARY KEY (id)
);


ALTER TABLE IF EXISTS Users
    OWNER to postgres;


CREATE TABLE IF NOT EXISTS Product
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(30) NOT NULL,
	price decimal NOT NULL,
    PRIMARY KEY (id)
);


ALTER TABLE IF EXISTS Product
    OWNER to postgres;


CREATE TABLE IF NOT EXISTS Bill
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
	customerid integer NOT NULL,
	product_id integer NOT NULL,
	state VARCHAR(30) NOT NULL,
    PRIMARY KEY (id)
);


ALTER TABLE IF EXISTS Bill
    OWNER to postgres;


CREATE TABLE IF NOT EXISTS Inventory
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
	product_id integer  UNIQUE REFERENCES Product(id) NOT NULL ,
	quantity int NOT NULL,
    PRIMARY KEY (id)
);


ALTER TABLE IF EXISTS Inventory
    OWNER to postgres;




INSERT INTO Users(name, username, email) 
VALUES
('Juan Pérez', 'juanperez', 'juanperez@gmail.com'),
('Ana Gómez', 'anagomez', 'anagomez@gmail.com'),
('Carlos López', 'carloslopez', 'carloslopez@gmail.com'),
('Maria Fernández', 'mariafernandez', 'mariafernandez@gmail.com'),
('Luis García', 'luisgarcia', 'luisgarcia@gmail.com'),
('Elena Martínez', 'elenamartinez', 'elenamartinez@gmail.com'),
('David Sánchez', 'davidsanchez', 'davidsanchez@gmail.com'),
('Paula Rodríguez', 'paularodriguez', 'paularodriguez@gmail.com'),
('José Herrera', 'joseherrera', 'joseherrera@gmail.com'),
('Laura Jiménez', 'laurajimenez', 'laurajimenez@gmail.com'),
('Antonio Morales', 'antoniomorales', 'antoniomorales@gmail.com'),
('Sofia Ruiz', 'sofiaruiz', 'sofiaruiz@gmail.com'),
('Pedro Fernández', 'pedrofernandez', 'pedrofernandez@gmail.com'),
('Carmen González', 'carmengonzalez', 'carmengonzalez@gmail.com'),
('Ricardo Pérez', 'ricardoperez', 'ricardoperez@gmail.com'),
('María Ruiz', 'mariaruiz', 'mariaruiz@gmail.com'),
('Miguel Díaz', 'migueldiaz', 'migueldiaz@gmail.com'),
('Isabel Martín', 'isabelmartin', 'isabelmartin@gmail.com'),
('Juan Martínez', 'juanmartinez', 'juanmartinez@gmail.com'),
('Adriana Rodríguez', 'adrianarodriguez', 'adrianarodriguez@gmail.com'),
('Javier Torres', 'javiertorres', 'javiertorres@gmail.com'),
('Rosa González', 'rosagonzalez', 'rosagonzalez@gmail.com'),
('Ricardo García', 'ricardogarcia', 'ricardogarcia@gmail.com'),
('Luis Rodríguez', 'luisrodriguez', 'luisrodriguez@gmail.com'),
('Ángel Jiménez', 'angeljimenez', 'angeljimenez@gmail.com'),
('Ana Díaz', 'anadiaz', 'anadiaz@gmail.com'),
('David Gómez', 'davidgomez', 'davidgomez@gmail.com'),
('Pilar López', 'pilarlopez', 'pilarlopez@gmail.com'),
('Sergio Martínez', 'sergiomartinez', 'sergiomartinez@gmail.com'),
('Clara Sánchez', 'clarasanchez', 'clarasanchez@gmail.com'),
('Felipe Pérez', 'felipeperez', 'felipeperez@gmail.com'),
('Jorge Ruiz', 'jorgeruiz', 'jorgeruiz@gmail.com'),
('Berta Fernández', 'bertafernandez', 'bertafernandez@gmail.com'),
('Raúl Rodríguez', 'raulrodriguez', 'raulrodriguez@gmail.com'),
('Marta López', 'martalopez', 'martalopez@gmail.com'),
('Antonio Pérez', 'antonioperez', 'antonioperez@gmail.com'),
('Beatriz González', 'beatrizgonzalez', 'beatrizgonzalez@gmail.com'),
('Luis Díaz', 'luisdiaz', 'luisdiaz@gmail.com'),
('José López', 'joselopez', 'joselopez@gmail.com'),
('Sandra Martínez', 'sandramartinez', 'sandramartinez@gmail.com'),
('Vicente García', 'vicentegarcia', 'vicentegarcia@gmail.com'),
('Sonia Torres', 'soniatorres', 'soniatorres@gmail.com'),
('Juan Jiménez', 'juanjimenez', 'juanjimenez@gmail.com'),
('Eva Fernández', 'evafernandez', 'evafernandez@gmail.com'),
('Raquel Ruiz', 'raquelruiz', 'raquelruiz@gmail.com'),
('Enrique López', 'enriquelopez', 'enriquelopez@gmail.com'),
('Alberto Pérez', 'albertoperez', 'albertoperez@gmail.com'),
('Mónica Rodríguez', 'monicarodriguez', 'monicarodriguez@gmail.com'),
('Carlos Martínez', 'carlosmartinez', 'carlosmartinez@gmail.com'),
('Gloria Sánchez', 'gloriasanchez', 'gloriasanchez@gmail.com');


INSERT INTO Product (name, price) VALUES
('Lenovo Laptop', 500.00),
('Logitech Mouse', 20.00),
('Redragon Keyboard', 30.00),
('LG 24" Monitor', 50.00),
('Samsung Smartphone', 300.00),
('iPad Tablet', 700.00),
('HP Printer', 550.00),
('Canon Camera', 600.00),
('Sony Headphones', 55.00),
('Huawei Smartwatch', 525.00),
('Gaming Chair', 250.00),
('TP-Link Router', 150.00),
('Seagate Hard Drive', 100.00),
('Kingston SSD', 200.00),
('NVIDIA Graphics Card', 1000.00),
('Corsair RAM', 540.00),
('Blue Yeti Microphone', 15.00),
('Logitech Webcam', 25.00),
('JBL Speakers', 55.00),
('Xbox Console', 600.00),
('PS5 Controller', 45.00),
('Cooling Pad', 20.00),
('Epson Projector', 1050.00),
('EVGA Power Supply', 350.00),
('ASUS Motherboard', 650.00),
('Universal Charger', 15.00),
('Mid Tower Case', 550.00),
('Solar Panel', 1000.00),
('Wi-Fi Repeater', 45.00),
('Samsung 55" TV', 1040.00);


INSERT INTO Inventory (product_id, quantity) VALUES
(1, 3),
(2, 5),
(3, 2),
(4, 4),
(5, 1),
(6, 2),
(7, 5),
(8, 3),
(9, 1),
(10, 4),
(11, 2),
(12, 5),
(13, 3),
(14, 2),
(15, 1),
(16, 4),
(17, 5),
(18, 2),
(19, 3),
(20, 1),
(21, 4),
(22, 3),
(23, 5),
(24, 1),
(25, 2),
(26, 4),
(27, 5),
(28, 3),
(29, 2),
(30, 1);




CREATE OR REPLACE PROCEDURE check_stock_and_user_availability()
AS $$
DECLARE
    stock_available INT := 0;
    user_exists INT := 0;
	bill_exists INT := 0;

BEGIN --ACA no me funciona con el key de TRANSACTION solo con BEGIN esto debido a que esta dentro de un procedure, ademas los IF statements solo me deja aplicarlos dentro de una procedure o funcion, no fuera de ellas.

		
		
		SELECT quantity INTO stock_available
		FROM Inventory
		WHERE product_id = 1;
		
		IF stock_available <= 0 THEN
		    RAISE NOTICE 'There is no stock for this product.';
		    RETURN;
		END IF;

		
		SELECT count(id) INTO user_exists
		FROM Users
		WHERE Users.id = 1
		LIMIT 1;

		
		-- Validar si existe el usuario (cliente)
		IF user_exists <= 0 THEN
		  RETURN;  -- Salir de la transacción si no existe un usuario en el resultado.
		END IF;
END;
$$ LANGUAGE plpgsql;






CREATE OR REPLACE PROCEDURE generate_new_bill()
AS $$
DECLARE
	bill_exists INT := 0;
BEGIN
		-- Si sí existe todo lo anterior, crear la factura
		INSERT INTO Bill (customerid, product_id, state) VALUES
		(10, 1, 'paid');
		
		
		-- Actualizar el inventario
		UPDATE Inventory
		SET quantity = quantity - 1
		WHERE product_id = 1;

	
		SELECT count(id) INTO bill_exists
		FROM Bill
		WHERE Bill.id = 1
		LIMIT 1;

		
		-- Validar existencia de la factura
		IF bill_exists <= 0 THEN
			RETURN;  -- Salir de la transacción si no existe la factura en el resultado.
		--ELSE
			--ROLLBACK TO SAVEPOINT checkout; Aca intente usar el rollback to savepoint en caso de que no exista tal bill id, pero al parecer no funciona dentro de una condicional IF o dentro de un procedure
		END IF;		
		
		
		UPDATE Inventory
		SET quantity = quantity + 1
		WHERE product_id = 1;

		
		UPDATE Bill
		SET state = 'returned'
		WHERE product_id = 1;

END;
$$ LANGUAGE plpgsql;

BEGIN;


CALL check_stock_and_user_availability();
SAVEPOINT checkout;
CALL generate_new_bill();


COMMIT;




SELECT * FROM Bill;