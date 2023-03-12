from Recipe import RECIPE
from parsedinstruction import parsedInstruction
import substitutions
#Keyword list to identify questions about a specific recipe's step
keywordList = [["ingredient", "ingredients"], ["cooking action", "action", "verb"], ["quantity", "much", "many", "amount"], ["time", "hours", "minutes", "long"], ["cookware", "tool", "kitchenware", "item", "use"]]

unchanged = True
firstTime = True
#Function to return an answer to questions about a specific recipe step, ie: what is the cooking action in this step?
#or questions like: what are the ingredients in this step?
def handleQuestion(index, recipe, step, subd):
    #For questions about a step's ingredients
    if index == 0:
        seen = False
        print("Step " + str(step+ 1) + " ingredient(s): ")
        for ingredient in recipe.parsed_instructions[step].ingredient:
            print(ingredient)
            seen = True
        if not(seen):
            print("This step has no specific ingredients.")
        elif subd:
            print("")
            print("*Remember to replace substituted ingredients for each step when necessary*")
        print("")
    #For questions about a step's cooking actions
    if index == 1:
        saw = False
        print("Step " + str(step+ 1) + " cooking action: ")
        for action in recipe.parsed_instructions[step].cookingAction:
            print(action)
            saw = True
        if not(saw):
            print("This step has no specific cooking action.")
        print("")
    #For questions about a step's quantity of ingredients
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
         elif subd:
            print("")
            print("*Remember to replace substituted ingredients for each step when necessary*")
            
    #For handling questions about a particular step's time    
    if index == 3:
         print(recipe.parsed_instructions[step].time)
    #For handling questions about a particular step's cookware
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
#Handles the user's request to substitute recipe, and calls the relevant method's in the
#substitutions.py file to return a correct output
def substitute_handler(substitute, recipe):
    subbed = True
    while subbed:  
        #Handles Non-vegan to Vegan
        if substitute == 1:
            recipe.ingredients_list = substitutions.nonToVeg(recipe)
            print("Subbed to Vegan!")
            subbed = False
        #Handles Vegan to Non-vegan
        elif substitute == 2:
            substitutions.vegToNon(recipe)
            subbed = False
        #Handles Unhealthy to Healthy
        elif substitute == 3:
            recipe.ingredients_list = substitutions.unToHealth(recipe)
            print("Subbed to Healthy!")
            subbed = False
        #Handles Healthy to Unhealthy
        elif substitute == 4:
            recipe.ingredients_list = substitutions.healthToUn(recipe)
            print("Subbed to Unhealthy!")
            subbed = False
        #Handles Make Italian
        elif substitute == 5:
            recipe.ingredients_list = substitutions.makeItalian(recipe)
            print("Subbed to Italian!")
            subbed = False
        #Handles Make Mexican
        elif substitute == 6:
            recipe.ingredients_list = substitutions.makeMexican(recipe)
            print("Subbed to Mexican!")
            subbed = False
        #If User chooses an invalid number, lets them rechoose, and the loop continues to handle
        #their request!
        else:
            subbed = True
            print("Invalid Substitution")
            substitute = get_subst()
#Function to gather step number input from user, if input is invalid number, lets user rechoose    
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
#Lets user pick a number corresponding to substitution preference
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
#Checks user's desired step to examine to see if it is valid, if not, lets user repick number
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
#prints and formats all instructions in recipe classes's instructions_list
def print_instructions(recipe):
    counter = 1
    for step in recipe.instructions_list:
            print("")
            print("Step " + str(counter) + ":")
            print(step)
            counter += 1
#Just like print_instructions() but for ingredients
def print_ingredients(recipe):
      for  ingredient in recipe.ingredients_list:
            print("")
            print(ingredient)
