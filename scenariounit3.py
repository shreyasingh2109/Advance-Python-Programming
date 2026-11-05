####ques 1

import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", default="students.csv")
args = parser.parse_args()

with open(args.file, "r") as file:
    reader = csv.DictReader(file)
    students = list(reader)

print("Student Records:")
for student in students:
    print(student)

roll = input("Enter Roll Number to search: ")

found = False
for student in students:
    if student["RollNo"] == roll:
        print("Student Found:", student)
        found = True
        break

if not found:
    print("Student not found.")


####ques 2

import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", default="employee.csv")
args = parser.parse_args()

with open(args.file, "r") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

print("Employee Records:")
for employee in employees:
    print(employee)

emp_id = input("Enter Employee ID to search: ")

found = False
for employee in employees:
    if employee["EmployeeID"] == emp_id:
        print("Employee Found:", employee)
        found = True
        break

if not found:
    print("Employee not found.")



###ques 3

import csv
import re

with open("books.csv", "r") as file:
    reader = csv.DictReader(file)
    books = list(reader)

print("All Book Records:")
for book in books:
    print(book)

keyword = input("Enter title keyword: ")
pattern = r"^" + re.escape(keyword)

print("Matching Books:")
found = False

for book in books:
    if re.search(pattern, book["Title"], re.IGNORECASE):
        print(book)
        found = True

if not found:
    print("No matching books found.")



####ques 4

import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", default="mobiles.csv")
args = parser.parse_args()

with open(args.file, "r") as file:
    reader = csv.DictReader(file)
    mobiles = list(reader)

print("Mobile Records:")
for mobile in mobiles:
    print(mobile)

brand = input("Enter Brand Name: ")

found = False
for mobile in mobiles:
    if mobile["Brand"].lower() == brand.lower():
        print("Mobile Found:", mobile)
        found = True

if not found:
    print("No mobile found for this brand.")



####ques 5

import csv

with open("patients.csv", "r") as file:
    reader = csv.DictReader(file)
    patients = list(reader)

print("Patient Records:")
for patient in patients:
    print(patient)

patient_id = input("Enter Patient ID to search: ")

found = False
for patient in patients:
    if patient["PatientID"] == patient_id:
        print("Patient Found:", patient)
        found = True
        break

if not found:
    print("Patient not found.")




#####ques 6

import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", default="grocery.csv")
args = parser.parse_args()

with open(args.file, "r") as file:
    reader = csv.DictReader(file)
    items = list(reader)

print("Grocery Inventory:")
for item in items:
    print(item)

item_id = input("Enter Item ID to search: ")

found = False
for item in items:
    if item["ItemID"] == item_id:
        print("Item Found:", item)
        found = True
        break

if not found:
    print("Item not found.")




#####ques 7

import csv
import re

with open("customers.csv", "r") as file:
    reader = csv.DictReader(file)
    customers = list(reader)

print("Customer Records:")
for customer in customers:
    print(customer)

account = input("Enter Account Number: ")

pattern = r"^[0-9]{10,16}$"

if not re.fullmatch(pattern, account):
    print("Invalid Account Number Format.")
else:
    found = False

    for customer in customers:
        if customer["AccountNumber"] == account:
            print("Customer Found:", customer)
            found = True
            break

    if not found:
        print("Customer not found.")





####ques 8

import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", default="courses.csv")
args = parser.parse_args()

with open(args.file, "r") as file:
    reader = csv.DictReader(file)
    courses = list(reader)

print("Course Records:")
for course in courses:
    print(course)

course_id = input("Enter Course ID to search: ")

found = False
for course in courses:
    if course["CourseID"] == course_id:
        print("Course Found:", course)
        found = True
        break

if not found:
    print("Course not found.")




#####ques 9

import csv
import re

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    movies = list(reader)

print("Movie Records:")
for movie in movies:
    print(movie)

movie_id = input("Enter Movie ID to search: ")

found = False
for movie in movies:
    if movie["MovieID"] == movie_id:
        print("Movie Found:", movie)
        found = True
        break

if not found:
    print("Movie not found.")

keyword = input("Enter movie title keyword: ")

print("Movies matching title:")
found = False

for movie in movies:
    if re.search(re.escape(keyword), movie["Title"], re.IGNORECASE):
        print(movie)
        found = True

if not found:
    print("No matching movies found.")




######ques 10

import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", default="sports.csv")
args = parser.parse_args()

with open(args.file, "r") as file:
    reader = csv.DictReader(file)
    equipment = list(reader)

print("Sports Equipment Records:")
for item in equipment:
    print(item)

equipment_id = input("Enter Equipment ID to search: ")

found = False
for item in equipment:
    if item["EquipmentID"] == equipment_id:
        print("Equipment Found:", item)
        found = True
        break

if not found:
    print("Equipment not found.")
