import sqlite3
import random
from datetime import datetime, timedelta

# Establish database connection and create a cursor
connection = sqlite3.connect("FRONTTOBACK DEVELOPMENT - CLIENT AND EMPLOYEE DATABASE SYSTEM.db")
cursor = connection.cursor()

# Function to generate a random date within a specified range
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

# Function to generate random descriptions
def random_description():
    descriptions = [
        "Office supplies", "Consulting services", "IT support",
        "Product design", "Marketing campaign", "Data analysis",
        "Training session", "Project management", "Security audit",
        "Inventory audit", "System upgrade", "Software development"
    ]
    return random.choice(descriptions)

def random_employee_id():
    # Assuming employee IDs follow the format "E001", "E002", etc.
    return f"E{random.randint(1, 25):03}"

# Function to populate orderTable with random data linking to employeeID
def populate_order_table(n=10):
    for _ in range(n):
        orderID = f"O{random.randint(1000, 9999)}"
        clientID = f"C{random.randint(100, 999)}"  # Assuming clientIDs in the same range as in populate_client_table
        employeeID = random_employee_id()  # Generate a random employee ID
        orderDate = random_date(datetime(2021, 1, 1), datetime(2024, 12, 31))
        description = random_description()  # Random description of the order
        totalPrice = round(random.uniform(50.0, 500.0), 2)  # Random price between $50 and $500
        
        cursor.execute('''INSERT OR IGNORE INTO orderTable (orderID, clientID, employeeID, orderDate, description, totalPrice)
                          VALUES (?, ?, ?, ?, ?, ?)''', 
                       (orderID, clientID, employeeID, orderDate, description, totalPrice))
    connection.commit()
    print(f"{n} random orders inserted into orderTable with employee links.")

# Usage
populate_order_table(10)   # Adjust the number of orders as needed

# Close the database connection after insertion
connection.close()
