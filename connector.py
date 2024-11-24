import sqlite3

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
