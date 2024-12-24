import os
import pandas as pd
import sqlite3 as sqlite3

connection = sqlite3.connect("data/tarot.db")

## arcana_def
df = pd.read_sql_query(f"SELECT * FROM arcana_def", connection)
print(df)
df = df.rename(columns={"name": "arcana"})    
print(df)

df.to_sql("arcana_def", connection, if_exists='replace', index=False)
print(f"DataFrame successfully imported into table 'arcana_def'.")
        
## suits_def
df = pd.read_sql_query(f"SELECT * FROM suits_def", connection)
print(df)
df = df.rename(columns={"name": "suit"})    
print(df)

df.to_sql("suits_def", connection, if_exists='replace', index=False)
print(f"DataFrame successfully imported into table 'suits_def'.")

## cards
df = pd.read_sql_query(f"SELECT * FROM tarot_cards", connection)
print(df)

df["arcana"] = df["suit"].apply(
    lambda x: "major arcana" if "major arcana" in x else "minor arcana"
)
  
print(df)
df.to_sql("tarot_cards", connection, if_exists='replace', index=False)
print(df)
print(f"DataFrame successfully imported into table 'tarot_cards'.")

connection.close()