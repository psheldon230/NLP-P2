from bs4 import BeautifulSoup
import requests
from recipe_scrapers import scrape_me
import nltk
from nltk.tree import Tree, TreePrettyPrinter
from nltk.tokenize import word_tokenize
import spacy
nlp = spacy.load("en_core_web_sm")

scraper =scrape_me(("https://www.allrecipes.com/recipe/223382/chicken-stir-fry/"))
instructions = scraper.instructions()
ingredients = scraper.ingredients()
#print(ingredients)
instructions = instructions.split(".")
for i in range(len(instructions)):
    instructions[i] = instructions[i].replace('\n',"")
test = nltk.pos_tag(word_tokenize(instructions[1]))
text = instructions[2]
doc =  nlp(text)
#print(doc.ents)
#print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])

#print(test)
cooking_verbs = ["add","break","boil","blend","bake","barbecue","cut","cover","crush","cool",
                 "chop","dip","dice","decorate","drain","fry","flip","grind","grate","grill",
                 "heat","knead","layer","light","measure","mix","microwave","mash","melt","mince"
                 "marinate","peel","pour","put",'remove',"roast","refridgerate","roll","rinse","stir",
                 "scramble","sprinkle","squeeze","spread","steam","simmer","slice","saute","sip","sharpen",
                 "sift","toss","turn off","tenderize","taste","toast","weigh","whisk","wash","combine","separate",
                 "cook","serve","transfer","move"]


#for step_breakdown the key will be a step id (# in array) and hold each steps important info:
                        #cooking action = a list that will hold all the cooking actions in that step
                        #ingredients = a list of all ingredients in that step
                        #tools = tools necessary in that step
#ideally the cooking action would include the specific preparation i.e "till browned", "finely chopped", etc.

step_breakdown = {'cooking action': [], 'ingredients': [], 'tools': []} 


#if empty its previous ingreidents
def find_ingredients(instruction):
    doc =  nlp(instruction)
    for chunk in doc.noun_chunks:
        for ingredient in ingredients:
            if chunk.root.text.lower() in ingredient and chunk.text not in step_breakdown["ingredients"]:
                step_breakdown["ingredients"].append(chunk.text)
    print(step_breakdown["ingredients"])

find_ingredients(text)

def find_tools(instruction):
    doc =  nlp(instruction)
    for chunk in doc.noun_chunks:
            if chunk.text.lower().find("a ") != -1 and chunk.root.text not in cooking_verbs:
                step_breakdown["tools"].append(chunk.text)
    print(step_breakdown["tools"])

find_tools(text)
# step = 1 //keep this, I commented it for now but it does a good job at taking out cooking actions
# print(instructions)
# for cooking_action in instructions:
#     for verb in cooking_verbs:
#         if verb in cooking_action.lower():
#             print(str(step) + ": " + verb)
#     step = step + 1

#need to get phrases for what you cook with i.e. "in a saucepan", could do this with chunking, 
#but it should have an output that is easy to print (aka readable to the user)



