from bs4 import BeautifulSoup
import requests
from recipe_scrapers import scrape_me
from parsedinstruction import parsedInstruction
import test
import sys

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
        return "9 seconds"
    def cookingAction_Parse(self, string):
         #takes a string as input, parses, and returns a cooking action for the current instruction
         return test.get_verb2(string)
    def quantity_Parse(self, string):
        return "7 pounds"
    def ingredient_Parse(self, string):
        return test.find_ingredients(string)
    def tool_Parse(self, string):
        return test.get_pps(string)
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
    


            

