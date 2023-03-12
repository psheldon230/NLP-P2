from Recipe import RECIPE
from parsedinstruction import parsedInstruction
import substitutions

keywordList = [["ingredient", "ingredients"], ["cooking action", "action", "verb"], ["quantity", "much", "many", "amount"], ["time", "hours", "minutes", "long"], ["cookware", "tool", "kitchenware", "item", "use"]]

unchanged = True
firstTime = True
def process_input():
    pass

def handleQuestion(index, recipe, step):
    if index == 0:
        seen = False
        print("Step " + str(step+ 1) + " ingredient(s): ")
        for ingredient in recipe.parsed_instructions[step].ingredient:
            print(ingredient)
            seen = True
        if not(seen):
            print("This step has no specific ingredients.")
        print("")

    if index == 1:
        saw = False
        print("Step " + str(step+ 1) + " cooking action: ")
        for action in recipe.parsed_instructions[step].cookingAction:
            print(action)
            saw = True
        if not(saw):
            print("This step has no specific cooking action.")
        print("")
    if index == 2:
         print("Step " + str(step+ 1) + " ingredient amounts: ")
         ran = False
         for elem in recipe.parsed_instructions[step].quantity:
             if elem['quantity'] != None and elem['unit'] != None:
                 print(str(elem['quantity']) + " " + str(elem['unit']))
                 ran = True
         if not(ran):
             print("This step has no specific ingredient amount.")
             print("")
            
        
    if index == 3:
         print(recipe.parsed_instructions[step].time)
    if index == 4:
        printed = False
        print("Step " + str(step+ 1) + " tool: ")
        for tool in recipe.parsed_instructions[step].tool:
            printed = True
            print(tool)
        print("")
        if not(printed):
            print("Please reference the tools from the previous step.")
            print("")
def substitute_handler(substitute, recipe):
    subbed = True
    while subbed:  
        if substitute == 1:
            recipe.ingredients_list = substitutions.nonToVeg(recipe)
            print("Subbed to Vegan!")
            subbed = False
        elif substitute == 2:
            substitutions.vegToNon(recipe)
            subbed = False
        elif substitute == 3:
            substitutions.unToHealth(recipe)
            subbed = False
        elif substitute == 4:
            substitutions.healthToUn(recipe)
            subbed = False
        elif substitute == 5:
            substitutions.makeItalian(recipe)
            subbed = False
        elif substitute == 5:
            substitutions.makeMexican(recipe)
            subbed = False
        else:
            subbed = True
            print("Invalid Substitution")
            substitute = get_subst()
    
def get_step():
     looking = True
     while looking:
            try:
                step = int(input("What step would you like to see? Please enter a number: ")) - 1
                looking = False
            except:
                print("Please enter an valid number")
                looking = True
     return step
def get_subst():
     looking = True
     while looking:
            try:
                step = int(input("What substitution would you like to see? Please enter a number: "))
                if step >=7 or step <= 0:
                    print("Please enter a valid substitution!")
                    looking = True
                else:
                    looking = False
            except:
                print("Please enter an valid number")
                looking = True
     return step
def checkStep(recipe, next, curr, back):
        looking = True
        while looking:
            if not(next) and not(back):
                step = get_step()
            elif back:
                step = curr - 1
            else:
                step = curr + 1
            looking = False
            if next or back:
                if step > len(recipe.instructions_list) - 1 or step < 0:
                    if next:

                        print("That was the last step!")
                        step -= 1
                    elif back:
                        print("That was the first step!")
                        step += 1
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
      for  ingredient in recipe.ingredients_list:
            print("")
            print(ingredient)
    
def show_help():
    print("")
    print("---------------------------------------------------------------------")
    print("Welcome to Chefly! I am your virtual recipe assistant to help with all things cooking related.")
    print("")
    print("First, choose a recipe from any well known cooking site online.")
    print("Next, you can choose to examine the whole recipe or go step by step")
    print("")
    print("Whole Recipe:")
    print("You can always ask questions about the whole recipe, such as:\n-show me all ingredients\n-show me all instructions")
    print("")
    print("Step by Step:")
    print("Once you are on a particular step, you can ask things like:\n-what ingredients do I need?\n-how long will that take?\n-what is the cooking action in this step?\n-how much do I need?\n-what tool do I need in this step?\n")
    print("")
    print("General Queries:")
    print("At any time, you can questions like:\n-how do I do that?\n-what can I substitute <ingredient> for\n-how do I cook chicken?\n")
    print("You can also say change recipe at any time, or exit to stop the chat.")
    print("---------------------------------------------------------------------")


    

