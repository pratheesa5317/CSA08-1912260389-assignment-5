import csv
import sqlite3
from io import StringIO

data = """station,date,hour,pm25,pm10,no2,temp
Adyar,2026-10-01,10,45,80,20,32
Guindy,2026-10-01,11,60,90,25,34
Velachery,2026-10-01,12,35,70,18,30
"""

con = sqlite3.connect("air_quality.db")

con.execute("""
CREATE TABLE IF NOT EXISTS readings(
station TEXT,
date TEXT,
hour INTEGER,
pm25 REAL,
pm10 REAL,
no2 REAL,
temp REAL
)
""")

reader = csv.DictReader(StringIO(data))

for row in reader:
    con.execute(
        "INSERT INTO readings VALUES(?,?,?,?,?,?,?)",
        (row["station"], row["date"], int(row["hour"]),
         float(row["pm25"]), float(row["pm10"]),
         float(row["no2"]), float(row["temp"]))
    )

con.commit()

print("Data stored successfully")

result = con.execute("SELECT * FROM readings").fetchall()

for r in result:
    print(r)

con.close()
