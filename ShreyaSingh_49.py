#####question 1 
import re
passwords = ["python@123", "python123"]

pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).+$'

for password in passwords:
    if re.match(pattern, password):
        print(password, "valid password")
    else:
        print(password, "invalid password")


import re 
passwords=["python@123","python123"]
pattern=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@#])'





#### question 2
import pandas as pd

salary = pd.Series([25000, 35000, 45000, 50000, 30000, 60000, 40000, 55000, 70000, 32000])

print("Employee Salaries:")
print(salary)

print("\nSalary at index position 3:")
print(salary[3])

print("\nSalaries greater than 40000:")
print(salary[salary > 40000])


print("\nMean Salary:", salary.mean())


print("Median Salary:", salary.median())

print("Maximum Salary:", salary.max())

print("Minimum Salary:", salary.min())