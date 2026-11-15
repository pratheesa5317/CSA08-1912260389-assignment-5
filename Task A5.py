positive = ["good", "clean", "helpful", "fast", "improved"]
negative = ["bad", "dirty", "slow", "smoke", "broken"]

def sentiment(text):

    words = text.lower().split()

    score = 0

    for word in words:
        if word in positive:
            score += 1
        elif word in negative:
            score -= 1

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

complaint = input("Enter Complaint: ")

print("Sentiment:", sentiment(complaint))


def chatbot(question):

    question = question.lower()

    if "pm2.5" in question:
        return "PM2.5 reading is 45"

    elif "station" in question:
        return "Available stations: Adyar, Guindy, Velachery"

    elif "pollution" in question:
        return "Air pollution is monitored daily"

    else:
        return "Sorry, I cannot understand"


q = input("Ask a question: ")

print("Chatbot:", chatbot(q))
