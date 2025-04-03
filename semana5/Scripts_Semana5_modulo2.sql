SET search_path TO lyfter_car_rental;

CREATE TABLE IF NOT EXISTS Users
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(30) NOT NULL,
    username VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL,
    password VARCHAR(12) NOT NULL,
    birthdate date NOT NULL,
    account_state VARCHAR(8) NOT NULL,
    PRIMARY KEY (id)
);


ALTER TABLE IF EXISTS Users
    OWNER to postgres;
	

CREATE TABLE IF NOT EXISTS Cars
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    brand VARCHAR(15),
    model VARCHAR(15) NOT NULL,
    year integer NOT NULL,
    state VARCHAR(10) NOT NULL,
    PRIMARY KEY (id)
);


ALTER TABLE IF EXISTS Cars
    OWNER to postgres;
	
	
CREATE TABLE IF NOT EXISTS CarXuser
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    userid integer NOT NULL,
    carid integer NOT NULL,
    rent_date date NOT NULL,
    state VARCHAR(12) NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS CarXuser
    OWNER to postgres;


INSERT INTO Users(name, username, email, password, birthdate, account_state) 
VALUES
('Juan Pérez', 'juanperez', 'juanperez@gmail.com', 'password1', '1990-01-15', 'active'),
('Ana Gómez', 'anagomez', 'anagomez@gmail.com', 'password2', '1985-02-25', 'active'),
('Carlos López', 'carloslopez', 'carloslopez@gmail.com', 'password3', '1988-03-30', 'inactive'),
('Maria Fernández', 'mariafernandez', 'mariafernandez@gmail.com', 'password4', '1992-04-05', 'active'),
('Luis García', 'luisgarcia', 'luisgarcia@gmail.com', 'password5', '1983-05-12', 'inactive'),
('Elena Martínez', 'elenamartinez', 'elenamartinez@gmail.com', 'password6', '1995-06-20', 'active'),
('David Sánchez', 'davidsanchez', 'davidsanchez@gmail.com', 'password7', '1990-07-30', 'active'),
('Paula Rodríguez', 'paularodriguez', 'paularodriguez@gmail.com', 'password8', '1989-08-11', 'inactive'),
('José Herrera', 'joseherrera', 'joseherrera@gmail.com', 'password9', '1991-09-14', 'active'),
('Laura Jiménez', 'laurajimenez', 'laurajimenez@gmail.com', 'password10', '1993-10-25', 'inactive'),
('Antonio Morales', 'antoniomorales', 'antoniomorales@gmail.com', 'password11', '1980-11-04', 'active'),
('Sofia Ruiz', 'sofiaruiz', 'sofiaruiz@gmail.com', 'password12', '1987-12-13', 'inactive'),
('Pedro Fernández', 'pedrofernandez', 'pedrofernandez@gmail.com', 'password13', '1992-01-19', 'active'),
('Carmen González', 'carmengonzalez', 'carmengonzalez@gmail.com', 'password14', '1994-02-22', 'inactive'),
('Ricardo Pérez', 'ricardoperez', 'ricardoperez@gmail.com', 'password15', '1986-03-30', 'active'),
('María Ruiz', 'mariaruiz', 'mariaruiz@gmail.com', 'password16', '1990-04-10', 'inactive'),
('Miguel Díaz', 'migueldiaz', 'migueldiaz@gmail.com', 'password17', '1985-05-18', 'active'),
('Isabel Martín', 'isabelmartin', 'isabelmartin@gmail.com', 'password18', '1992-06-01', 'inactive'),
('Juan Martínez', 'juanmartinez', 'juanmartinez@gmail.com', 'password19', '1993-07-25', 'active'),
('Adriana Rodríguez', 'adrianarodriguez', 'adrianarodriguez@gmail.com', 'password20', '1981-08-12', 'inactive'),
('Javier Torres', 'javiertorres', 'javiertorres@gmail.com', 'password21', '1990-09-15', 'active'),
('Rosa González', 'rosagonzalez', 'rosagonzalez@gmail.com', 'password22', '1986-10-04', 'inactive'),
('Ricardo García', 'ricardogarcia', 'ricardogarcia@gmail.com', 'password23', '1992-11-20', 'active'),
('Luis Rodríguez', 'luisrodriguez', 'luisrodriguez@gmail.com', 'password24', '1991-12-30', 'inactive'),
('Ángel Jiménez', 'angeljimenez', 'angeljimenez@gmail.com', 'password25', '1989-01-10', 'active'),
('Ana Díaz', 'anadiaz', 'anadiaz@gmail.com', 'password26', '1993-02-20', 'inactive'),
('David Gómez', 'davidgomez', 'davidgomez@gmail.com', 'password27', '1988-03-15', 'active'),
('Pilar López', 'pilarlopez', 'pilarlopez@gmail.com', 'password28', '1994-04-07', 'inactive'),
('Sergio Martínez', 'sergiomartinez', 'sergiomartinez@gmail.com', 'password29', '1990-05-17', 'active'),
('Clara Sánchez', 'clarasanchez', 'clarasanchez@gmail.com', 'password30', '1987-06-22', 'inactive'),
('Felipe Pérez', 'felipeperez', 'felipeperez@gmail.com', 'password31', '1992-07-01', 'active'),
('Jorge Ruiz', 'jorgeruiz', 'jorgeruiz@gmail.com', 'password32', '1984-08-18', 'inactive'),
('Berta Fernández', 'bertafernandez', 'bertafernandez@gmail.com', 'password33', '1990-09-29', 'active'),
('Raúl Rodríguez', 'raulrodriguez', 'raulrodriguez@gmail.com', 'password34', '1993-10-13', 'inactive'),
('Marta López', 'martalopez', 'martalopez@gmail.com', 'password35', '1988-11-02', 'active'),
('Antonio Pérez', 'antonioperez', 'antonioperez@gmail.com', 'password36', '1991-12-14', 'inactive'),
('Beatriz González', 'beatrizgonzalez', 'beatrizgonzalez@gmail.com', 'password37', '1992-01-26', 'active'),
('Luis Díaz', 'luisdiaz', 'luisdiaz@gmail.com', 'password38', '1990-02-20', 'inactive'),
('José López', 'joselopez', 'joselopez@gmail.com', 'password39', '1986-03-05', 'active'),
('Sandra Martínez', 'sandramartinez', 'sandramartinez@gmail.com', 'password40', '1989-04-11', 'inactive'),
('Vicente García', 'vicentegarcia', 'vicentegarcia@gmail.com', 'password41', '1991-05-03', 'active'),
('Sonia Torres', 'soniatorres', 'soniatorres@gmail.com', 'password42', '1994-06-16', 'inactive'),
('Juan Jiménez', 'juanjimenez', 'juanjimenez@gmail.com', 'password43', '1982-07-23', 'active'),
('Eva Fernández', 'evafernandez', 'evafernandez@gmail.com', 'password44', '1990-08-25', 'inactive'),
('Raquel Ruiz', 'raquelruiz', 'raquelruiz@gmail.com', 'password45', '1993-09-08', 'active'),
('Enrique López', 'enriquelopez', 'enriquelopez@gmail.com', 'password46', '1987-10-02', 'inactive'),
('Alberto Pérez', 'albertoperez', 'albertoperez@gmail.com', 'password47', '1992-11-18', 'active'),
('Mónica Rodríguez', 'monicarodriguez', 'monicarodriguez@gmail.com', 'password48', '1994-12-12', 'inactive'),
('Carlos Martínez', 'carlosmartinez', 'carlosmartinez@gmail.com', 'password49', '1988-01-06', 'active'),
('Gloria Sánchez', 'gloriasanchez', 'gloriasanchez@gmail.com', 'password50', '1991-02-14', 'inactive');



