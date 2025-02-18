from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"

# 📌 List of chatbot responses (Arham's replies)
responses = [
    "Hey there! How can I help?",
    "That's interesting! Tell me more.",
    "I'm here to chat with you!",
    "What’s on your mind?",
    "Arham is always here for you!",
    "Keep going! I’m listening.",
    "That sounds great!",
    "Tell me more about it."
]

@app.route("/", methods=["GET", "POST"])
def chat():
    # If the session doesn't have messages, initialize it
    if "messages" not in session:
        session["messages"] = []

    if request.method == "POST":
        user_message = request.form["message"]  # Get user's message
        bot_reply = random.choice(responses)  # Pick a random response

        # Store the messages
        session["messages"].append({"sender": "You", "text": user_message})
        session["messages"].append({"sender": "Arham", "text": bot_reply})

    return render_template("chat.html", messages=session["messages"])

@app.route("/clear")
def clear_chat():
    session.pop("messages", None)  # Clear the chat
    return render_template("chat.html", messages=[])

if __name__ == "__main__":
    app.run(debug=True)