while True:
    unchanged = True
    if firstTime:
        url = input("Hi I'm Chefly! Enter a Recipe URL to get cooking!" )
        firstTime = False
    else:
        url = input("Please enter another recipe URL: ")
    step = 0
    recipe = RECIPE(url)
    print("Yum! Thats a great choice!")
    print("Let's make " + recipe.scraper.title() + "!")
    print("")
    print("-------------------------------------------------------------------------")
    yorn = input("Would you like to see all ingredients? ")
    if yorn.__contains__("y") or yorn.__contains__("all") or yorn.__contains__("sure"):
        print("Here is what you'll need: ")
        print_ingredients(recipe)
    else:
        print("Okay!")
    print("-------------------------------------------------------------------------")
    start = input("Would you like to see all the instructions? Or go step by step? ")
    if start.__contains__("all"):
        print("")
        print_instructions(recipe)
        print("")
    elif start.__contains__("step"):
        step = checkStep(recipe, False, step, False)
        print("")
        print("Step " + str(step + 1) + ":")
        print(recipe.instructions_list[step])
    print("-------------------------------------------------------------------------")
    substitute = input("Would you like to make a substitution?")
    if substitute.__contains__("y") or substitute.__contains__("sure"):
        print("")
        print("What would you like to substitute? You can choose one of the following: ")
        print("")
        print("[1] Non-Vegan to Vegan, [2] Vegan to Non Vegan, [3] Unhealthy to healthy, [4] Healthy to unhealthy, [5]Make this Italian Style, [6] Make this Mexican Style")
        print("")
        retval = get_subst()
        substitute_handler(retval, recipe)
        print("Here are the new Ingredients you'll need: ")
        substitutions.compare_lists(recipe, recipe.ingredients_list)

    while unchanged:
        print("-------------------------------------------------------------------------")
        question = input("What would you like to know? You can ask things like next step, show all steps, show ingredients for this step, or how much do I need, or how do I do that: ")
        print("")
        if question.__contains__("next step"):
            step = checkStep(recipe, True, step, False)
            print("")
            print("Step " + str(step + 1) + ":")
            print(recipe.instructions_list[step])
        elif question.__contains__("previous") or question.__contains__("back"):
            step = checkStep(recipe, False, step, True)
            print("")
            print("Step " + str(step + 1) + ":")
            print(recipe.instructions_list[step])
        elif question.__contains__("all steps"):
            print_instructions(recipe)
            print("")
            step = 0
        elif question.__contains__("all ingredients"):
            print_ingredients(recipe)
            print("")
            step = 0
        elif question.__contains__("step"):
            step = checkStep(recipe, False, step, False)
            print("")
            print("Step " + str(step + 1) + ":")
            print(recipe.instructions_list[step])
        elif question == "Change Recipe" or question == "change recipe" or question == "Change recipe":
            unchanged = False
        elif question.__contains__("How do I do that") or question.__contains__("how do"):
            string = recipe.instructions_list[step]
            string = string.replace(" ", "+")
            print("I found this on YouTube to answer your question: ")
            print("https://www.youtube.com/results?search_query=how+do+I+" + string)
        elif question.__contains__("How do I") or question.__contains__("how do i") or question.__contains__("how do"):
            question = question.replace(" ", "+")
            print("I found this on YouTube to answer your question: ")
            print("https://www.youtube.com/results?search_query=" + question)
        elif question.__contains__("what is a"):
            question = question.replace(" ", "+")
            print("This might answer your question: ")
            print("https://www.google.com/search?q=" + question)
        elif question.__contains__("what can I substitute"):
             question = question.replace(" ", "+")
             print("This might answer your substitution question: ")
             print("https://www.google.com/search?q=" + question)
        elif question == "exit":
            exit()
        elif question == "help":
            show_help()
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


        



