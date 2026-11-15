import sqlite3

con = sqlite3.connect(":memory:")

con.execute("""
CREATE TABLE readings(
station TEXT,
pm25 REAL
)
""")

data = [
    ("Adyar", 45),
    ("Guindy", 60),
    ("Velachery", 35)
]

con.executemany(
    "INSERT INTO readings VALUES (?,?)",
    data
)

con.commit()

station = input("Enter Station Name: ")

result = con.execute(
    "SELECT * FROM readings WHERE station=?",
    (station,)
).fetchall()

if result:
    for row in result:
        print(row)
else:
    print("No matching station found")

con.close()
