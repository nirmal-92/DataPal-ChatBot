from flask import Flask, request, jsonify
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

app = Flask(__name__)

# Example training data (user queries and their intents)
training_data = [
    ("Who won the last match?", "match_score"),
    ("Tell me about Messi", "player_info"),
    ("When is the next Arsenal game?", "upcoming_match"),
    ("Who is the top scorer?", "player_info"),
    ("What is the score of the last match?", "match_score")
]

# Separate the queries and labels
queries = [item[0] for item in training_data]
labels = [item[1] for item in training_data]

# Initialize Tfidf Vectorizer and Logistic Regression model
vectorizer = TfidfVectorizer()
model = LogisticRegression()

# Function to train the model
def train_model():
    X = vectorizer.fit_transform(queries)
    y = np.array(labels)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model.fit(X_train, y_train)
    
    # Evaluate accuracy
    accuracy = model.score(X_test, y_test)
    return accuracy

# Function to classify intent of a message
def get_intent(message):
    message_vec = vectorizer.transform([message])
    intent = model.predict(message_vec)
    return intent[0]

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form.get('message')
    
    if user_message.lower() == "train yourself":
        # Train the model and get the accuracy
        accuracy = train_model()
        return f"Training complete! Model accuracy: {accuracy * 100:.2f}%"
    
    # Get the intent for the user's message
    intent = get_intent(user_message)
    
    # Respond based on intent
    if intent == "match_score":
        return "The latest match was won by Team A!"
    elif intent == "player_info":
        return "Lionel Messi is a famous footballer from Argentina."
    elif intent == "upcoming_match":
        return "The next match is on Sunday."
    else:
        return "I'm not sure about that. Please try again."

if __name__ == "__main__":
    app.run(debug=True)
