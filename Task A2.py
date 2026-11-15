data = [
    ["Adyar", 45],
    ["Guindy", 60],
    ["Velachery", -5],
    ["Adyar", None],
    ["Guindy", 80]
]

cleaned = []

for row in data:
    if row[1] is not None and row[1] >= 0:
        cleaned.append(row)

values = [r[1] for r in cleaned]

minimum = min(values)
maximum = max(values)

print("Cleaned Data:")

for row in cleaned:
    normal = (row[1] - minimum) / (maximum - minimum)
    print(row, "Normalized:", round(normal, 2))

fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5 / 9

print("Celsius:", round(celsius, 2))
