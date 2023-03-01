from bs4 import BeautifulSoup
import requests
from recipe_scrapers import scrape_me
import nltk
from nltk.tree import Tree, TreePrettyPrinter
from nltk.tokenize import word_tokenize

scraper =scrape_me(("https://www.allrecipes.com/recipe/223382/chicken-stir-fry/"))
instructions = scraper.instructions()
instructions = instructions.split(".")
test = nltk.pos_tag(word_tokenize(instructions[1]))
print(test)
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

step_breakdown = {} 


# step = 1 //keep this, I commented it for now but it does a good job at taking out cooking actions
# print(instructions)
# for cooking_action in instructions:
#     for verb in cooking_verbs:
#         if verb in cooking_action.lower():
#             print(str(step) + ": " + verb)
#     step = step + 1

#need to get phrases for what you cook with i.e. "in a saucepan", could do this with chunking, 
#but it should have an output that is easy to print (aka readable to the user)