-- SQL-команды для создания таблиц
CREATE TABLE customers_data
(
	customers_id varchar(100) PRIMARY KEY NOT NULL,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100)
);

CREATE TABLE employees_data
(
	employee_id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100),
	birth_date date,
	notes text NOT NULL
);

CREATE TABLE orders_data
(
	order_id int PRIMARY KEY NOT NULL,
	customer_id varchar(100) REFERENCES customers_data(customers_id) NOT NULL,
	employee_id int REFERENCES employees_data(employee_id),
	order_date date NOT NULL,
	ship_city text NOT NULL
);