INSERT INTO Cars (brand, model, year, state) 
VALUES
    ('Toyota', 'Corolla', 2020, 'Available'),
    ('Honda', 'Civic', 2019, 'Available'),
    ('Ford', 'Fiesta', 2021, 'Rented'),
    ('Chevrolet', 'Cruze', 2018, 'Available'),
    ('Nissan', 'Altima', 2022, 'Rented'),
    ('BMW', '320i', 2021, 'Available'),
    ('Mercedes', 'A-Class', 2020, 'Available'),
    ('Audi', 'A4', 2019, 'Rented'),
    ('Volkswagen', 'Golf', 2022, 'Available'),
    ('Hyundai', 'Elantra', 2020, 'Rented'),
    ('Mazda', 'CX-5', 2021, 'Available'),
    ('Kia', 'Optima', 2022, 'Rented'),
    ('Toyota', 'Camry', 2018, 'Available'),
    ('Honda', 'Accord', 2019, 'Rented'),
    ('Ford', 'Mustang', 2021, 'Available'),
    ('Chevrolet', 'Malibu', 2020, 'Available'),
    ('Nissan', 'Sentra', 2022, 'Rented'),
    ('BMW', 'X5', 2021, 'Available'),
    ('Mercedes', 'C-Class', 2020, 'Rented'),
    ('Audi', 'Q5', 2021, 'Available'),
    ('Volkswagen', 'Passat', 2020, 'Available'),
    ('Hyundai', 'Sonata', 2022, 'Rented'),
    ('Mazda', 'Mazda3', 2019, 'Available'),
    ('Kia', 'Sorrento', 2021, 'Rented'),
    ('Toyota', 'Highlander', 2020, 'Available'),
    ('Honda', 'Pilot', 2021, 'Available'),
    ('Ford', 'Explorer', 2022, 'Rented'),
    ('Chevrolet', 'Equinox', 2019, 'Available'),
    ('Nissan', 'Rogue', 2020, 'Rented'),
    ('BMW', 'X3', 2022, 'Available'),
    ('Mercedes', 'GLC', 2021, 'Available'),
    ('Audi', 'Q7', 2020, 'Rented'),
    ('Volkswagen', 'Tiguan', 2021, 'Available'),
    ('Hyundai', 'Tucson', 2019, 'Rented'),
    ('Mazda', 'CX-3', 2020, 'Available'),
    ('Kia', 'Sportage', 2021, 'Rented'),
    ('Toyota', '4Runner', 2022, 'Available'),
    ('Honda', 'CR-V', 2021, 'Available'),
    ('Ford', 'Edge', 2020, 'Rented'),
    ('Chevrolet', 'Traverse', 2021, 'Available'),
    ('Nissan', 'Murano', 2022, 'Available'),
    ('BMW', 'X1', 2020, 'Rented'),
    ('Mercedes', 'GLA', 2021, 'Available'),
    ('Audi', 'Q3', 2019, 'Available'),
    ('Volkswagen', 'Atlas', 2022, 'Rented'),
    ('Hyundai', 'Palisade', 2021, 'Available'),
    ('Mazda', 'CX-30', 2022, 'Available'),
    ('Kia', 'Telluride', 2020, 'Available'),
    ('Toyota', 'Land Cruiser', 2021, 'Rented'),
    ('Honda', 'Passport', 2022, 'Available'),
    ('Ford', 'Bronco', 2020, 'Available'),
    ('Chevrolet', 'Tahoe', 2021, 'Rented'),
    ('Nissan', 'Armada', 2022, 'Available');



