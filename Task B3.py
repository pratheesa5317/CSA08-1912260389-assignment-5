import sqlite3
import time
import random

data = []

for i in range(1000):
    data.append(("Adyar", random.randint(10, 100)))

# Python Loop

start = time.perf_counter()

total = 0

for station, value in data:
    total += value

print("Loop Average:", total / len(data))

loop_time = time.perf_counter() - start

# SQL

con = sqlite3.connect(":memory:")

con.execute("CREATE TABLE aq(station TEXT, pm25 REAL)")

con.executemany("INSERT INTO aq VALUES (?,?)", data)

start = time.perf_counter()

result = con.execute(
    "SELECT AVG(pm25) FROM aq"
).fetchone()

sql_time = time.perf_counter() - start

print("SQL Average:", result[0])

print("Loop Time:", loop_time)
print("SQL Time:", sql_time)

con.close()
