# onlinestore=# CREATE TABLE Products(id serial, name varchar(100), price integer, quantity integer);
# CREATE TABLE
# onlinestore=# \l
# onlinestore=# \dt
#           List of relations
#  Schema |   Name   | Type  |  Owner   
# --------+----------+-------+----------
#  public | products | table | zhanybek
# (1 row)

# onlinestore=# CREATE TABLE Customers(id serial primary key, first_name varchar(100), last_name varchar(100), email varchar(100));
# CREATE TABLE
# onlinestore=# CREATE TABLE Orders(id serial, customer_id integer, order_date date, total_amount integer, foreign key (customer_id) pereferences Customer (id));
# ERROR:  syntax error at or near "pereferences"
# LINE 1: ..., total_amount integer, foreign key (customer_id) pereferenc...
#                                                              ^
# onlinestore=# CREATE TABLE Orders(id serial, customer_id integer, order_date date, total_amount integer, foreign key (customer_id) peferences Customer (id));
# ERROR:  syntax error at or near "peferences"
# LINE 1: ..., total_amount integer, foreign key (customer_id) peferences...
#                                                              ^
# onlinestore=# CREATE TABLE Orders(id serial, customer_id integer, order_date date, total_amount integer, foreign key (customer_id) REFERENCES Customers (id));
# CREATE TABLE
# onlinestore=# \dt
#            List of relations
#  Schema |   Name    | Type  |  Owner   
# --------+-----------+-------+----------
#  public | customers | table | zhanybek
#  public | orders    | table | zhanybek
#  public | products  | table | zhanybek
# (3 rows)

# onlinestore=# select * from customers; 
#  id | first_name | last_name | email 
# ----+------------+-----------+-------
# (0 rows)

# onlinestore=# insert into customers (first_name, las)

# onlinestore=# insert into customers (first_name, las)

# onlinestore=# insert into customers (first_name, last_name, email) values ('john', 'snow', 'john@gmail.com');
# INSERT 0 1
# onlinestore=# select * from customers; 
#  id | first_name | last_name |     email      
# ----+------------+-----------+----------------
#   1 | john       | snow      | john@gmail.com
# (1 row)

# onlinestore=# select * from orders; 
#  id | customer_id | order_date | total_amount 
# ----+-------------+------------+--------------
# (0 rows)

# onlinestore=# insert into customers (cu) values ('john', 'snow', 'john@gmail.com');

# onlinestore=# insert into orders (customer_id, order_date, total_amount) values (8833, 08.03.2024, 2000);
# ERROR:  syntax error at or near ".2024"
# LINE 1: ..._id, order_date, total_amount) values (8833, 08.03.2024, 200...
#                                                              ^
# onlinestore=# insert into orders (customer_id, order_date, total_amount) values (8833, 08.03, 2000);
# ERROR:  column "order_date" is of type date but expression is of type numeric
# LINE 1: ...tomer_id, order_date, total_amount) values (8833, 08.03, 200...
#                                                              ^
# HINT:  You will need to rewrite or cast the expression.
# onlinestore=# insert into orders (customer_id, order_date, total_amount) values (8833, 08.03, 2000));
# ERROR:  syntax error at or near ")"
# LINE 1: ...r_id, order_date, total_amount) values (8833, 08.03, 2000));
#                                                                      ^
# onlinestore=# insert into orders (customer_id, order_date, total_amount) values ('8833', 08.03, 2000));
# ERROR:  syntax error at or near ")"
# LINE 1: ...id, order_date, total_amount) values ('8833', 08.03, 2000));
#                                                                      ^
# onlinestore=# insert into orders (customer_id, order_date, total_amount) values ('8833', 08.03, 2000);
# ERROR:  column "order_date" is of type date but expression is of type numeric
# LINE 1: ...mer_id, order_date, total_amount) values ('8833', 08.03, 200...
#                                                              ^
# HINT:  You will need to rewrite or cast the expression.
# onlinestore=# insert into orders (customer_id, order_date, total_amount) values ('8833', 08.03, '2000');
# ERROR:  column "order_date" is of type date but expression is of type numeric
# LINE 1: ...mer_id, order_date, total_amount) values ('8833', 08.03, '20...
#                                                              ^
# HINT:  You will need to rewrite or cast the expression.
# onlinestore=# insert into orders (customer_id, order_date, total_amount) values ('8833', '08.03', '2000');
# ERROR:  invalid input syntax for type date: "08.03"
# LINE 1: ...mer_id, order_date, total_amount) values ('8833', '08.03', '...
#                                                              ^
# onlinestore=# insert into orders (customer_id, order_date, total_amount) values (8833, 08.03, 2000);
# ERROR:  column "order_date" is of type date but expression is of type numeric
# LINE 1: ...tomer_id, order_date, total_amount) values (8833, 08.03, 200...
#                                                              ^
# HINT:  You will need to rewrite or cast the expression.
# onlinestore=# select * from orders; 
#  id | customer_id | order_date | total_amount 
# ----+-------------+------------+--------------
# (0 rows)