INSERT INTO CarXuser (userid, carid, rent_date, state)
VALUES
(1, 1, '2025-03-24', 'Completed'),
(1, 5, '2023-11-12', 'Ongoing'),
(2, 2, '2021-05-18', 'Pending'),
(2, 6, '2022-07-30', 'Denied'),
(3, 3, '2024-02-14', 'Ongoing'),
(3, 7, '2020-08-06', 'Denied'),
(4, 8, '2023-09-22', 'Ongoing'),
(5, 9, '2025-01-11', 'Pending'),
(5, 10, '2021-06-17', 'Ongoing'),
(6, 11, '2022-10-04', 'Denied'),
(6, 12, '2024-12-25', 'Ongoing'),
(7, 13, '2021-04-28', 'Denied'),
(8, 14, '2020-10-15', 'Ongoing'),
(8, 15, '2023-02-05', 'Pending'),
(9, 16, '2024-03-20', 'Pending'),
(9, 17, '2022-05-01', 'Ongoing'),
(10, 18, '2023-12-30', 'Completed'),
(11, 19, '2025-02-22', 'Ongoing'),
(11, 20, '2020-06-10', 'Denied'),
(12, 21, '2021-11-29', 'Pending'),
(12, 22, '2024-04-16', 'Ongoing'),
(13, 23, '2023-07-08', 'Denied'),
(13, 24, '2022-01-19', 'Ongoing'),
(14, 25, '2021-03-25', 'Denied'),
(15, 26, '2020-09-09', 'Pending'),
(15, 27, '2023-05-04', 'Ongoing'),
(16, 28, '2022-11-18', 'Denied'),
(17, 29, '2024-01-23', 'Ongoing'),
(18, 30, '2025-03-13', 'Pending'),
(18, 3, '2021-12-02', 'Ongoing'),
(19, 7, '2022-06-06', 'Completed'),
(19, 8, '2020-02-29', 'Ongoing'),
(20, 2, '2023-08-17', 'Pending'),
(20, 1, '2024-09-21', 'Denied'),
(21, 4, '2021-10-05', 'Denied'),
(21, 9, '2025-04-15', 'Completed'),
(22, 6, '2022-12-11', 'Pending'),
(22, 11, '2023-01-10', 'Pending'),
(23, 14, '2021-07-22', 'Ongoing'),
(23, 10, '2020-03-03', 'Ongoing'),
(24, 17, '2024-11-07', 'Ongoing'),
(24, 12, '2023-04-17', 'Ongoing'),
(25, 19, '2021-08-30', 'Ongoing'),
(26, 22, '2024-06-25', 'Ongoing'),
(27, 25, '2025-01-03', 'Denied'),
(28, 27, '2022-04-11', 'Ongoing'),
(29, 26, '2023-02-24', 'Pending'),
(29, 28, '2021-09-12', 'Completed'),
(30, 24, '2024-08-13', 'Ongoing'),
(30, 29, '2022-07-25', 'Ongoing'),
(1, 21, '2020-11-30', 'Denied'),
(2, 30, '2025-02-03', 'Completed'),
(3, 4, '2021-12-01', 'Pending'),
(4, 5, '2022-03-10', 'Ongoing'),
(5, 6, '2024-05-14', 'Pending'),
(6, 7, '2021-01-07', 'Denied'),
(7, 8, '2023-06-27', 'Ongoing'),
(8, 9, '2020-04-20', 'Denied'),
(9, 10, '2022-02-16', 'Ongoing'),
(10, 11, '2021-03-29', 'Pending'),
(11, 12, '2023-10-09', 'Ongoing'),
(12, 13, '2022-08-22', 'Denied'),
(13, 14, '2024-03-15', 'Ongoing'),
(14, 15, '2021-11-03', 'Pending'),
(15, 16, '2025-03-10', 'Completed'),
(16, 17, '2023-09-18', 'Ongoing'),
(17, 18, '2024-01-13', 'Completed'),
(18, 19, '2020-07-07', 'Ongoing'),
(19, 20, '2021-04-01', 'Denied'),
(20, 21, '2022-09-13', 'Denied'),
(21, 22, '2023-08-08', 'Ongoing'),
(22, 23, '2021-06-01', 'Pending'),
(23, 24, '2024-10-12', 'Ongoing'),
(24, 25, '2025-03-05', 'Completed'),
(25, 26, '2022-12-21', 'Completed'),
(26, 27, '2023-05-15', 'Ongoing'),
(27, 28, '2020-10-12', 'Denied'),
(28, 29, '2021-02-18', 'Ongoing'),
(29, 30, '2023-07-10', 'Denied'),
(30, 1, '2024-04-23', 'Completed');

