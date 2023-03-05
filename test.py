from bs4 import BeautifulSoup
import requests
from recipe_scrapers import scrape_me
import spacy
nlp = spacy.load("en_core_web_sm")

scraper =scrape_me(("https://www.allrecipes.com/recipe/223382/chicken-stir-fry/"))
instructions = scraper.instructions()
ingredients = scraper.ingredients()
#print(ingredients)
instructions = instructions.split(".")
for i in range(len(instructions)):
    instructions[i] = instructions[i].replace('\n',"")
text = instructions[7]
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
    return step_breakdown["ingredients"]


def get_pps(instruction):
    "Function to get PPs from a parsed document."
    doc =  nlp(instruction)
    pps = []
    for token in doc:
        # Try this with other parts of speech for different subtrees.
        if token.pos_ == 'ADP':
            pp = ' '.join([tok.orth_ for tok in token.subtree])
            pps.append(pp)
    return pps

#print(get_pps(doc))


def get_verb(instruction):
    "Function to get PPs from a parsed document."
    doc =  nlp(instruction)
    pps = []
    for token in doc:
        # Try this with other parts of speech for different subtrees.
        if token.pos_ == 'VERB':
            pp = ' '.join([tok.orth_ for tok in token.subtree])
            pps.append(pp)
    return pps

#print(get_verb(doc))
# step = 1 //keep this, I commented it for now but it does a good job at taking out cooking actions
# print(instructions)
# for cooking_action in instructions:
#     for verb in cooking_verbs:
#         if verb in cooking_action.lower():
#             print(str(step) + ": " + verb)
#     step = step + 1

#need to get phrases for what you cook with i.e. "in a saucepan", could do this with chunking, 
#but it should have an output that is easy to print (aka readable to the user)