# onlinestore=# insert into orders (customer_id, order_date, total_amount) values (8833, 08.03, 2000);
# ERROR:  column "order_date" is of type date but expression is of type numeric
# LINE 1: ...tomer_id, order_date, total_amount) values (8833, 08.03, 200...
#                                                              ^
# HINT:  You will need to rewrite or cast the expression.
# onlinestore=# INSERT INTO orders (customer_id, order_date, total_amount) VALUES (8833, '2024-03-08', 2000);
# ERROR:  insert or update on table "orders" violates foreign key constraint "orders_customer_id_fkey"
# DETAIL:  Key (customer_id)=(8833) is not present in table "customers".
# onlinestore=# INSERT INTO orders (customer_id, order_date, total_amount) VALUES (8833, '2024-03-08', 2000);
# ERROR:  insert or update on table "orders" violates foreign key constraint "orders_customer_id_fkey"
# DETAIL:  Key (customer_id)=(8833) is not present in table "customers".
# onlinestore=# INSERT INTO orders (customer_id, order_date, total_amount) VALUES (8833, '2024.03.08', 2000);
# ERROR:  insert or update on table "orders" violates foreign key constraint "orders_customer_id_fkey"
# DETAIL:  Key (customer_id)=(8833) is not present in table "customers".
# onlinestore=# INSERT INTO orders (customer_id, order_date, total_amount) VALUES (1, '2024.03.08', 2000);
# INSERT 0 1
# onlinestore=# select * from orders; 
#  id | customer_id | order_date | total_amount 
# ----+-------------+------------+--------------
#   4 |           1 | 2024-03-08 |         2000
# (1 row)

# onlinestore=# select * from products; 
#  id | name | price | quantity 
# ----+------+-------+----------
# (0 rows)

# onlinestore=# INSERT INTO products (name, price, quantity) VALUES ('Mcdonalds', 5, 100);
# INSERT 0 1
# onlinestore=# select * from products; 
#  id |   name    | price | quantity 
# ----+-----------+-------+----------
#   1 | Mcdonalds |     5 |      100
# (1 row)

# onlinestore=# \dt
#            List of relations
#  Schema |   Name    | Type  |  Owner   
# --------+-----------+-------+----------
#  public | customers | table | zhanybek
#  public | orders    | table | zhanybek
#  public | products  | table | zhanybek
# (3 rows)

# onlinestore=# insert into customers (first_name, last_name, email) values ('john', 'snow', 'john@gmail.com'), ('Alihan', 'Kurmanbekov', 'kurmanbekov@gmail.com'), ('Anvar', 'Shamsudinov', 'shamsudinov@gmail.com'), ('Azamat', 'Mukambetov', 'mukambetov@gmail.com'), ('Zhoomart', 'Namazov', 'namazov@gmail.com');
# INSERT 0 5
# onlinestore=# select * fr

# onlinestore=# select * from customers;
#  id | first_name |  last_name  |         email         
# ----+------------+-------------+-----------------------
#   1 | john       | snow        | john@gmail.com
#   2 | john       | snow        | john@gmail.com
#   3 | Alihan     | Kurmanbekov | kurmanbekov@gmail.com
#   4 | Anvar      | Shamsudinov | shamsudinov@gmail.com
#   5 | Azamat     | Mukambetov  | mukambetov@gmail.com
#   6 | Zhoomart   | Namazov     | namazov@gmail.com
# (6 rows)

# onlinestore=# DELETE FROM customers WHERE id=1;
# ERROR:  update or delete on table "customers" violates foreign key constraint "orders_customer_id_fkey" on table "orders"
# DETAIL:  Key (id)=(1) is still referenced from table "orders".
# onlinestore=# DELETE FROM customers WHERE id=2;
# DELETE 1
# onlinestore=# select * from customers;
#  id | first_name |  last_name  |         email         
# ----+------------+-------------+-----------------------
#   1 | john       | snow        | john@gmail.com
#   3 | Alihan     | Kurmanbekov | kurmanbekov@gmail.com
#   4 | Anvar      | Shamsudinov | shamsudinov@gmail.com
#   5 | Azamat     | Mukambetov  | mukambetov@gmail.com
#   6 | Zhoomart   | Namazov     | namazov@gmail.com
# (5 rows)

# onlinestore=# select * from products;
#  id |   name    | price | quantity 
# ----+-----------+-------+----------
#   1 | Mcdonalds |     5 |      100
# (1 row)

# onlinestore=# INSERT INTO products (name, price, quantity) VALUES ('KFC', 19.12, 200), ('Doner', 6.28, 500), ('Hamburger', 12.37, 300), ('strawberries in chocolate', 50.40, 1000), ('Pizza', 34.20, 400);
# INSERT 0 5
# onlinestore=# select * from products;
#  id |           name            | price | quantity 
# ----+---------------------------+-------+----------
#   1 | Mcdonalds                 |     5 |      100
#   2 | KFC                       |    19 |      200
#   3 | Doner                     |     6 |      500
#   4 | Hamburger                 |    12 |      300
#   5 | strawberries in chocolate |    50 |     1000
#   6 | Pizza                     |    34 |      400
# (6 rows)

