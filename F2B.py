#==============================================================================================
# FRONTTOBACK DEVELOPMENT - EMPLOYEE AND CLIENT MANAGEMENT SYSTEM             Gafar Aleshe
# USING AN SQL DATABASE                                   PROJECT START DATE: APRIL 2024
# TABLES - employeeTable, clientTable, ordersTable, departmentTable, payrollTable, leaveRequestTable
# INCLUDES - client information and invoices
#
# This code initializes and manages a SQLite database for an Employee and Client Management System. 
# It includes functionality to:
# 
# 1. **Create and Initialize Database**:
#    - Checks if the database file exists. If not, creates a new database file.
#    - Creates tables for employees, clients, orders, departments, attendance, payroll, and leave requests with appropriate schema.
# 
# 2. **Main Menu**:
#    - Provides a main menu interface for the user to choose between different management sections (Employee, Client, Job, Exit).
# 
# 3. **Employee Menu**:
#    - Allows users to display all employees, add a new employee, edit existing employee details, or delete an employee.
#    - Functions ensure that operations on the employee data are performed safely and efficiently.
# 
# 4. **Client Management**:
#    - Manage client information, including adding, editing, and deleting client records. This section is not fully detailed here but follows a similar structure to the employee management functions.
# 
# 5. **Database Operations**:
#    - Executes SQL commands to interact with the database, including creating tables, inserting, updating, and deleting records.
#    - Ensures data integrity with proper foreign key relationships and handles potential errors in database operations.
# 
# The system supports basic CRUD (Create, Read, Update, Delete) operations for employee and client records and integrates with other tables to manage related data.
#==============================================================================================

#### IMPORTS ####

import sqlite3
from os.path import isfile
import os
from datetime import datetime

#=======================================================================================

#### GLOBAL DECLARATIONS ####

# DATABASE - If the database exists in the same folder as the program it will be opened.
#            If it does not exist it will be created with an empty employeeTable.

newDatabase = not isfile("FRONTTOBACK DEVELOPMENT - CLIENT AND EMPLOYEE DATABASE SYSTEM.db")   # newDatabase is True or False  
           
# OPEN OR CREATE THE DATABASE - AS A GLOBAL    
fronttoback = sqlite3.connect("FRONTTOBACK DEVELOPMENT - CLIENT AND EMPLOYEE DATABASE SYSTEM.db")
 
# IF THIS IS A NEW DATABASE - CREATE THE DATABASE TABLES        
if newDatabase:

    print("The database 'FRONTTOBACK DEVELOPMENT - CLIENT AND EMPLOYEE DATABASE SYSTEM.db' does not exist")
    print("It will be created with tables - users, client, job.")
   
    sqlCommand =  "CREATE TABLE employeeTable("
    sqlCommand += "employeeID TEXT PRIMARY KEY,"
    sqlCommand += "employeeName TEXT,"
    sqlCommand += "employeeAddress TEXT,"
    sqlCommand += "employeeDOB TEXT,"
    sqlCommand += "employeePhone TEXT,"
    sqlCommand += "employeeEmail TEXT,"
    sqlCommand += "employeeJobTitle TEXT,"
    sqlCommand += "employeePosition TEXT,"
    sqlCommand += "employeeHireDate TEXT,"
    sqlCommand += "employeeSalary TEXT)"
    
    fronttoback.execute(sqlCommand)
    fronttoback.commit()

    sqlCommand = "CREATE TABLE clientTable("
    sqlCommand += "clientID TEXT PRIMARY KEY, "
    sqlCommand += "clientName TEXT, "
    sqlCommand += "clientAddress TEXT, "
    sqlCommand += "clientPhone TEXT, "
    sqlCommand += "clientEmail TEXT, "
    sqlCommand += "contactPerson TEXT) "
   
    fronttoback.execute(sqlCommand)
    fronttoback.commit()
    
    # SQL command to create the orderTable
    sqlCommand = "CREATE TABLE IF NOT EXISTS orderTable("
    sqlCommand += "orderID TEXT PRIMARY KEY, "
    sqlCommand += "clientID TEXT, "
    sqlCommand += "employeeID TEXT, "
    sqlCommand += "description TEXT, "
    sqlCommand += "price REAL, "
    sqlCommand += "FOREIGN KEY (clientID) REFERENCES clientTable(clientID), "
    sqlCommand += "FOREIGN KEY (employeeID) REFERENCES employeeTable(employeeID))"

    # Execute the command
    fronttoback.execute(sqlCommand)
    fronttoback.commit()

    



