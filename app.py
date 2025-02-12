from flask import Flask, jsonify, render_template
import requests
import datetime
import os

app = Flask(__name__)
FACTS_FILE = "facts.txt"

# Function to fetch a fact from NumbersAPI
def get_daily_fact():
    today = datetime.datetime.now().strftime("%m/%d")
    response = requests.get(f"http://numbersapi.com/{today}/date")
    return response.text if response.status_code == 200 else "No fact available."

# Function to save the fact to a file
def save_fact(fact):
    with open(FACTS_FILE, "a") as file:
        file.write(f"{datetime.datetime.now().date()}: {fact}\n")

# Function to read the latest fact
def get_latest_fact():
    try:
        with open(FACTS_FILE, "r") as file:
            lines = file.readlines()
            return lines[-1] if lines else "No facts recorded yet."
    except FileNotFoundError:
        return "No facts recorded yet."

@app.route("/")
def home():
    latest_fact = get_latest_fact()
    return render_template("index.html", fact=latest_fact)

@app.route("/fetch-fact")
def fetch_fact():
    fact = get_daily_fact()
    save_fact(fact)
    return jsonify({"fact": fact})

if __name__ == "__main__":
    app.run(debug=True)
