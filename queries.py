import sqlite3

conn = sqlite3.connect('employee.db')

cur = conn.cursor()

def insert_employee(NAME, AGE, ADDRESS, SALARY):
    conn = sqlite3.connect('employee.db')
    cur = conn.cursor()
    statement = "INSERT INTO EMP(NAME, AGE, ADDRESS, SALARY) VALUES (?, ?, ?, ?)"
    cur.execute(statement, [NAME, AGE, ADDRESS, SALARY])
    conn.commit()
    return True

def update_employee(ID, NAME, AGE, ADDRESS, SALARY):
    conn = sqlite3.connect('employee.db')
    cur = conn.cursor()
    statement = "UPDATE EMP SET NAME = ?, AGE = ?, ADDRESS = ?, SALARY = ? WHERE ID = ?"
    cur.execute(statement, [NAME, AGE, ADDRESS, SALARY])
    conn.commit()
    return True

def delete_employee(NAME):
    conn = sqlite3.connect('employee.db')
    cur = conn.cursor()
    statement = "DELETE FROM EMP WHERE NAME = ?"
    cur.execute(statement, [NAME])
    conn.commit()
    return True

def get_by_name(NAME):
    conn = sqlite3.connect('employee.db')
    cur = conn.cursor()
    statement = "SELECT ID, NAME, AGE, ADDRESS, SALARY FROM EMP WHERE NAME = ?"
    cur.execute(statement, [NAME])
    return cur.fetchone()

def get_employees():
    conn = sqlite3.connect('employee.db')
    cur = conn.cursor()
    statement = "SELECT ID, NAME, AGE, ADDRESS, SALARY FROM EMP"
    cur.execute(statement)
    return cur.fetchall()