#=======================================================================================

#### THE MAIN FUNCTION ####

def main():
    choice = "0"

    while choice != "x":
        print("")
        print("FRONTTOBACK EMPLOYEE - MAIN MENU")
        print("================================")
        print("1 - Employee Menu     ")
        print("2 - Client Menu       ")
        print("3 - Order Menu        ")
        print("4 - Invoice Generator ")
        print("x - Exit.             ")

        choice = input("\nEnter your choice : ")

        if choice == "1":
            employeeMenu()
        elif choice == "2":
            clientMenu()
        elif choice == "3":
            orderMenu()
        elif choice == "4":
            orderID = input("Enter the Order ID for the invoice: ")
            generate_invoice(orderID)
        elif choice == "x":
            fronttoback.close()
#=======================================================================================

def employeeMenu():
    choice = "0"

    while choice != "x":
        print("")
        print("FRONTTOBACK DEVELOPMENT - EMPLOYEE MENU")
        print("=======================================")
        print("1 - Display all Employees.")
        print("2 - Add a new Employee.")
        print("3 - Edit an Employee.")
        print("4 - Delete an Employee.")
        print("5 - Sort and Search Employee Records")
        print("x - Back to Main Menu.")

        choice = input("\nEnter your choice : ")
        print("")

        if choice == "1":
            displayAllEmployees()
##        if choice == "1":
##            display_sorted_employees(fetch_all_employees())
        elif choice == "2":
            addNewEmployee()
        elif choice == "3":
            editAnEmployee()
        elif choice == "4":
            deleteAnEmployee()
        elif choice == "5":
            employeeSortAndSearchMenu()

#---------------------------------------------------------------------------------------

def displayAllEmployees():
    print("FRONTTOBACK DEVELOPMENT - EMPLOYEE MENU")
    print("---------------------------------------")
    print(f"{'Emp ID':<8} {'Employee Name':<20} {'Address':<20} {'DOB':<12} {'Phone':<15} {'Email':<30} {'Job Title':<20} {'Position':<15} {'Hire Date':<12} {'Salary':<10}")
    print("-"*8, "-"*20, "-"*20, "-"*12, "-"*15, "-"*30, "-"*20, "-"*15, "-"*12, "-"*10)

    sqlCommand = "SELECT * FROM employeeTable"
    try:
        for record in fronttoback.execute(sqlCommand):
            print(f"{record[0]:<8} {record[1]:<20} {record[2]:<20} {record[3]:<12} {record[4]:<15} {record[5]:<30} {record[6]:<20} {record[7]:<15} {record[8]:<12} {record[9]:<10}")
    except Exception as e:
        print(f"Error: {e}")



#---------------------------------------------------------------------------------------

def addNewEmployee():
    print("NEW EMPLOYEE")
    print("------------")

    employeeID = input("Enter Employee ID : ")
    employeeName = input("Enter Employee Name : ")
    employeeAddress = input("Enter Employee Address : ")
    employeeDOB = input("Enter Date of Birth (YYYY-MM-DD) : ")
    employeePhone = input("Enter Phone Number : ")
    employeeEmail = input("Enter Email : ")
    employeeJobTitle = input("Enter Job Title : ")
    employeePosition = input("Enter Position : ")
    employeeHireDate = input("Enter Hire Date (YYYY-MM-DD) : ")
    employeeSalary = input("Enter Salary : ")

    newEmployeeRecord = [employeeID, employeeName, employeeAddress, employeeDOB, employeePhone, employeeEmail, employeeJobTitle, employeePosition, employeeHireDate, employeeSalary]

    sqlCommand = "INSERT INTO employeeTable VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

    try:
        fronttoback.execute(sqlCommand, newEmployeeRecord)
        fronttoback.commit()
        print("\n** New Employee has been added **")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


#---------------------------------------------------------------------------------------

