import os
import pandas as pd
import sqlite3 as sqlite3

# Configure Pandas to display all columns
pd.set_option('display.max_columns', None)

# List of JSON files to process
suits = ["pentacles.json", 
         "swords.json", 
         "wands.json", 
         "cups.json", 
         "major_arcana.json"]

# Directory containing the JSON files
data_dir = "data/raw_data"

# List to store DataFrames
suit_df_list = []

# Process each JSON file
for suit in suits:
    try:
        # Construct the full file path
        file = os.path.join(data_dir, suit)
        print(f"Processing file: {file}")
        
        # Read the JSON data into a dictionary
        data = pd.read_json(file)
        
        # Extract the first key dynamically
        name = next(iter(data.keys()))
        
        # Convert the JSON content into a DataFrame
        df = pd.DataFrame(data[name].tolist())
        
        # Add a column for the suit name
        df['suit'] = suit.split('.')[0]  # Extract suit name from the filename
        
        # Append the DataFrame to the list
        suit_df_list.append(df)
    except Exception as e:
        print(f"Error processing {suit}: {e}")

# Concatenate all DataFrames into one
combined_df = pd.concat(suit_df_list, ignore_index=True)

# Display the combined DataFrame
print("\nCombined DataFrame:")
print(combined_df.head())  # Display the first few rows

# Create or connect to SQLite database
connection = sqlite3.connect("data/tarot.db")

# Write Suits DataFrame to SQLite database
combined_df.to_sql('suits', connection, if_exists='replace', index=False)

print("Suits DataFrame written to SQLite database successfully.")

# Verify the data
result = pd.read_sql("SELECT * FROM suits", connection)
print(result)

# Close the connection
connection.close()


