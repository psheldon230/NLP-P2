import recipe_scrapers
from input import RECIPE

url = input("Welcome to our Recipe Chat Bot! Please enter a recipe URL:" )
recipe = RECIPE(url)
responses = []

def process_input():
    pass

while True:
    input = input()
    response = process_input(input)
    if response in responses:
        print(response)
    elif response == "Exit":
        exit()
    else:
        print("Sorry, I'm not sure, please ask again")

    





