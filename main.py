import sqlite3
from flask import Flask, jsonify, render_template, url_for, request, redirect
import queries
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/employees", methods = ['GET'])
def get_employees():
    employees = queries.get_employees()
    return jsonify(employees)

@app.route("/employee", methods=['POST'])
def insert_employee():
    employee_details = request.get_json()
    NAME = employee_details["NAME"]
    AGE = employee_details['AGE']
    ADDRESS = employee_details['ADDRESS']
    SALARY = employee_details['SALARY']
    result = queries.insert_employee(NAME, AGE, ADDRESS, SALARY)
    return jsonify(result)

@app.route("/employee", methods = ["PUT"])
def update_employee():
    employee_details = request.get_json()
    ID = employee_details["ID"]
    NAME = employee_details["NMAE"]
    AGE = employee_details["AGE"]
    ADDRESS = employee_details["ADDRESS"]
    SALARY = employee_details["SALARY"]
    result = queries.update_employee(ID, NAME, AGE, ADDRESS, SALARY)
    return jsonify(result)

@app.route("/employee/<NAME>", methods = ["DELETE"])
def delete_employee(NAME):
    result = queries.delete_employee(NAME)
    return jsonify(result)

@app.route("/employee/<NAME>", methods = ["GET"])
def get_by_name(NAME):
    employee = queries.get_by_name(NAME)
    return jsonify(employee)

if __name__ == "__main__":
    app.run(debug = True)