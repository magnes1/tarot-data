import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("data/tarot.db")
cursor = connection.cursor()

# Name of the table to remove
table_name = "suits"

try:
    # Execute the DROP TABLE statement
    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
    print(f"Table '{table_name}' has been removed successfully.")
except sqlite3.Error as e:
    print(f"Error occurred: {e}")
finally:
    # Close the connection
    connection.close()

# Reconnect to the database
connection = sqlite3.connect("data/tarot.db")
cursor = connection.cursor()

# List all remaining tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Remaining tables in the database:")
for table in tables:
    print(table[0])

connection.close()