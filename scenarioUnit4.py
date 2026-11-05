### ques 1
import numpy as np
import pandas as pd

# Create NumPy array
marks = np.array([75, 85, 90, 65, 95])

# Statistical calculations
print("Mean Marks:", np.mean(marks))
print("Median Marks:", np.median(marks))
print("Maximum Marks:", np.max(marks))
print("Minimum Marks:", np.min(marks))

# Create DataFrame
df = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E"],
    "Marks": marks
})

print("\nStudent Records:")
print(df)

# Students scoring more than 80
print("\nStudents scoring more than 80:")
print(df[df["Marks"] > 80])



#####ques 2

import numpy as np
import pandas as pd

# Create NumPy array
salary = np.array([45000, 65000, 55000, 80000, 70000])

# Statistical calculations
print("Average Salary:", np.mean(salary))
print("Maximum Salary:", np.max(salary))
print("Minimum Salary:", np.min(salary))

# Create DataFrame
df = pd.DataFrame({
    "Employee": ["A", "B", "C", "D", "E"],
    "Salary": salary
})

print("\nEmployee Records:")
print(df)

# Employees earning more than 60000
print("\nEmployees earning more than 60000:")
print(df[df["Salary"] > 60000])


####ques 3

import numpy as np
import pandas as pd

# Create NumPy array
prices = np.array([15000, 25000, 35000, 45000, 20000])

# Statistical calculations
print("Mean Price:", np.mean(prices))
print("Median Price:", np.median(prices))
print("Maximum Price:", np.max(prices))
print("Minimum Price:", np.min(prices))

# Create DataFrame
df = pd.DataFrame({
    "Mobile": ["Samsung", "Redmi", "iPhone", "OnePlus", "Realme"],
    "Price": prices
})

print("\nMobile Records:")
print(df)

# Mobiles costing more than 30000
print("\nMobiles costing more than 30000:")
print(df[df["Price"] > 30000])



####ques 4

import numpy as np
import pandas as pd

# Create NumPy array
prices = np.array([250, 450, 600, 800, 350])

# Calculate average price
print("Average Book Price:", np.mean(prices))

# Create DataFrame
df = pd.DataFrame({
    "Book": ["Python", "DSA", "Java", "AI", "C Programming"],
    "Price": prices
})

print("\nBook Records:")
print(df)

# Books costing more than 500
print("\nBooks costing more than 500:")
print(df[df["Price"] > 500])



####ques 5

import numpy as np
import pandas as pd

# Create NumPy array
bills = np.array([2500, 3500, 1800, 4200, 3000])

# Statistical calculations
print("Mean Bill:", np.mean(bills))
print("Median Bill:", np.median(bills))
print("Maximum Bill:", np.max(bills))
print("Minimum Bill:", np.min(bills))

# Create DataFrame
df = pd.DataFrame({
    "Consumer": ["A", "B", "C", "D", "E"],
    "Bill": bills
})

print("\nElectricity Bill Records:")
print(df)

# Consumers whose bill exceeds 3000
print("\nConsumers whose bill exceeds 3000:")
print(df[df["Bill"] > 3000])


####ques 6

import numpy as np
import pandas as pd

# Create NumPy array
runs = np.array([3500, 5200, 4800, 7000, 6100])

# Statistical calculations
print("Average Runs:", np.mean(runs))
print("Highest Runs:", np.max(runs))
print("Lowest Runs:", np.min(runs))

# Create DataFrame
df = pd.DataFrame({
    "Player": ["Player A", "Player B", "Player C",
               "Player D", "Player E"],
    "Runs": runs
})

print("\nCricket Records:")
print(df)

# Players scoring more than 5000 runs
print("\nPlayers scoring more than 5000 runs:")
print(df[df["Runs"] > 5000])



####ques 7

import numpy as np
import pandas as pd

# Create NumPy array
costs = np.array([15000, 25000, 18000, 40000, 30000])

# Statistical calculations
print("Mean Treatment Cost:", np.mean(costs))
print("Maximum Treatment Cost:", np.max(costs))
print("Minimum Treatment Cost:", np.min(costs))

# Create DataFrame
df = pd.DataFrame({
    "Patient": ["A", "B", "C", "D", "E"],
    "Treatment Cost": costs
})

print("\nHospital Records:")
print(df)

# Patients with treatment cost above 20000
print("\nPatients with treatment cost above 20000:")
print(df[df["Treatment Cost"] > 20000])



#####ques 8

import numpy as np
import pandas as pd

# Create NumPy array of product prices
prices = np.array([100, 250, 500, 150, 300])

# Statistical calculations
print("Mean Price:", np.mean(prices))
print("Median Price:", np.median(prices))
print("Maximum Price:", np.max(prices))
print("Minimum Price:", np.min(prices))

# Create DataFrame
df = pd.DataFrame({
    "Product": ["Rice", "Sugar", "Oil", "Wheat", "Milk"],
    "Price": prices,
    "Quantity": [15, 8, 5, 20, 6]
})

print("\nGrocery Records:")
print(df)

# Grocery items having quantity less than 10
print("\nItems having quantity less than 10:")
print(df[df["Quantity"] < 10])




#####ques 9

import numpy as np
import pandas as pd

# Create NumPy array
fees = np.array([20000, 30000, 25000, 40000, 15000])

# Statistical calculations
print("Average Course Fee:", np.mean(fees))
print("Maximum Course Fee:", np.max(fees))
print("Minimum Course Fee:", np.min(fees))

# Create DataFrame
df = pd.DataFrame({
    "Course": ["Python", "Data Science", "AI",
               "Machine Learning", "Web Development"],
    "Fee": fees
})

print("\nCourse Records:")
print(df)

# Courses costing more than 25000
print("\nCourses costing more than 25000:")
print(df[df["Fee"] > 25000])



####ques10

import numpy as np
import pandas as pd

# Create NumPy array
rents = np.array([2500, 4500, 3500, 6000, 5000])

# Statistical calculations
print("Mean Rent:", np.mean(rents))
print("Median Rent:", np.median(rents))
print("Maximum Rent:", np.max(rents))
print("Minimum Rent:", np.min(rents))

# Create DataFrame
df = pd.DataFrame({
    "Room": ["Room 101", "Room 102", "Room 103",
             "Room 104", "Room 105"],
    "Rent": rents
})

print("\nHotel Room Records:")
print(df)

# Rooms having rent greater than 4000
print("\nRooms having rent greater than 4000:")
print(df[df["Rent"] > 4000])
