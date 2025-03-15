-- SQLite
CREATE TABLE Authors(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Name nvarchar(25) NOT NULL
);

CREATE TABLE Books(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Name nvarchar(25) NOT NULL,
Author INTEGER REFERENCES Authors(id)
);

CREATE TABLE Customers(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Name nvarchar(25) NOT NULL,
Email nvarchar(25) NOT NULL
);

CREATE TABLE Rents(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
BookID INTEGER REFERENCES Books(Id) NOT NULL,
CustomerID INTEGER REFERENCES Customers(Id) NOT NULL,
State nvarchar(8) NOT NULL
);

INSERT INTO Authors (Name) VALUES ('Miguel de Cervantes');
INSERT INTO Authors (Name) VALUES ('Dante Alighieri');
INSERT INTO Authors (Name) VALUES ('Takehiko Inoue');
INSERT INTO Authors (Name) VALUES ('Akira Toriyama');
INSERT INTO Authors (Name) VALUES ('Walt Disney');

INSERT INTO Books (Name,Author) VALUES ('Don Quijote',1);
INSERT INTO Books (Name,Author) VALUES ('La Divina Comedia',2);
INSERT INTO Books (Name,Author) VALUES ('Vagabond 1-3',3);
INSERT INTO Books (Name,Author) VALUES ('Dragon Ball 1',4);
INSERT INTO Books (Name,Author) VALUES ('The Book of the 5 Rings',NULL);

INSERT INTO Customers (Name,Email) VALUES ('John Doe','j.doe@email.com');
INSERT INTO Customers (Name,Email) VALUES ('Jane Doe','jane@doe.com');
INSERT INTO Customers (Name,Email) VALUES ('Luke Skywalker','darth.son@email.com');

INSERT INTO Rents (BookID,CustomerID,State) VALUES (1,2,'Returned');
INSERT INTO Rents (BookID,CustomerID,State) VALUES (2,2,'Returned');
INSERT INTO Rents (BookID,CustomerID,State) VALUES (1,1,'On time');
INSERT INTO Rents (BookID,CustomerID,State) VALUES (3,1,'On time');
INSERT INTO Rents (BookID,CustomerID,State) VALUES (2,2,'Overdue');

SELECT Name AS Book_Name,Author FROM Books WHERE Author NOT NULL;
SELECT Name AS Book_Name,Author FROM Books WHERE Author IS NULL;
SELECT Authors.Name AS Author_Name,Books.Name AS Book_Name FROM Authors LEFT JOIN Books ON Books.Author = Authors.Id WHERE Books.Author IS NULL;
SELECT Books.Name AS Book_Name,Rents.State FROM Rents INNER JOIN Books ON Rents.BookID = Books.Id WHERE Rents.State NOT LIKE 'Returned';
SELECT Books.Name AS Book_Name,Rents.State FROM Rents INNER JOIN Books ON Rents.BookID = Books.Id WHERE Rents.State IS NULL; --Nunca han sido rentados, segun las tablas todos los libros han sido rentados en algun momento
SELECT Name as Customer_Name,Rents.State FROM Customers LEFT JOIN Rents ON Customers.Id = Rents.CustomerID WHERE Rents.State IS NULL; --Clientes que nunca han rentado un libro, segun las tablas todos los clientes han rentado libros en algun momento
SELECT Books.Name AS Book_Name, Rents.State FROM Books INNER JOIN Rents ON Books.Id = Rents.BookID WHERE Rents.State LIKE 'Overdue';