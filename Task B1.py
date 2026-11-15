import csv
from io import StringIO

data = """station,pm25
Adyar,45
Guindy,NA
Velachery,-5
Adyar,60
Guindy,120
"""

reader = csv.DictReader(StringIO(data))

cleaned = []

for row in reader:

    try:
        value = float(row["pm25"])

        if 0 <= value <= 99:
            cleaned.append((row["station"], value))

    except ValueError:
        continue

print("Cleaned Data:")

for row in cleaned:
    print(row)

print("Total Valid Records:", len(cleaned))
