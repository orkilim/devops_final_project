import random

import requests
import json
def get_money_interval(difficulty):
    url= "https://open.er-api.com/v6/latest/USD"
    t = requests.get(url)
    data = json.loads(t.text)
    USDToILSRate = data["rates"]["ILS"]
    amount = random.randint(1, 100)
    interval = [amount - (5-difficulty),amount + (5-difficulty)]
    return amount,interval

def get_guess_from_user(amount):
    return int(input(f"how much ILS are {amount} USD? > "))

def play(difficulty):
    amount,interval= get_money_interval(difficulty)
    guess = get_guess_from_user(amount)
    if(interval[0]<=guess<=interval[1]):
        print("CORRECT")
        return True
    else:
        print("INCORRECT")
        return False