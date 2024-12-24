import os
import pandas as pd
import sqlite3 as sqlite3

# Create or connect to SQLite database
connection = sqlite3.connect("data/tarot.db")

# Create a cursor object
cursor = connection.cursor()

# Query to list all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all results
tables = cursor.fetchall()
tbl_name= [item[0] for item in tables]

# Print table names
print("Tables in the database:")
for table in tables:
    print(table[0])

print(f"-------------------------------------------------")
# Close the connection
connection.close()


# # Verify the data
# result = pd.read_sql("SELECT * FROM numbers", connection)
# print(result)

def table_info(table_name, db_name = "data/tarot.db"):
    # Connect to the database
    connection = sqlite3.connect(db_name)
    
    # Read the table into a DataFrame
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", connection)
    
    # Print column types and row count
    print(f"Table: {table_name}")
    print(f"Number of Observations: {len(df)}")
    print("Columns:")
    print(df.dtypes)
    print(f"----------------------------------------------------------")
    
    # Close the connection
    connection.close()

# Example Usage
for table in tbl_name:
    table_info(table)



