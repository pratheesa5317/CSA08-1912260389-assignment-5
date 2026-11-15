data = {
    "Adyar": [45, 50, 55, 60],
    "Guindy": [65, 70, 75, 80],
    "Velachery": [30, 35, 40, 45]
}

print("Station Analysis")

for station, values in data.items():
    print("Station:", station)
    print("Minimum:", min(values))
    print("Maximum:", max(values))
    print("Average:", sum(values) / len(values))

print("\nHighest Pollution Station:")

highest = max(data, key=lambda x: sum(data[x]) / len(data[x]))

print(highest)
