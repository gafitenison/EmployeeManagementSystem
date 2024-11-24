def generateInvoice(orderID):
    # SQL Command to join tables and get all necessary invoice data
    sqlCommand = """
    SELECT 
        o.orderID, o.orderDate, o.quantity, o.totalPrice,
        c.clientID, c.clientName, c.clientAddress,
        p.productID, p.productName, p.productPrice,
        r.reportID, r.reportSummary
    FROM 
        orderTable o
    JOIN 
        clientTable c ON o.clientID = c.clientID
    JOIN 
        productTable p ON o.productID = p.productID
    JOIN 
        reportTable r ON o.orderID = r.orderID
    WHERE 
        o.orderID = ?;
    """
    
    # Execute query and fetch data
    result = fronttoback.execute(sqlCommand, (orderID,)).fetchone()

    # Check if data is found
    if result:
        orderID, orderDate, quantity, totalPrice, clientID, clientName, clientAddress, productID, productName, productPrice, reportID, reportSummary = result

        # Print the Invoice
        print("\nFRONTTOBACK DEVELOPMENT - INVOICE")
        print("===================================")
        print(f"Invoice for Order ID: {orderID}")
        print(f"Client Name: {clientName}")
        print(f"Client Address: {clientAddress}")
        print(f"Product Name: {productName}")
        print(f"Order Date: {orderDate}")
        print(f"Quantity: {quantity}")
        print(f"Total Price: {totalPrice}")
        print(f"Report Summary: {reportSummary}")
        print("===================================")
    else:
        print(f"No invoice found for Order ID: {orderID}")

# Option to add this into the report or order menu:
def invoiceMenu():
    print("INVOICE MENU")
    print("============")
    print("1 - Generate Invoice by Order ID")
    print("x - Back to Main Menu")
    
    choice = input("\nEnter your choice : ")

    if choice == "1":
        orderID = input("Enter the Order ID: ")
        generateInvoice(orderID)
def mergeSortEmployeeRecords(employeeRecords, sortByField):
    if len(employeeRecords) > 1:
        mid = len(employeeRecords) // 2
        leftHalf = employeeRecords[:mid]
        rightHalf = employeeRecords[mid:]

        # Recursive call on both halves
        mergeSortEmployeeRecords(leftHalf, sortByField)
        mergeSortEmployeeRecords(rightHalf, sortByField)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i][sortByField] < rightHalf[j][sortByField]:
                employeeRecords[k] = leftHalf[i]
                i += 1
            else:
                employeeRecords[k] = rightHalf[j]
                j += 1
            k += 1
newEmployeeRecord = [employeeID, firstName, lastName, dateOfBirth, address, phone, email, position, hireDate, salary, status]
        # Check if any element was left
        while i < len(leftHalf):
            employeeRecords[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            employeeRecords[k] = rightHalf[j]
            j += 1
            k += 1

def binarySearchEmployeeRecords(employeeRecords, searchValue, searchByField):
    low = 0
    high = len(employeeRecords) - 1
   
    while low <= high:
        mid = (low + high) // 2
       
        if employeeRecords[mid][searchByField] == searchValue:
            return mid
        elif employeeRecords[mid][searchByField] < searchValue:
            low = mid + 1
        else:
            high = mid - 1
   
    return -1

def sortAndSearchByField(fieldIndex, fieldName):
    sqlCommand = "SELECT * FROM employeeTable"
    employeeRecords = [record for record in fronttoback.execute(sqlCommand)]
   
    mergeSortEmployeeRecords(employeeRecords, fieldIndex)
   
    print(f"\nSorted Employee Records by {fieldName}:")
    for record in employeeRecords:
        print(record)
   
    searchValue = input(f"\nEnter {fieldName} to search: ")
   
    resultIndex = binarySearchEmployeeRecords(employeeRecords, searchValue, fieldIndex)
   
    if resultIndex != -1:
        print("\nEmployee Found:", employeeRecords[resultIndex])
    else:
        print("\nEmployee not found.")

def employeeSortAndSearchMenu():
    fields = ["employeeID", "firstName", "lastName", "jobTitle", "email"]
   
    while True:
        print("\nSort and Search Employee Records")
        print("1. Sort and Search by employeeID")
        print("2. Sort and Search by firstName")
        print("3. Sort and Search by lastName")
        print("4. Sort and Search by jobTitle")
        print("5. Sort and Search by email")
        print("x. Exit to Employee Menu")
       
        choice = input("Choose a field to sort and search by: ")
       
        if choice == 'x':
            break
        elif choice in ['1', '2', '3', '4', '5']:
            fieldIndex = int(choice) - 1
            chosenField = fields[fieldIndex]
            sortAndSearchByField(fieldIndex, chosenField)
        else:
            print("Invalid choice, please choose again.")

def employeeMenu():
    choice = "0"
   
    while choice != "x":
        print("")
        print("FRONTTOBACK DEVELOPMENT - EMPLOYEE MENU")
        print("--------------------------------------")
        print("1 - Display all Employees.")
        print("2 - Add a new Employee.")
        print("3 - Edit an Employee.")
        print("4 - Delete an Employee.")
        print("5 - Sort and Search Employee Records.")
        print("x - Back to Main Menu.")
       
        choice = input("\nEnter your choice : ")
        print("")
       
        if choice == "1":
            displayAllEmployees()
        elif choice == "2":
            addNewEmployee()
        elif choice == "3":
            editAnEmployee()
        elif choice == "4":
            deleteAnEmployee()
        elif choice == "5":
            sortAndSearchMenu()
