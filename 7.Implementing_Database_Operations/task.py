import psycopg2

def table():
    conn = psycopg2.connect(dbname="demodb", user="postgres", password="1234", host="localhost", port="5432")

    cursor = conn.cursor()
    cursor.execute('''create table employees (Name Text, ID int, Age int);''')
    print("Table created successfully")

    conn.commit()
    conn.close()


# table()

def data():
    conn = psycopg2.connect(dbname="demodb", user="postgres", password="1234", host="localhost", port="5432")

    name = input("Enter name: ")
    id = input("Enter id: ")
    age = input("Enter age: ")
    cursor = conn.cursor()
    # cursor.execute('''insert into employees (Name, ID, Age) values("Akash",212,24);''')
    query = ('''insert into employees (Name, ID, Age) values(%s,%s,%s);''')
    cursor.execute(query,(name, id, age))

    print("Data added successfully")

    conn.commit()
    conn.close()

# data()


def extract():
    conn = psycopg2.connect(dbname="demodb", user="postgres", password="1234", host="localhost", port="5432")

    cursor = conn.cursor()
    cursor.execute('''select * from employees;''')
    print(cursor.fetchone())
    print("Data extracted successfully")

    conn.commit()
    conn.close()

# extract()


def cond_extract():
    conn = psycopg2.connect(dbname="demodb", user="postgres", password="1234", host="localhost", port="5432")

    cursor = conn.cursor()
    cursor.execute('''select name from employees where age = 24;''')
    # print(cursor.fetchone())
    print(cursor.fetchall())

    print("Data extracted successfully")

    conn.commit()
    conn.close()

# cond_extract()

def truncate():
    conn = psycopg2.connect(dbname="demodb", user="postgres", password="1234", host="localhost", port="5432")

    cursor = conn.cursor()
    cursor.execute('''truncate table employees;''')
    # print(cursor.fetchone())
    # print(cursor.fetchall())

    print("Data deleted successfully")

    conn.commit()
    conn.close()

truncate()