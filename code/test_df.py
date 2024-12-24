import os
import pandas as pd
import sqlite3
from datetime import date

# Create or connect to SQLite database
connection = sqlite3.connect("data/tarot.db")

# Create a cursor object
cursor = connection.cursor()

# Query to list all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all results
tables = cursor.fetchall()
tbl_name = [item[0] for item in tables]

# Write table names to a text file
with open("output/test_dfs.txt", "w") as file:
    file.write("Date: " + str(date.today()) +"\n")
    file.write(f"-------------------------------------------------\n")
    file.write("Tables in the database:\n")
    for table in tables:
        file.write(f"{table[0]}\n")
    file.write(f"-------------------------------------------------\n")

# Close the connection
connection.close()


# Function to get table information and write to the file
def table_info(table_name, db_name="data/tarot.db", output_file="output/test_dfs.txt"):
    # Connect to the database
    connection = sqlite3.connect(db_name)
    
    # Read the table into a DataFrame
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", connection)
    
    # Write table information to the file
    with open(output_file, "a") as file:
        file.write(f"Table: {table_name}\n")
        file.write(f"Number of Observations: {len(df)}\n")
        file.write("Columns:\n")
        file.write(df.dtypes.to_string() + "\n")
        file.write(f"----------------------------------------------------------\n")
    
    # Close the connection
    connection.close()


# Example Usage: Write all table info to the text file
for table in tbl_name:
    table_info(table)

print("Results have been written to 'output/test_dfs.txt'.")