def editAnEmployee():
    print("EDIT EMPLOYEE DETAILS")
    print("---------------------")

    employeeIDToEdit = input("Enter the Employee ID of the Employee to Edit : ")

    sqlCommand = "SELECT * FROM employeeTable WHERE employeeID = ?"

    try:
        queryResult = fronttoback.execute(sqlCommand, (employeeIDToEdit,))
        employeeToEdit = queryResult.fetchone()

        if employeeToEdit is None:
            print("Employee ID not found.")
            return

        print("\nThe Employee to Edit...")
        print("")
        print(f"{'1':<8} {'2':<20} {'3':<20} {'4':<12} {'5':<15} {'6':<25} {'7':<15} {'8':<15} {'9':<12} {'10':<10}")
        print(f"{'Emp ID':<8} {'Employee Name':<20} {'Address':<20} {'DOB':<12} {'Phone':<15} {'Email':<25} {'Job Title':<15} {'Position':<15} {'Hire Date':<12} {'Salary':<10}")
        print("-"*8, "-"*20, "-"*20, "-"*12, "-"*15, "-"*25, "-"*15, "-"*15, "-"*12, "-"*10)
        

        print("%-8s %-20s %-20s %-12s %-15s %-25s %-15s %-15s %-12s %-10s" %(employeeToEdit))
        fieldToEdit = int(input("\nEnter a Field Number to edit. Eg. 5 for Phone : "))
        newValue = input("\nEnter the new value for that field : ")

        fieldNames = ["employeeID", "employeeName", "employeeAddress", "employeeDOB", "employeePhone", "employeeEmail", "employeeJobTitle", "employeePosition", "employeeHireDate", "employeeSalary"]

        sqlCommand = f"UPDATE employeeTable SET {fieldNames[fieldToEdit - 1]} = ? WHERE employeeID = ?"
        fronttoback.execute(sqlCommand, (newValue, employeeIDToEdit))
        fronttoback.commit()

        print("\n** Record Updated **")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

#---------------------------------------------------------------------------------------

def deleteAnEmployee():
    print("DELETE AN EMPLOYEE FROM THE EMPLOYEE TABLE")
    print("------------------------------------------")

    employeeIDToRemove = input("Enter Employee ID : ")

    sqlCommand = "DELETE FROM employeeTable WHERE employeeID = ?"

    try:
        fronttoback.execute(sqlCommand, (employeeIDToRemove,))
        fronttoback.commit()
        print("\n** Employee " + employeeIDToRemove + " Deleted **")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

#---------------------------------------------------------------------------------------
        
#### SORT EMPLOYEES ####
# Function to sort and search employee records
# Fetch all employees from the database 
def fetch_all_employees():
    sqlCommand = "SELECT * FROM employeeTable"
    cursor = fronttoback.cursor()
    employees = cursor.execute(sqlCommand).fetchall()
    # Convert each employee record into a dictionary with column names as keys
    return [dict(zip([column[0] for column in cursor.description], row)) for row in employees]
# Fetch all clients from the database
def fetch_all_clients():
    sqlCommand = "SELECT * FROM clientTable"
    cursor = fronttoback.cursor()
    clients = cursor.execute(sqlCommand).fetchall()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in clients]

# Fetch all orders from the database
def fetch_all_orders():
    sqlCommand = "SELECT * FROM orderTable"
    cursor = fronttoback.cursor()
    orders = cursor.execute(sqlCommand).fetchall()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in orders]

def employeeSortAndSearchMenu():
    choice = "0"
    
    while choice != "x":
        print("")
        print("FRONTTOBACK DEVELOPMENT - EMPLOYEE SORT & SEARCH MENU")
        print("====================================================")
        print("1 - Sort Employees by Employee ID")
        print("2 - Sort Employees by Employee Name")
        print("3 - Search for an Employee by Employee ID")
        print("x - Back to Employee Menu.")
        
        choice = input("\nEnter your choice: ")
        print("")
        
        # Fetch all employees
        employees = fetch_all_employees()
        
        if choice == "1":
            merge_sort(employees, key="employeeID")
            display_sorted_employees(employees)
        elif choice == "2":
            merge_sort(employees, key="employeeName")
            display_sorted_employees(employees)
        elif choice == "3":
            target_id = input("Enter the Employee ID to search: ")
            merge_sort(employees, key="employeeID")  # Ensure list is sorted for binary search
            result = binary_search(employees, key="employeeID", target=target_id)
            if result:
                print("\nEmployee found:")
                print(result)
            else:
                print("\nEmployee not found.")
        elif choice == "x":
            break
        
