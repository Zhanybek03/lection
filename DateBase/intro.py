# PostgreSQL - Система управления базами данных(СУБД/DBMS)
# Это ряд програм и инструментов позволяющих создавать БД, управлять ею и манипулировать данными внутри(CRUD)
# Postges - сама база данных, она объектно реляционная, то есть данные хранятся в виде таблиц, и таблицы имеют связи между собой


# SQL (Structured Query language) - декларативный язык структуриванных запросов, он применяеться для создания и получения данных при помощи запросов в БД


# ______________________________________---
# команда для входа в бд через юзера postgres:
# sudo -u postgres psql

# команда для входа в своего юзера 
# psql

# создание суперюзера 
# CREATE ROLE 'username' SUPERUSER LOGIN PASSWORD '1';

# изменение пароля 
# ALTER USER 'username' WITH PASSWORD '1';

# to create DB\
# CREATE DATABASE 'name';

# \l - список всех бд

# \du - все юзеры

# \c 'name' - команда для подключения к бд

# \dt - все твблицы (нужно подключиться к бд зврвнее)

# \d 'name' - подробная информация про таблицу (нужно подкючиться к бд заранее)

# psql -U <username> -d <dbname> -подключаемся под выбранным username к dbname

# \q - выход либо назад 

# --------------------------------
# Типы полей в Postgres

# Numeric Types(числовые типы)
    # a. smallint(2 bytes) -> -32767 to 32767
    # b. integer(4 bytes) -> -2.147... to 2.147...
    # c. bigint(8 bytes) -> ...
    # d. real (4 bytes) -> число с плавающий точкой, вещественное
    # f. serial (4 bytes) -> integer, auto-increment

# Character types(Символьные типы(стоковых)):
    # a. varchar(кол-во символов) -> если мы укажем 50. символов, а заполним только 10, то остальные будут свободны. Макс 255
    # b. char(кол-во символ) -> если мы укажем 50 символов, а заполним только 10, то оствльные будут заполнены пробелом. Макс 255
    # с. text() -> неогр кол-вщ символов

# Boolen Type 
    # a. boolean(1 bytes) -> True/False

# date -> календарная дата (год. месяц. день)

# location -> координантная точка (x, y) - (254, - 12)

# enumerate types:
    # ('a', 'b', 'c')
    # CREATE TYPE <any name> AenumUM ('Happy', 'Sad', 'Mad');

# -------------------------------

# Команда для добавления данных в табл
# INSERT INTO <tablename> [(columns)] VALUES (data), (data);

# Команда для обновления данных
# UPDATE <table> SET <column> = <new_value> WHERE <column> = <value>;

# Команда для удаления данных
# DELETE FROM <table> WHERE <column> = <value>;


# Команда для получения данных 
# SELECT (colums)* FROM <table>


#  ORDER BY: Позволяет нам сортировать выводящие данные по убыванию или возрастанию. ASC(по возрастанию) и DESС(по убыванию)

# Синтаксис: SELECT <row> FROM <tablename>  ORDER BY <row> [ASC/DESC]


# WHERE: используется для фильтрации по полям. Будут выводится те данные которые соответсвуют условию оператора WHERE
# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> = 'чему либо'

# BETWEEN: условие между
# SELECT * FROM products WHERE id BETWEEN 3 and 8 

# AND оператор и, для множественных условий 
# IN: WHERE <row> in (1, 2, 3, 4);
# LIMIT: ставит ограничение в кол-во получаемых данных


# LIKE: Выводит результат который соответствует ввуденному шаблону для строк. Чувствителен к регистру 
# ILIKE: тоже самое только не зависит от регистра 
# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> LIKE/ILIKE 'чем либо';

# GROUP BY: разделяет данные которые мы получаем в SELECT, при этом группируя их по определенному признаку. И теперь для каждой группы можно исп функцию 
# HAVING: ставит условие при пломози которого данные отбираются в группировка
# ---------------------------------- В тандеме
# Агрегатные функции: AVG(), COUNT(), MIN(), MAX(), SUM()

# Экспорт бд(дамп):
# pg_dump -U <username> -d 'dbname' > 'file.sql'

# Импорт:
# psql -U <username> -d <dbname> -f <filename> 


#  --------------------------------------------

# Ограничения:
    # 1. NOT NULL - обязательно к заполнению
    # 2. UNIQUE - будет хранится только уникальные данные 
    # 3. CHECK -> CHECK age > -1 - ограничение проверки на условие
    # 4. PRIMARY KEY(для установки идентификатора данных в талблице)
    # 5. FOREIGN KEY(для установки связей между тадлицами)
    # 6. ON DELETE - для установки поведение при удаление данных которые были связаны 
# ----------------------------------------

# JOIN: выборка данных из двух талбл, соединение табл

# LEFT JOIN: выборка будет содержать все строки из левой табл

# RIGHT JOIN: выборка будет содержать все строки из правой табл

# SELECT p1.title, p1.price, o1.quantity, p1.price * o1.quantity as total_sum FROM products p1, orders o1 WHERE p1.id = o1.product_id;
#  - Запросы сразу в дву табл

# SELECT p1.title, p1.price, o1.quantity, p1.price * o1.quantity as total_sum FROM products p1, JOIN orders o1 WHERE p1.id = o1.product_id;v

# ------------------------------------------------------x