--CAMBIO DE ESTADO DEL USUARIO
Update Users SET account_state = 'active' WHERE id BETWEEN  1 AND 10 AND account_state LIKE 'inactive';


--CAMBIO DE ESTADO DEL AUTOMOVIL
Update Cars SET state = 'Rented' WHERE id > 5 AND id < 15 AND state LIKE 'Available';

--CONFIRMAR DEVOLUCION DEL AUTO AL COMPLETAR ALQUILER
SELECT * FROM Cars
INNER JOIN CarXuser ON Cars.id = CarXuser.carid
WHERE Cars.id BETWEEN 1 AND 15 AND CarXuser.state LIKE 'Ongoing';

Update Cars SET state = 'Available' WHERE state LIKE 'Rented' AND id BETWEEN 1 AND 15;
Update CarXuser SET state = 'Completed' WHERE carid BETWEEN 1 AND 15 AND state LIKE 'Ongoing';

SELECT * FROM Cars
INNER JOIN CarXuser ON Cars.id = CarXuser.carid
WHERE Cars.id BETWEEN 1 AND 15 AND CarXuser.state LIKE 'Completed';

--DESABILITAR UN AUTO DE ALQUILER
Update CarXuser SET state = 'Unavailable' WHERE carid = 12 AND state LIKE 'Ongoing' OR state LIKE 'Pending' OR state LIKE 'Denied' OR state LIKE 'Completed';

SELECT * FROM CarXuser WHERE carid = 12;

--OBTENER TODOS LOS AUTOMOVILES ALQUILADOS
SELECT id AS Car_id,brand,model,state AS Car_state FROM Cars WHERE Cars.state LIKE 'Rented' ORDER BY id ASC;

--OBTENER TODOS LOS AUTOMOVILES DISPONIBLES
SELECT id AS Car_id,brand,model,state AS Car_state FROM Cars WHERE Cars.state LIKE 'Available' ORDER BY id ASC;