import os
import pandas as pd
import sqlite3 as sqlite3
# Configure Pandas to display all columns
pd.set_option('display.max_columns', None)

arcana_def = "arcana_def.json"
numbers_def = "numbers_def.json"
images = "tarot_images.json"
suits_def = "suits_def.json"

# Directory containing the JSON files
data_dir = "data/raw_data"

def json_to_sqlite(data_dir, json_file, table_name, db_name = "data/tarot.db"):
    
    """
    Reads a JSON file, converts it to a DataFrame, and imports it into an SQLite3 database.
    
    Parameters:
        json_file (str): Path to the JSON file.
        db_name (str): Name of the SQLite database file (e.g., 'my_database.db').
        table_name (str): Name of the table to create or update in the database.
    
    Returns:
        None
    """
    
    try:
        # Step 1: Read JSON file into a DataFrame
        print(f"Reading JSON file: {json_file}")
        file = os.path.join(data_dir, json_file)
        df = pd.read_json(file)
        
        # Extract the first key dynamically
        name = next(iter(df.keys()))
        # Convert the JSON content into a DataFrame
        df = pd.DataFrame(df[name].tolist())
        
        # Identify columns with lists and convert to strings
        for column in df.columns:
            if df[column].apply(lambda x: isinstance(x, list)).any():
                df[column] = df[column].apply(lambda x: ','.join(x) if isinstance(x, list) else x)
        print("JSON file successfully loaded into DataFrame.")

        # Step 2: Connect to SQLite database (creates if it doesn't exist)
        connection = sqlite3.connect(db_name)
        print(f"Connected to SQLite database: {db_name}")

        # Step 3: Write DataFrame to SQLite table
        df.to_sql(table_name, connection, if_exists='replace', index=False)
        print(f"DataFrame successfully imported into table '{table_name}'.")
        
       

        # Step 4: Close the connection
        connection.close()
        print("SQLite connection closed.")
        print(f"--------------------------------")
    except Exception as e:
        print(f"An error occurred: {e}")

arcana_def = "arcana_def.json"
numbers_def = "numbers_def.json"
images = "tarot_images.json"

# Directory containing the JSON files
data_dir = "data/raw_data"

# Example Usage
if __name__ == "__main__":
    json_to_sqlite(data_dir, arcana_def, table_name = "arcana_def")
    json_to_sqlite(data_dir, suits_def, table_name = "suits_def")
    json_to_sqlite(data_dir, numbers_def, table_name = "numbers_def")
    json_to_sqlite(data_dir, images, table_name = "images")