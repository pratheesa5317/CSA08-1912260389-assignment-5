import sqlite3
import re
from collections import Counter

# Sentiment Analysis

def sentiment(text):

    positive = ["good", "clean", "helpful"]
    negative = ["bad", "dirty", "smoke"]

    score = 0

    for word in text.lower().split():

        if word in positive:
            score += 1

        elif word in negative:
            score -= 1

    return "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"


complaint = "The road is dirty and air is bad"

print("Sentiment:", sentiment(complaint))


# Extractive Summarisation

def summarise(text):

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    frequency = Counter(words)

    ranked = sorted(
        sentences,
        key=lambda s: sum(
            frequency[w] for w in re.findall(r'\b[a-zA-Z]+\b', s.lower())
        ),
        reverse=True
    )

    return " ".join(ranked[:2])


text = "Road is dirty. Air quality is poor. Citizens need clean air."

print("Summary:", summarise(text))


# Database Indexing

con = sqlite3.connect(":memory:")

con.execute("""
CREATE TABLE complaints(
station TEXT,
complaint TEXT
)
""")

con.execute(
    "INSERT INTO complaints VALUES (?,?)",
    ("Adyar", complaint)
)

con.execute("""
CREATE INDEX idx_station
ON complaints(station)
""")

result = con.execute(
    "SELECT * FROM complaints WHERE station=?",
    ("Adyar",)
).fetchall()

print("Database Result:", result)

con.close()
