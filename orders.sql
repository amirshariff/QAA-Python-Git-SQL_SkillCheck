CREATE TABLE IF NOT EXISTS cafe (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    customer_name VARCHAR(10) NOT NULL, 
    drink VARCHAR (10) NOT NULL,
    size VARCHAR(15) NOT NULL,
    price FLOAT NOT NULL 
);

INSERT INTO cafe (customer_name, drink, size, price) 
VALUES ('Reese_Witherspoon', 'Tea', 'Small',  0.5);

INSERT INTO cafe (customer_name, drink, size, price) 
VALUES ('Bruno_Mars', 'Iced_Coffee', 'Large', 0.2);

INSERT INTO cafe (customer_name, drink, size, price) 
VALUES ('Andy_Cole', 'tea', 'Small', 0.1);

INSERT INTO cafe (customer_name, drink, size, price) 
VALUES ('Joell_Ortiz', 'black_coffee', 'Medium',  0.2);

INSERT INTO cafe (customer_name, drink, size, price) 
VALUES ('Thiery_Henry', 'Black_Coffee', 'Medium',  0.7);

INSERT INTO cafe (customer_name, drink, size,  price) 
VALUES ('Alan_Shearer', 'Flat_White', 'Large',  0.05);


SELECT * FROM cafe 