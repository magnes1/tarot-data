import os
import pandas as pd
import sqlite3 as sqlite3

connection = sqlite3.connect("data/tarot.db")

img = pd.read_sql_query(f"SELECT * FROM images", connection)
del img["suit"]
print(img)
print("----------------------------------------------------------------")

tarot = pd.read_sql_query(f"SELECT * FROM tarot_cards", connection)
print(tarot)
print("----------------------------------------------------------------")

# Merge DataFrames on the "ID" column
master = pd.merge(tarot, img, on=["name", "arcana"], how="outer")

print(master)
print("----------------------------------------------------------------")
print("master dataframe")
print(f"Number of observations: {master.shape[0]}")

print("Columns:")
for col in master.columns: print(col)

master.to_sql("master", connection, if_exists='replace', index=False)
print(f"DataFrame successfully imported into table 'master'.")

# Save to a JSON file
sample_data = master[0:10]
sample_data.to_json("data/sample_data.json", orient="records", indent=4)
print("DataFrame saved to 'sample_data.json'.")

connection.close()