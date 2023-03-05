import recipe_scrapers
from Recipe import RECIPE
from  parsedinstruction import parsedInstruction

keywordList = [["ingredient", "ingredients"], ["cooking action", "action", "verb"], ["quantity", "much", "many", "amount"], ["time", "hours", "minutes", "long"], ["cookware", "tool", "kitchenware", "item", "use"]]

unchanged = True
firstTime = True
def process_input():
    pass

def handleQuestion(index, recipe, step):
    if index == 0:
        print(recipe.parsed_instructions[step].ingredient)
    if index == 1:
         print(recipe.parsed_instructions[step].cookingAction)
    if index == 2:
         print(recipe.parsed_instructions[step].quantity)
    if index == 3:
         print(recipe.parsed_instructions[step].time)
    if index == 4:
        print(recipe.parsedInstructions[step].tool)

def checkStep(recipe, next, curr):
        looking = True
        while looking:
            if not(next):
                step = int(input("What step would you like to see? Please enter a number ")) - 1
            else:
                step = curr + 1
            looking = False
            if next:
                if step == len(recipe.instructions_list) - 1:
                    print("That was the last step!")
                    step -= 1
                    looking == False

            elif step > len(recipe.instructions_list)-1 or step < 0:
                print("Please choose a valid step!")
                looking = True
        return step

def print_instructions(recipe):
    counter = 1
    for step in recipe.instructions_list:
            print("")
            print("Step " + str(counter) + ":")
            print(step)
            counter += 1
def print_ingredients(recipe):
      for  ingredient in recipe.scraper.ingredients():
            print("")
            print(ingredient)
    



    

while True:
    unchanged = True
    if firstTime:
        url = input("Welcome to our Recipe Chat Bot! Enter a Recipe URL to get cooking!" )
        firstTime = False
    else:
        url = input("Please enter another recipe URL: ")
    step = 0
    recipe = RECIPE(url)
    print("Yum! Thats a great choice!")
    print("Let's make " + recipe.scraper.title() + "!")
    yorn = input("Would you like to see all ingredients? ")
    if yorn.__contains__("y") or yorn.__contains__("all"):
        print("Here is what you'll need: ")
        print_ingredients(recipe)
    else:
        print("Okay!")
    start = input("Would you like to see all the instructions? Or go step by step? ")
    if start.__contains__("all"):
        print_instructions(recipe)
    elif start.__contains__("step"):
        step = checkStep(recipe, False, step)
        print("")
        print("Step " + str(step + 1) + ":")
        print(recipe.instructions_list[step])
    while unchanged:
        print("")
        question = input("What would you like to know? You can ask things like next step, show all steps, show the cooking ingredients, or how much do I need ")
        print("")
        if question.__contains__("next step"):
            step = checkStep(recipe, True, step)
            print("")
            print("Step " + str(step + 1) + ":")
            print(recipe.instructions_list[step])
        elif question.__contains__("all steps"):
            print_instructions(recipe)
            step = 0
        elif question.__contains__("all ingredients"):
            print_ingredients(recipe)
            step = 0
        elif question.__contains__("step"):
            step = checkStep(recipe, False, step)
            print("")
            print("Step " + str(step + 1) + ":")
            print(recipe.instructions_list[step])
        elif question == "Change Recipe" or question == "change recipe" or question == "Change recipe":
            unchanged = False
        elif question == "exit":
            exit()
        else:
            answered = False
            for i in range(len(keywordList)):
                for j in range(len(keywordList[i])):
                    if question.__contains__(keywordList[i][j]):
                        handleQuestion(i, recipe, step)
                        answered = True
                        break
            if not(answered):
                print("Sorry, I am not sure. Please ask another question.")


        



