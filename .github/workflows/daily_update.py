import requests
import datetime

FACTS_FILE = "facts.txt"

def get_daily_fact():
    today = datetime.datetime.now().strftime("%m/%d")
    response = requests.get(f"http://numbersapi.com/{today}/date")
    return response.text if response.status_code == 200 else "No fact available."

def save_fact(fact):
    with open(FACTS_FILE, "a") as file:
        file.write(f"{datetime.datetime.now().date()}: {fact}\n")

if __name__ == "__main__":
    fact = get_daily_fact()
    save_fact(fact)
    print("Daily fact added!")
