import pandas as pd
import sqlite3

csv_file = r"C:\Users\Ketan\village_data.csv"

# ✅ simple rakho
db_file = "village.db"

df = pd.read_csv(csv_file)
df.columns = df.columns.str.strip()

conn = sqlite3.connect(db_file)

df.to_sql("villages", conn, if_exists="replace", index=False)

print("✅ Data inserted into DB successfully")

conn.close()