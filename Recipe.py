from recipe_scrapers import scrape_me
from parsedinstruction import parsedInstruction
import instructionInfo

class RECIPE:

    def __init__(self, url):
        self
        looking = True
        while looking:
            try:
                scrape_me(url)
                looking = False
            except:
                url = input('Please try another recipe: ')
                looking = True
        self.scraper = scrape_me(url)
        self.ingredients_list = self.scraper.ingredients()
        self.old_ingredients = self.scraper.ingredients()
        self.parsed_instructions = []
        self.instructions_list = self.seperate_instruction(self.scraper.instructions_list())
        self.populate()
    
    def populate(self):
        #This will populate parsed_instructions list with necessary fields
        for instruction in self.instructions_list:
            parsedIndex = parsedInstruction(0, 0, 0, 0, 0)
            parsedIndex.time = self.time_Parse(instruction)
            parsedIndex.cookingAction = self.cookingAction_Parse(instruction)
            parsedIndex.quantity = self.quantity_Parse(instruction)
            parsedIndex.ingredient = self.ingredient_Parse(instruction)
            parsedIndex.tool = self.tool_Parse(instruction)
            self.parsed_instructions.append(parsedIndex)
    def time_Parse(self, string):
        #takes a string as input, parses, and returns a time value for the current instruction
        time = instructionInfo.get_time(string)
        if time == []:
            return "There is no specific time limit, but there might be extra notable signs to tell you when to stop. Ask for extra information to see."
        else:
            return ("You should do this for about: " + time[0])

    def cookingAction_Parse(self, string):
         #takes a string as input, parses, and returns a cooking action for the current instruction
         return instructionInfo.get_verb2(string)
    def quantity_Parse(self, string):
        return instructionInfo.get_quantity(string, self.scraper.ingredients())
    def ingredient_Parse(self, string):
        return instructionInfo.find_ingredients(string,self.scraper.ingredients())
    def tool_Parse(self, string):
        return instructionInfo.get_tools(string)
    def seperate_instruction(self, instructions):
        oldList = instructions
        seperatedList = []
        for step in oldList:
             step = step.split(".")
             for i in step:
                 seperatedList.append(i)

                 
            #instructions[i] = instructions[i].replace('\n',"")
        ret_list = [x for x in seperatedList if x != ""]
        formated = [x[1:] if x.startswith(" ") else x for x in ret_list]
        return formated
    


            