#---------------------------------------------------------------------------------------
        
# Helper function to display sorted employee records
def display_sorted_employees(employees):
    print("Sorted Employee Records")
    print(f"{'Emp ID':<8} {'Employee Name':<20} {'Address':<20} {'DOB':<12} {'Phone':<15} {'Email':<30} {'Job Title':<20} {'Position':<15} {'Hire Date':<12} {'Salary':<10}")
    print("-"*8, "-"*20, "-"*20, "-"*12, "-"*15, "-"*30, "-"*20, "-"*15, "-"*12, "-"*10)
    
    for record in employees:
        print(f"{record['employeeID']:<8} {record['employeeName']:<20} {record['employeeAddress']:<20} {record['employeeDOB']:<12} "
              f"{record['employeePhone']:<15} {record['employeeEmail']:<30} {record['employeeJobTitle']:<20} "
              f"{record['employeePosition']:<15} {record['employeeHireDate']:<12} {record['employeeSalary']:<10}")

#---------------------------------------------------------------------------------------
        
# Merge Sort Function
def merge_sort(employees, key):
    if len(employees) > 1:
        mid = len(employees) // 2
        left_half = employees[:mid]
        right_half = employees[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i][key] < right_half[j][key]:
                employees[k] = left_half[i]
                i += 1
            else:
                employees[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            employees[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            employees[k] = right_half[j]
            j += 1
            k += 1
#---------------------------------------------------------------------------------------
            
# Binary Search Function
def binary_search(employees, key, target):
    left, right = 0, len(employees) - 1
    while left <= right:
        mid = (left + right) // 2
        if employees[mid][key] == target:
            return employees[mid]
        elif employees[mid][key] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None
    
#==============================================================================================

def clientMenu():
    choice = "0"

    while choice != "x":
        print("")
        print("FRONTTOBACK DEVELOPMENT - CLIENT MENU")
        print("=====================================")
        print("1 - Display all Clients.")
        print("2 - Add a new Client.")
        print("3 - Edit a Client.")
        print("4 - Delete a Client.")
        print("5 - Sort and Search Client Records")
        print("x - Back to Main Menu.")

        choice = input("\nEnter your choice : ")
        print("")

        if choice == "1":
            displayAllClients()
##        if choice == "1":  
##            display_sorted_clients(fetch_all_clients())
        elif choice == "2":
            addNewClient()
        elif choice == "3":
            editAClient()
        elif choice == "4":
            deleteAClient()
        elif choice == "5":
            clientSortAndSearchMenu()

#---------------------------------------------------------------------------------------

def displayAllClients():
    print("FRONTTOBACK DEVELOPMENT - CLIENT MENU")
    print("-------------------------------------")
    print(f"{'Client ID':<10} {'Client Name':<20} {'Address':<25} {'Phone':<15} {'Email':<30} {'Contact Person':<20}")
    print("-" * 10, "-" * 20, "-" * 25, "-" * 15, "-" * 30, "-" * 20)

    sqlCommand = "SELECT * FROM clientTable"
    try:
        
        for record in fronttoback.execute(sqlCommand):
            print(f"{record[0]:<10} {record[1]:<20} {record[2]:<25} {record[3]:<15} {record[4]:<30} {record[5]:<20}")
    except Exception as e:
        print(f"Error: {e}")

#---------------------------------------------------------------------------------------

def addNewClient():
    print("NEW CLIENT")
    print("----------")

    clientID = input("Enter Client ID : ")
    clientName = input("Enter Client Name : ")
    clientAddress = input("Enter Client Address : ")
    clientPhone = input("Enter Phone Number : ")
    clientEmail = input("Enter Email : ")
    contactPerson = input("Enter Contact Person : ")

    newClientRecord = [clientID, clientName, clientAddress, clientPhone, clientEmail, contactPerson]

    sqlCommand = "INSERT INTO clientTable VALUES (?, ?, ?, ?, ?, ?)"

    try:
        fronttoback.execute(sqlCommand, newClientRecord)
        fronttoback.commit()
        print("\n** New Client has been added **")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

#---------------------------------------------------------------------------------------

def editAClient():
    print("EDIT CLIENT DETAILS")
    print("-------------------")

    clientIDToEdit = input("Enter the Client ID of the Client to Edit : ")

    sqlCommand = "SELECT * FROM clientTable WHERE clientID = ?"

    try:
        queryResult = fronttoback.execute(sqlCommand, (clientIDToEdit,))
        clientToEdit = queryResult.fetchone()

        if clientToEdit is None:
            print("Client ID not found.")
            return

        print("\nThe Client to Edit...")
        print("")
        print(f"{'1':<10} {'2':<20} {'3':<25} {'4':<15} {'5':<30} {'6':<20}")
        print(f"{'Client ID':<10} {'Client Name':<20} {'Address':<25} {'Phone':<15} {'Email':<30} {'Contact Person':<20}")
        print("-" * 10, "-" * 20, "-" * 25, "-" * 15, "-" * 30, "-" * 20)

        print(f"{clientToEdit[0]:<10} {clientToEdit[1]:<20} {clientToEdit[2]:<25} {clientToEdit[3]:<15} {clientToEdit[4]:<30} {clientToEdit[5]:<20}")
        
        fieldToEdit = int(input("\nEnter a Field Number to edit. Eg. 4 for Phone : "))
        newValue = input("\nEnter the new value for that field : ")

        fieldNames = ["clientID", "clientName", "clientAddress", "clientPhone", "clientEmail", "contactPerson"]

        sqlCommand = f"UPDATE clientTable SET {fieldNames[fieldToEdit - 1]} = ? WHERE clientID = ?"
        fronttoback.execute(sqlCommand, (newValue, clientIDToEdit))
        fronttoback.commit()

        print("\n** Record Updated **")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

#---------------------------------------------------------------------------------------

def deleteAClient():
    print("DELETE A CLIENT FROM THE CLIENT TABLE")
    print("-------------------------------------")

    clientIDToRemove = input("Enter Client ID : ")

    sqlCommand = "DELETE FROM clientTable WHERE clientID = ?"

    try:
        fronttoback.execute(sqlCommand, (clientIDToRemove,))
        fronttoback.commit()
        print("\n** Client " + clientIDToRemove + " Deleted **")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

#---------------------------------------------------------------------------------------

# Function to sort and search client records

def clientSortAndSearchMenu():
    choice = "0"
    
    while choice != "x":
        print("")
        print("FRONTTOBACK DEVELOPMENT - CLIENT SORT & SEARCH MENU")
        print("===================================================")
        print("1 - Sort Clients by Client ID")
        print("2 - Sort Clients by Client Name")
        print("3 - Search for a Client by Client ID")
        print("x - Back to Client Menu.")
        
        choice = input("\nEnter your choice: ")
        print("")
        
        # Fetch all clients
        clients = fetch_all_clients()
        
        if choice == "1":
            merge_sort(clients, key="clientID")
            display_sorted_clients(clients)
        elif choice == "2":
            merge_sort(clients, key="clientName")
            display_sorted_clients(clients)
        elif choice == "3":
            target_id = input("Enter the Client ID to search: ")
            merge_sort(clients, key="clientID")  # Ensure list is sorted for binary search
            result = binary_search(clients, key="clientID", target=target_id)
            if result:
                print("\nClient found:")
                print(result)
            else:
                print("\nClient not found.")
        elif choice == "x":
            break
#---------------------------------------------------------------------------------------
# Display sorted client records
def display_sorted_clients(clients):
    print("Sorted Client Records")
    print(f"{'Client ID':<10} {'Client Name':<20} {'Address':<20} {'Phone':<15} {'Email':<30} {'Contact Person':<20}")
    print("-"*10, "-"*20, "-"*20, "-"*15, "-"*30, "-"*20)
    
    for record in clients:
        print(f"{record['clientID']:<10} {record['clientName']:<20} {record['clientAddress']:<20} "
              f"{record['clientPhone']:<15} {record['clientEmail']:<30} {record['contactPerson']:<20}")

# Display sorted order records
def display_sorted_orders(orders):
    print("Sorted Order Records")
    print(f"{'Order ID':<10} {'Client ID':<10} {'Product ID':<10} {'Order Date':<12} {'Quantity':<10} {'Total Price':<10}")
    print("-"*10, "-"*10, "-"*10, "-"*12, "-"*10, "-"*10)
    
    for record in orders:
        print(f"{record['orderID']:<10} {record['clientID']:<10} {record['productID']:<10} "
              f"{record['orderDate']:<12} {record['quantity']:<10} {record['totalPrice']:<10}")

#---------------------------------------------------------------------------------------
def orderMenu():
    choice = "0"

    while choice != "x":
        print("")
        print("FRONTTOBACK DEVELOPMENT - ORDER MENU")
        print("===================================")
        print("1 - Display all Orders.")
        print("2 - Add a new Order.")
        print("3 - Edit an Order.")
        print("4 - Delete an Order.")
        print("5 - Sort and Search Order Records")
        print("x - Back to Main Menu.")

        choice = input("\nEnter your choice : ")
        print("")

        if choice == "1":
            displayAllOrders()
        elif choice == "2":
            addNewOrder()
        elif choice == "3":
            editAnOrder()
        elif choice == "4":
            deleteAnOrder()
        elif choice == "5":
            orderSortAndSearchMenu()
        elif choice == "x":
            print("Returning to Main Menu.")
        else:
            print("Invalid choice. Please try again.")

#---------------------------------------------------------------------------------------
            
# Display all orders in orderTable
def displayAllOrders():
    print("FRONTTOBACK DEVELOPMENT - ORDER MENU")
    print("------------------------------------")
    print(f"{'Order ID':<10} {'Client ID':<10} {'Employee ID':<12} {'Description':<20} {'Price':<10}")
    print("-" * 10, "-" * 10, "-" * 12, "-" * 20, "-" * 10)
    
    sqlCommand = "SELECT * FROM orderTable"
    try:
        for record in fronttoback.execute(sqlCommand):
            print(f"{record[0]:<10} {record[1]:<10} {record[2]:<12} {record[3]:<20} {record[4]:<10.2f}")
    except Exception as e:
        print(f"Error: {e}")

#---------------------------------------------------------------------------------------

def addNewOrder():
    print("NEW ORDER")
    print("---------")

    orderID = input("Enter Order ID : ")
    clientID = input("Enter Client ID : ")
    employeeID = input("Enter Employee ID : ")
    description = input("Enter Description : ")
    price = float(input("Enter Price : "))

    newOrderRecord = [orderID, clientID, employeeID, description, price]

    sqlCommand = "INSERT INTO orderTable (orderID, clientID, employeeID, description, price) VALUES (?, ?, ?, ?, ?)"

    try:
        fronttoback.execute(sqlCommand, newOrderRecord)
        fronttoback.commit()
        print("\n** New Order has been added **")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


#---------------------------------------------------------------------------------------
def editAnOrder():
    print("EDIT ORDER DETAILS")
    print("------------------")

    orderIDToEdit = input("Enter the Order ID of the Order to Edit : ")

    sqlCommand = "SELECT * FROM orderTable WHERE orderID = ?"

    try:
        queryResult = fronttoback.execute(sqlCommand, (orderIDToEdit,))
        orderToEdit = queryResult.fetchone()

        if orderToEdit is None:
            print("Order ID not found.")
            return

        print("\nThe Order to Edit...")
        print("")
        print(f"{'1':<10} {'2':<10} {'3':<12} {'4':<20} {'5':<10}")
        print(f"{'Order ID':<10} {'Client ID':<10} {'Employee ID':<12} {'Description':<20} {'Price':<10}")
        print("-" * 10, "-" * 10, "-" * 12, "-" * 20, "-" * 10)

        print(f"{orderToEdit[0]:<10} {orderToEdit[1]:<10} {orderToEdit[2]:<12} {orderToEdit[3]:<20} {orderToEdit[4]:<10.2f}")
        
        fieldToEdit = int(input("\nEnter a Field Number to edit (2 for Client ID, 3 for Employee ID, 4 for Description, 5 for Price) : "))
        newValue = input("\nEnter the new value for that field : ")

        fieldNames = ["orderID", "clientID", "employeeID", "description", "price"]

        if fieldNames[fieldToEdit - 1] == "price":
            newValue = float(newValue)  # Convert price to float

        sqlCommand = f"UPDATE orderTable SET {fieldNames[fieldToEdit - 1]} = ? WHERE orderID = ?"
        fronttoback.execute(sqlCommand, (newValue, orderIDToEdit))
        fronttoback.commit()

        print("\n** Record Updated **")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    except IndexError:
        print("Invalid field selection.")

#---------------------------------------------------------------------------------------

def deleteAnOrder():
    print("DELETE AN ORDER FROM THE ORDER TABLE")
    print("------------------------------------")

    orderIDToRemove = input("Enter Order ID : ")

    sqlCommand = "DELETE FROM orderTable WHERE orderID = ?"

    try:
        fronttoback.execute(sqlCommand, (orderIDToRemove,))
        fronttoback.commit()
        print("\n** Order " + orderIDToRemove + " Deleted **")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

#---------------------------------------------------------------------------------------
# Function to sort and search order records

def orderSortAndSearchMenu():
    choice = "0"
    
    while choice != "x":
        print("")
        print("FRONTTOBACK DEVELOPMENT - ORDER SORT & SEARCH MENU")
        print("===================================================")
        print("1 - Sort Orders by Order ID")
        print("2 - Sort Orders by Client ID")
        print("3 - Search for an Order by Order ID")
        print("x - Back to Order Menu.")
        
        choice = input("\nEnter your choice: ")
        print("")
        
        # Fetch all orders
        orders = fetch_all_orders()
        
        if choice == "1":
            merge_sort(orders, key="orderID")
            display_sorted_orders(orders)
        elif choice == "2":
            merge_sort(orders, key="clientID")
            display_sorted_orders(orders)
        elif choice == "3":
            target_id = input("Enter the Order ID to search: ")
            merge_sort(orders, key="orderID")  # Ensure list is sorted for binary search
            result = binary_search(orders, key="orderID", target=target_id)
            if result:
                print("\nOrder found:")
                print(result)
            else:
                print("\nOrder not found.")
        elif choice == "x":
            break

# Display sorted order records with updated fields
def display_sorted_orders(orders):
    print("Sorted Order Records")
    print(f"{'Order ID':<10} {'Client ID':<10} {'Employee ID':<12} {'Description':<20} {'Price':<10}")
    print("-"*10, "-"*10, "-"*12, "-"*20, "-"*10)
    
    for record in orders:
        print(f"{record['orderID']:<10} {record['clientID']:<10} {record['employeeID']:<12} "
              f"{record['description']:<20} {record['price']:<10.2f}")


#---------------------------------------------------------------------------------------

def generate_invoice(orderID):
    print("GENERATE INVOICE")
    print("----------------")

    # Fetch order details
    sqlCommand = "SELECT * FROM orderTable WHERE orderID = ?"
    cursor = fronttoback.cursor()
    cursor.execute(sqlCommand, (orderID,))
    order = cursor.fetchone()

    if not order:
        print("Order not found.")
        return

    # Fetch client details
    clientID = order[1]  # Assuming order[1] is the clientID in the order record
    sqlCommand = "SELECT * FROM clientTable WHERE clientID = ?"
    cursor.execute(sqlCommand, (clientID,))
    client = cursor.fetchone()

    # Fetch employee details
    employeeID = order[2]  # Assuming order[2] is the employeeID in the order record
    sqlCommand = "SELECT * FROM employeeTable WHERE employeeID = ?"
    cursor.execute(sqlCommand, (employeeID,))
    employee = cursor.fetchone()

    # Format the invoice
    invoice = f"""
    FRONTTOBACK DEVELOPMENT - INVOICE
    ======================================
    Invoice Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    
    Order Details:
    --------------
    Order ID       : {order[0]}
    Description    : {order[3]}
    Price          : ${order[4]:.2f}

    Client Details:
    ---------------
    Client ID      : {client[0] if client else 'N/A'}
    Name           : {client[1] if client else 'N/A'}
    Address        : {client[2] if client else 'N/A'}
    Phone          : {client[3] if client else 'N/A'}
    Email          : {client[4] if client else 'N/A'}

    Employee Responsible:
    ---------------------
    Employee ID    : {employee[0] if employee else 'N/A'}
    Name           : {employee[1] if employee else 'N/A'}
    Position       : {employee[2] if employee else 'N/A'}

    ======================================
    Total Amount Due: ${order[4]:.2f}
    Thank you for choosing FrontToBack Development!
    """
    
    # Print the invoice
    print(invoice)

    # Save the invoice to a file
    filename = f"Invoice_{orderID}.txt"
    with open(filename, "w") as file:
        file.write(invoice)
    print(f"Invoice saved as {filename}")

main()