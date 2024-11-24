import sqlite3
import random
import string
from datetime import datetime, timedelta
# Connect to the SQLite database
#db_path = '/mnt/data/FRONTTOBACK DEVELOPMENT - CLIENT AND EMPLOYEE DATABASE SYSTEM.db'
connection = sqlite3.connect("FRONTTOBACK DEVELOPMENT - CLIENT AND EMPLOYEE DATABASE SYSTEM.db")

# Get the cursor to execute SQL commands
cursor = connection.cursor()

# Retrieve the schema of the database
schema_query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = cursor.execute(schema_query).fetchall()

# Get the details of each table
table_schemas = {}
for (table_name,) in tables:
    table_info_query = f"PRAGMA table_info({table_name});"
    columns = cursor.execute(table_info_query).fetchall()
    table_schemas[table_name] = columns
connection.commit()
# Close the connection
connection.close()

table_schemas
# Function to generate random names
def random_name():
    first_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'Daisy', 'Ella', 'Frank', "Johnson", "Jones", "Williams", "Garcia", "Smith", "Brown", "Lee", "Harris", "Walker", "Martinez"]
    last_names = ['Smith', 'Doe', 'Brown', 'Johnson', 'Williams', 'Jones', 'Garcia', 'Martinez', "John", "Daisy", "Ella", "Alice", "Michael", "Chris", "Sarah", "Robert", "Linda", "Karen"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to generate random phone numbers
def random_phone():
    return f"+1-{random.randint(100, 999)}-{random.randint(100, 9999)}"

# Function to generate random emails
def random_email(name):
    domain = random.choice(["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"])
    return f"{name.replace(' ', '.').lower()}@{domain}"

# Function to generate random dates
def random_date(start_date, end_date):
    return (start_date + timedelta(days=random.randint(0, (end_date - start_date).days))).strftime('%Y-%m-%d')

#Connect to the SQLite database again to insert data
connection = sqlite3.connect("FRONTTOBACK DEVELOPMENT - CLIENT AND EMPLOYEE DATABASE SYSTEM.db")
cursor = connection.cursor()

# Populate employeeTable
for i in range(25):
    employeeID = f"E{i+1:03}"
    employeeName = random_name()
    employeeAddress = f"{random.randint(100, 999)} {random.choice(['Main St', 'Second St', 'Third St', 'Fourth St', 'Road Ln', 'Park Rd', 'Grove Rd', 'Ducking Ln', 'Privet Drive', 'Cortis Rd', 'Sydney Rd', 'Upper Park' , 'Baker St', 'New Rd', 'North St', 'Mead Ln', 'Kings Way', 'Berwick Close'])}"
    employeeDOB = random_date(datetime(1980, 1, 1), datetime(2000, 1, 1))
    employeePhone = random_phone()
    employeeEmail = random_email(employeeName)
    employeeJobTitle = random.choice(['Manager', 'Developer', 'Designer', 'Analyst', 'Security Engineer', 'Consultant', 'Administrator'])
    employeePosition = random.choice(['Full-Time', 'Part-Time', 'Volunteer'])
    employeeHireDate = random_date(datetime(2015, 1, 1), datetime(2024, 1, 1))
    employeeSalary = f"${random.randint(50000, 120000)}"

    cursor.execute('''INSERT INTO employeeTable (employeeID, employeeName, employeeAddress, employeeDOB, employeePhone, 
                      employeeEmail, employeeJobTitle, employeePosition, employeeHireDate, employeeSalary) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                   (employeeID, employeeName, employeeAddress, employeeDOB, employeePhone, 
                    employeeEmail, employeeJobTitle, employeePosition, employeeHireDate, employeeSalary))

def random_product_id():
    return f"P{random.randint(1000, 9999)}"

# Function to populate clientTable with random data
def populate_client_table(n=10):
    for _ in range(n):
        clientID = f"C{random.randint(100, 999)}"
        clientName = random_name()
        clientAddress = f"{random.randint(100, 999)} {random.choice(['Main St', 'Second St', 'Third St', 'Park Ave', 'High St'])}"
        clientPhone = random_phone()
        clientEmail = random_email(clientName)
        contactPerson = random_name()
        
        cursor.execute('''INSERT OR IGNORE INTO clientTable (clientID, clientName, clientAddress, clientPhone, clientEmail, contactPerson)
                          VALUES (?, ?, ?, ?, ?, ?)''', 
                       (clientID, clientName, clientAddress, clientPhone, clientEmail, contactPerson))
    connection.commit()
    print(f"{n} random clients inserted into clientTable.")


# Helper function to generate random data
def random_description():
    descriptions = [
        "Office supplies", "Consulting services", "IT support",
        "Product design", "Marketing campaign", "Data analysis",
        "Training session", "Project management", "Security audit",
        "Inventory audit", "System upgrade", "Software development"
    ]
    return random.choice(descriptions)

def random_client_id():
    # Assuming client IDs are in the format "C001", "C002", etc.
    return f"C{random.randint(100, 999):03}"

def random_employee_id():
    # Assuming employee IDs are in the format "E001", "E002", etc.
    return f"E{random.randint(1, 25):03}"

# Function to populate orderTable with random data
def populate_order_table(n=10):
    for _ in range(n):
        orderID = f"O{random.randint(1000, 9999)}"  # Unique order ID
        clientID = random_client_id()  # Random client ID
        employeeID = random_employee_id()  # Random employee ID
        description = random_description()  # Random order description
        price = round(random.uniform(50.0, 500.0), 2)  # Random price between $50 and $500
        
        # Insert the new record into orderTable
        cursor.execute('''INSERT OR IGNORE INTO orderTable (orderID, clientID, employeeID, description, price)
                          VALUES (?, ?, ?, ?, ?)''', 
                       (orderID, clientID, employeeID, description, price))
    connection.commit()
    print(f"{n} random orders inserted into orderTable.")

# Usage
populate_order_table(10)  # Adjust the number of records as needed



# Close the database connection after insertion
connection.commit()
connection.close()

"Database populated with random data."
