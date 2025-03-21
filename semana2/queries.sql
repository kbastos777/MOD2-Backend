-- SQLite
-- SELECT 'INSERT INTO bills (number,purchase_date,cart_email,purchase_total,customer_phone_number,employee_code) VALUES (''' || number || ''',''' || purchase_date || ''',''' || cart_email || ''',''' || purchase_total || ''',''' || customer_phone_number || ''',''' || employee_code || ''');' 
-- FROM bills; -- Esto sirve para visualizar como se ingresaron los registros a las tablas, devuelve cual comando de insert se utilizo exactamente


CREATE TABLE purchase_carts(
id INTEGER PRIMARY KEY AUTOINCREMENT,
email nvarchar(25) NOT NULL
);

CREATE TABLE products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
code nvarchar(8) UNIQUE NOT NULL,
name nvarchar(10) NOT NULL,
price FLOAT NOT NULL,
entry_date TIMESTAMP NOT NULL
);

CREATE TABLE bills(
id INTEGER PRIMARY KEY AUTOINCREMENT,
number SMALLINT UNIQUE NOT NULL,
purchase_date TIMESTAMP NOT NULL,
cart_email nvarchar(25) REFERENCES purchase_carts(email) NOT NULL,
purchase_total FLOAT NOT NULL,
customer_phone_number nvarchar(12),
employee_code nvarchar(5) NOT NULL
);

CREATE TABLE purchase_cartsXProducts (
id INTEGER PRIMARY KEY AUTOINCREMENT,
cart_id INTEGER REFERENCES purchase_carts(id) NOT NULL,
product_id INTEGER REFERENCES product(id) NOT NULL
);

CREATE TABLE productsXBills (
id INTEGER PRIMARY KEY AUTOINCREMENT,
bill_id INTEGER REFERENCES bills(id) NOT NULL,
product_id INTEGER REFERENCES product(id) NOT NULL,
product_quantity SMALLINT NOT NULL
);


INSERT INTO purchase_carts (email) VALUES ('tlaughlan1@ebay.co.uk');
INSERT INTO purchase_carts (email) VALUES ('tlaughlan1@ebay.co.uk');
INSERT INTO purchase_carts (email) VALUES ('tlaughlan1@ebay.co.uk');
INSERT INTO purchase_carts (email) VALUES ('kneames4@cdbaby.com');
INSERT INTO purchase_carts (email) VALUES ('kneames4@cdbaby.com');
INSERT INTO purchase_carts (email) VALUES ('schadwen5@liveinternet.ru');
INSERT INTO purchase_carts (email) VALUES ('edunlop6@google.com.au');
INSERT INTO purchase_carts (email) VALUES ('skivell8@apple.com');
INSERT INTO purchase_carts (email) VALUES ('skivell8@apple.com');
INSERT INTO purchase_carts (email) VALUES ('psimmgen9@wunderground.com');
INSERT INTO purchase_carts (email) VALUES ('bvegasa@tinyurl.com');

INSERT INTO products (code,name,price,entry_date) VALUES ('43245trt','perfume',1000,'2025-12-31');
INSERT INTO products (code,name,price,entry_date) VALUES ('43e35eee','Hat',10000,'2024-11-3');
INSERT INTO products (code,name,price,entry_date) VALUES ('4555gggg','Golden egg',100000,'2023-01-3');
INSERT INTO products (code,name,price,entry_date) VALUES ('7555gggg','Skateboard',50000,'2025-11-4');
INSERT INTO products (code,name,price,entry_date) VALUES ('6546oihh','Deluxe Lamp',200000,'2024-10-3');
INSERT INTO products (code,name,price,entry_date) VALUES ('77567hyu','Video Game',45000,'2024-10-3');
INSERT INTO products (code,name,price,entry_date) VALUES ('iiiii435','Chess Table',75000,'2022-01-23');
INSERT INTO products (code,name,price,entry_date) VALUES ('4453fstg','TV',1000000,'2024-05-5');
INSERT INTO products (code,name,price,entry_date) VALUES ('6575fghd','Plant',20000,'2025-11-4');
INSERT INTO products (code,name,price,entry_date) VALUES ('ttt44335','Phone',200000,'2022-11-1');

INSERT INTO bills (number,purchase_date,cart_email,purchase_total,customer_phone_number,employee_code) VALUES (1,'2-20-2025','tlaughlan1@ebay.co.uk',211000,'88765544','emp01'); -- ttt44335 43e35eee 43245trt
INSERT INTO bills (number,purchase_date,cart_email,purchase_total,customer_phone_number,employee_code) VALUES (2,'6-10-2024','tlaughlan1@ebay.co.uk',195000,'88765544','emp02');--7555gggg 4555gggg 77567hyu
INSERT INTO bills (number,purchase_date,cart_email,purchase_total,customer_phone_number,employee_code) VALUES (3,'4-5-2025','tlaughlan1@ebay.co.uk',135000,'88765544','emp01'); --iiiii435 6575fghd 6575fghd 6575fghd
INSERT INTO bills (number,purchase_date,cart_email,purchase_total,customer_phone_number,employee_code) VALUES (4,'1-1-2023','kneames4@cdbaby.com',1220000,'70097654','emp03'); -- 43e35eee 43e35eee ttt44335 4453fstg
INSERT INTO bills (number,purchase_date,cart_email,purchase_total,customer_phone_number,employee_code) VALUES (5,'12-12-2024','kneames4@cdbaby.com',295000,'70097654','emp02'); -- ttt44335 iiiii435 6575fghd
INSERT INTO bills (number,purchase_date,cart_email,purchase_total,customer_phone_number,employee_code) VALUES (6,'2-12-2020','schadwen5@liveinternet.ru',122000,'40789967','emp01'); -- 43245trt 43245trt 6575fghd 4555gggg
INSERT INTO bills (number,purchase_date,cart_email,purchase_total,customer_phone_number,employee_code) VALUES (7,'2-1-2025','edunlop6@google.com.au',45000,'78653333','emp01'); --77567hyu
INSERT INTO bills (number,purchase_date,cart_email,purchase_total,customer_phone_number,employee_code) VALUES (8,'7-11-2024','skivell8@apple.com',220000,'88568888','emp03');-- ttt44335 6575fghd
INSERT INTO bills (number,purchase_date,cart_email,purchase_total,customer_phone_number,employee_code) VALUES (9,'3-7-2025','skivell8@apple.com',12000,'88568888','emp03'); --43245trt 43245trt 43e35eee
INSERT INTO bills (number,purchase_date,cart_email,purchase_total,customer_phone_number,employee_code) VALUES (10,'4-26-2021','psimmgen9@wunderground.com',50000,'78653456','emp02'); --7555gggg
INSERT INTO bills (number,purchase_date,cart_email,purchase_total,customer_phone_number,employee_code) VALUES (11,'12-12-2024','bvegasa@tinyurl.com',1000000,'48776578','emp01'); -- 4453fstg

INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (1,10);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (1,2);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (1,1);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (2,4);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (2,3);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (2,6);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (3,7);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (3,9);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (3,9);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (3,9);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (4,2);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (4,2);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (4,10);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (4,8);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (5,10);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (5,7);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (5,9);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (6,1);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (6,1);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (6,9);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (6,3);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (7,6);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (8,10);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (8,9);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (9,1);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (9,1);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (9,2);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (10,4);
INSERT INTO purchase_cartsXProducts (cart_id,product_id) VALUES (11,8);

INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (1,10,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (1,2,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (1,1,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (2,4,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (2,3,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (2,6,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (3,7,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (3,9,3);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (4,2,2);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (4,10,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (4,8,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (5,10,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (5,7,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (5,9,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (6,1,2);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (6,9,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (6,3,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (7,6,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (8,10,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (8,9,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (9,1,2);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (9,2,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (10,4,1);
INSERT INTO productsXBills (bill_id,product_id,product_quantity) VALUES (11,8,1);

SELECT * from products;

SELECT * from products WHERE price > 50000;

SELECT cart_id,product_id,code,name AS product_name,price AS product_price from purchase_cartsXProducts LEFT JOIN products ON purchase_cartsXProducts.product_id = products.id WHERE product_id == 10

SELECT  purchase_cartsXProducts.cart_id,purchase_cartsXProducts.product_id,products.code,products.name AS product_name,(products.price * SUM(productsXBills.product_quantity)) AS Purchased_total from purchase_cartsXProducts 
LEFT JOIN products ON purchase_cartsXProducts.product_id = products.id
LEFT JOIN productsXBills ON productsXBills.product_id = purchase_cartsXProducts.product_id
GROUP by name ORDER BY name

SELECT id AS bill_id , number AS bill_number ,purchase_date,cart_email AS customer_email ,purchase_total,customer_phone_number,employee_code FROM bills
WHERE bills.cart_email LIKE 'tlaughlan1@ebay.co.uk'

SELECT id AS bill_id , number AS bill_number ,purchase_date,cart_email AS customer_email,customer_phone_number,employee_code,purchase_total FROM bills
ORDER BY purchase_total DESC

SELECT id AS bill_id , number AS bill_number ,purchase_date,cart_email AS customer_email,customer_phone_number,employee_code,purchase_total FROM bills
WHERE number = 11 