# onlinestore=# INSERT INTO orders (customer_id, order_date, total_amount) VALUES (3, '2024.03.03, 3300), (4, '2024.02.23', 4300), (5, '2024.01.05, 300), (6, '2024.01.30, 5000);
# onlinestore'# select * from products;
# onlinestore'# INSERT INTO products (name, price, quantity) VALUES ('KFC', 19.12, 200), ('Doner', 6.28, 500), ('Hamburger', 12.37, 300), ('strawberries in chocolate', 50.40, 1000), ('Pizza', 34.20, 400);
# onlinestore'# ^C
# onlinestore=# INSERT INTO products (name, price, quantity) VALUES ('KFC', 19.12, 200), ('Doner', 6.28, 500), ('Hamburger', 12.37, 300), ('strawberries in chocolate', 50.40, 1000), ('Pizza', 34.20, 400);
# INSERT 0 5
# onlinestore=# select * from products;
#  id |           name            | price | quantity 
# ----+---------------------------+-------+----------
#   1 | Mcdonalds                 |     5 |      100
#   2 | KFC                       |    19 |      200
#   3 | Doner                     |     6 |      500
#   4 | Hamburger                 |    12 |      300
#   5 | strawberries in chocolate |    50 |     1000
#   6 | Pizza                     |    34 |      400
#   7 | KFC                       |    19 |      200
#   8 | Doner                     |     6 |      500
#   9 | Hamburger                 |    12 |      300
#  10 | strawberries in chocolate |    50 |     1000
#  11 | Pizza                     |    34 |      400
# (11 rows)

# onlinestore=# select * from or;
# ERROR:  syntax error at or near "or"
# LINE 1: select * from or;
#                       ^
# onlinestore=# select * from orders;
#  id | customer_id | order_date | total_amount 
# ----+-------------+------------+--------------
#   4 |           1 | 2024-03-08 |         2000
# (1 row)

# onlinestore=# INSERT INTO orders (customer_id, order_date, total_amount) VALUES (3, '2024.03.03, 3300), (4, '2024.02.23', 4300), (5, '2024.01.05, 300), (6, '2024.01.30, 5000);
# onlinestore'# ^C
# onlinestore=# select * from orders;
#  id | customer_id | order_date | total_amount 
# ----+-------------+------------+--------------
#   4 |           1 | 2024-03-08 |         2000
# (1 row)

# onlinestore=# INSERT INTO orders (customer_id, order_date, total_amount) VALUES (3, '2024.03.03', 3300), (4, '2024.02.23', 4300), (5, '2024.01.05, 300), (6, '2024.01.30, 5000);INTO orders (customer_id, order_date, total_amount) VALUES (3, '2024.03.03, 3300), (4, '2024.02.23', 4300), (5, '2024.01.05,ERROR:  syntax error at or near "2024.01"
# LINE 1: ... '2024.02.23', 4300), (5, '2024.01.05, 300), (6, '2024.01.30...
#                                                              ^
# onlinestore=# INSERT INTO orders (customer_id, order_date, total_amount) VALUES (3, '2024-03-03', 3300), (4, '2024-02-23', 4300), (5, '2024-01-05', 300), (6, '2024.01.30', 5000);
# INSERT 0 4
# onlinestore=# select * from orders;
#  id | customer_id | order_date | total_amount 
# ----+-------------+------------+--------------
#   4 |           1 | 2024-03-08 |         2000
#   5 |           3 | 2024-03-03 |         3300
#   6 |           4 | 2024-02-23 |         4300
#   7 |           5 | 2024-01-05 |          300
#   8 |           6 | 2024-01-30 |         5000
# (5 rows)

# onlinestore=# UPDATE products SET price=10 WHERE id=1;
# UPDATE 1
# onlinestore=# select * from products;
#  id |           name            | price | quantity 
# ----+---------------------------+-------+----------
#   2 | KFC                       |    19 |      200
#   3 | Doner                     |     6 |      500
#   4 | Hamburger                 |    12 |      300
#   5 | strawberries in chocolate |    50 |     1000
#   6 | Pizza                     |    34 |      400
#   7 | KFC                       |    19 |      200
#   8 | Doner                     |     6 |      500
#   9 | Hamburger                 |    12 |      300
#  10 | strawberries in chocolate |    50 |     1000
#  11 | Pizza                     |    34 |      400
#   1 | Mcdonalds                 |    10 |      100
# (11 rows)

# onlinestore=# UPDATE products SET quantity=99 WHERE id=1;
# UPDATE 1
# onlinestore=# select * from products;
#  id |           name            | price | quantity 
# ----+---------------------------+-------+----------
#   2 | KFC                       |    19 |      200
#   3 | Doner                     |     6 |      500
#   4 | Hamburger                 |    12 |      300
#   5 | strawberries in chocolate |    50 |     1000
#   6 | Pizza                     |    34 |      400
#   7 | KFC                       |    19 |      200
#   8 | Doner                     |     6 |      500
#   9 | Hamburger                 |    12 |      300
#  10 | strawberries in chocolate |    50 |     1000
#  11 | Pizza                     |    34 |      400
#   1 | Mcdonalds                 |    10 |       99
# (11 rows)

