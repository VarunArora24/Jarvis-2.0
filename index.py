from flask import Flask, render_template, request, jsonify
import datetime
from jarvis_logic import get_response

app = Flask(__name__)

@app.route("/")
def home():
    name = "Varun"
    now = datetime.datetime.now()
    day_name = now.strftime("%A")
    date_str = now.strftime("%B %d, %Y")

    hour = now.hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    greet_message = f"{greeting}, {name}"
    today_message = f"Today is {day_name}, {date_str}"

    return render_template(
        "index.html",
        greet_message=greet_message,
        today_message=today_message,
        name=name
    )

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = get_response(user_message)  # <- use get_response here
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