#Formats and prints the help section when called    
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


    
#Outer loop in User Interface
#Here, users can do things like enter a URL, make a substitution, see all ingredients, or see all steps
while True:
    subd = False
    unchanged = True
    if firstTime:
        url = input("Hi I'm Chefly! Enter a Recipe URL to get cooking! " )
        firstTime = False
    else:
        url = input("Please enter another recipe URL: ")
    step = 0
    #Creates Recipe class object
    recipe = RECIPE(url)
    print("Yum! Thats a great choice!")
    print("Let's make " + recipe.scraper.title() + "!")
    print("")
    print("-------------------------------------------------------------------------")
    #Asks user if they want to see all ingredients, calls print_ingredients() if they do
    yorn = input("Would you like to see all ingredients? ")
    if yorn.__contains__("y") or yorn.__contains__("all") or yorn.__contains__("sure"):
        print("Here is what you'll need: ")
        print_ingredients(recipe)
    else:
        print("Okay!")
    print("-------------------------------------------------------------------------")
    #Asks user if they would like to substitute, calls get_subst() to store input, and substitute_handler()
    #if they do
    substitute = input("Would you like to make a substitution?" )
    if substitute.__contains__("y") or substitute.__contains__("sure"):
        print("")
        print("What would you like to substitute? You can choose one of the following: ")
        print("")
        print("[1] Non-Vegan to Vegan, [2] Vegan to Non Vegan, [3] Unhealthy to healthy, [4] Healthy to unhealthy, [5]Make this Italian Style, [6] Make this Mexican Style")
        print("")
        retval = get_subst()
        substitute_handler(retval, recipe)
        print("")
        print("Here are the new Ingredients you'll need: ")
        print("")
        substitutions.compare_lists(recipe, recipe.ingredients_list)
        subd = True
    print("-------------------------------------------------------------------------")
    #Asks user if they want to see a list of all instructions, or examine one individually
    start = input("Would you like to see all the instructions? Or go step by step? ")
    if start.__contains__("all"):
        print("")
        print_instructions(recipe)
        print("")
        if subd:
            print("*Remember to replace substituted ingredients for each step when necessary*")
            print("")
    elif start.__contains__("step"):
        step = checkStep(recipe, False, step, False)
        print("")
        print("Step " + str(step + 1) + ":")
        print(recipe.instructions_list[step])
        if subd:
            print("*Remember to replace substituted ingredients for each step when necessary*")
            print("")
  #Inner loop of Chefly, where users can see all steps, all ingredients, or navigate specific steps
  # and see information about each specific one 
    while unchanged:
        print("-------------------------------------------------------------------------")
        question = input("What would you like to know? You can ask things like next step, show all steps, show ingredients for this step, or how much do I need, or how do I do that: ")
        print("")
        #Handles user's response for the inner loop

        #If user says next step, program calls check_step() and proceeds to next
        if question.__contains__("next step"):
            step = checkStep(recipe, True, step, False)
            print("")
            print("Step " + str(step + 1) + ":")
            print(recipe.instructions_list[step])
            if subd:
                print("*Remember to replace substituted ingredients for each step when necessary*")
                print("")
        #If user says previous step, or back step, changes step count to - 1
        elif question.__contains__("previous") or question.__contains__("back"):
            step = checkStep(recipe, False, step, True)
            print("")
            print("Step " + str(step + 1) + ":")
            print(recipe.instructions_list[step])
            if subd:
                print("*Remember to replace substituted ingredients for each step when necessary*")
                print("")
        #Prints all steps
        elif question.__contains__("all steps"):
            print_instructions(recipe)
            print("")
            step = 0
            if subd:
                print("*Remember to replace substituted ingredients for each step when necessary*")
                print("")
        #Prints all ingredients
        elif question.__contains__("all ingredients"):
            print_ingredients(recipe)
            print("")
            step = 0
        #If user wants to see a specific step, prints that step
        elif question.__contains__("step"):
            step = checkStep(recipe, False, step, False)
            print("")
            print("Step " + str(step + 1) + ":")
            print(recipe.instructions_list[step])
            if subd:
                print("*Remember to replace substituted ingredients for each step when necessary*")
                print("")
        #If user wants to change recipe, sets inner loop variable to false to re start the outer loop
        elif question == "Change Recipe" or question == "change recipe" or question == "Change recipe":
            unchanged = False
        #If user asks How do I do that, queries YouTube for their specific question
        elif question.__contains__("How do I do that") or question.__contains__("how do"):
            string = recipe.instructions_list[step]
            string = string.replace(" ", "+")
            print("I found this on YouTube to answer your question: ")
            print("https://www.youtube.com/results?search_query=how+do+I+" + string)
        #If user asks how do I do that for more general questions, queries YouTube
        elif question.__contains__("How do I") or question.__contains__("how do i") or question.__contains__("how do"):
            question = question.replace(" ", "+")
            print("I found this on YouTube to answer your question: ")
            print("https://www.youtube.com/results?search_query=" + question)
        #If user asks a question in format 'what is a', queries google and returns a link with results
        elif question.__contains__("what is a"):
            question = question.replace(" ", "+")
            print("This might answer your question: ")
            print("https://www.google.com/search?q=" + question)
        #If user asks substitution questions, queries google for the result
        elif question.__contains__("what can I substitute"):
             question = question.replace(" ", "+")
             print("This might answer your substitution question: ")
             print("https://www.google.com/search?q=" + question)
        #If user types 'exit', terminates program
        elif question == "exit":
            exit()
        #If user types 'help' calls show_help() method
        elif question == "help":
            show_help()
        else:
            #For specific questions about a recipe's step
            #Checks to see which keyword matches the users question, to appropriately call handle_question()
            answered = False
            for i in range(len(keywordList)):
                for j in range(len(keywordList[i])):
                    if question.__contains__(keywordList[i][j]):
                        handleQuestion(i, recipe, step, subd)
                        answered = True
                        break
            #If handle_question() has not been called, and for all other questions that haven't been handled,
            #print this result
            if not(answered):
                print("Sorry, I am not sure. Please ask another question.")


        



