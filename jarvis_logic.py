import random
import os
from datetime import datetime, timedelta
import requests

name = "Varun"

# Greeting logic
from datetime import datetime, timedelta

def get_greeting():
    # Convert UTC to IST (UTC+5:30)
    now_utc = datetime.utcnow()
    now_ist = now_utc + timedelta(hours=5, minutes=30)
    current_hour = now_ist.hour

    if 0 <= current_hour < 12:
        time_of_day = "morning"
    elif 12 <= current_hour < 16:
        time_of_day = "afternoon"
    elif 16 <= current_hour < 19:
        time_of_day = "evening"
    else:
        time_of_day = "night"

    return f"Good {time_of_day}, {name}!"


# Greeting responses
list_greet = [
    "Hi there! How can I assist you today?",
    "Hello! What can I do for you?",
    "Greetings! Ready when you are.",
    "Hey! How may I help you right now?",
    "Hello, Varun. Your digital assistant is online.",
    "Hi! Need help with something?",
    "At your service! Just tell me what you need.",
    "Hey there! What task should I tackle?",
    "Good to see you! What can I do for you today?",
    "Welcome back! How can I make your day easier?"
]

# Weather function
def get_weather(city):
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        return "API key not set. Please add OPENWEATHER_API_KEY as an environment variable."
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if data.get("cod") != 200:
            return "City not found. Please try again."
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        return f"The weather in {city} is {weather} with {temp}°C and {humidity}% humidity."
    except requests.RequestException:
        return "Error fetching weather."

# Rock-paper-scissor game
def play_rps(user_choices, total_times):
    list_rock_game = ["rock", "paper", "scissor"]
    user_score = 0
    comp_score = 0
    responses = []

    for your_input in user_choices:
        computer_input = random.choice(list_rock_game)
        if your_input == computer_input:
            responses.append(f"Both selected {your_input}, draw!")
        elif (your_input == "scissor" and computer_input == "paper") or \
             (your_input == "rock" and computer_input == "scissor") or \
             (your_input == "paper" and computer_input == "rock"):
            responses.append(f"You chose {your_input}, I chose {computer_input}. You win this round!")
            user_score += 1
        else:
            responses.append(f"You chose {your_input}, I chose {computer_input}. I win this round!")
            comp_score += 1

    responses.append(f"Final Score - You: {user_score}, Jarvis: {comp_score}")
    if user_score > comp_score:
        responses.append("You have won! Congrats 🎉")
    elif user_score < comp_score:
        responses.append("I have won! Yay 😎")
    else:
        responses.append("It's a draw!")

    return responses

# Main response router
def get_response(user_input):
    user_input = user_input.lower()
    if user_input in ["hello", "hi", "hey", "hii"]:
        return random.choice(list_greet)
    elif "time" in user_input:
        now_utc = datetime.utcnow()
        now_ist = now_utc + timedelta(hours=5, minutes=30)
        return f"The time now is {now_ist.strftime('%H:%M:%S')}"
    elif "weather" in user_input:
        return "Please provide the city name using: weather:<city>"
    elif user_input.startswith("weather:"):
        city = user_input.split("weather:")[1].strip()
        return get_weather(city)
    elif "rock paper scissor" in user_input:
        return "Send a list of your moves and number of rounds to play the game."
    elif user_input == "exit":
        return "Goodbye!"
    else:
        return "I don't understand that yet. Try something else."
