from recipe_scrapers import scrape_me
import spacy
nlp = spacy.load("en_core_web_sm")

cooking_verbs = ["add","break","boil","blend","bake","barbecue","cut","cover","crush","cool",
                 "chop","dip","dice","decorate","drain","fry","flip","grind","grate","grill",
                 "heat","knead","layer","light","measure","mix","microwave","mash","melt","mince"
                 "marinate","peel","pour","put",'remove',"roast","refridgerate","roll","rinse","stir",
                 "scramble","sprinkle","squeeze","spread","steam","simmer","slice","saute","sip","sharpen",
                 "sift","toss","turn off","tenderize","taste","toast","weigh","whisk","wash","combine","separate",
                 "cook","serve","transfer","move","heat","set","reserve","season","peel"]

cooking_units = [
    'teaspoon', 'teaspoons', 
    'tablespoon', 'tablespoons', 
    'cup', 'cups', 
    'egg', 'eggs',
    'fluid', 'fluids', 
    'ounce', 'ounces', 
    'pint', 'pints', 
    'quart', 'quarts', 
    'gallon', 'gallons',
    'pound', 'pounds', 
    'milliliter', 'milliliters',
    'liter', 'liters', 
    'milligram', 'milligrams', 
    'gram', 'grams',
    'kilogram', 'kilograms', 
    'millimeter', 'millimeters', 
    'centimeter', 'centimeters', 
    'meter', 'meters', 
    'square', 'squares', 
    'foot', 'feet', 
    'inch', 'inches',
    'cubic', 'cubics', 
    'pinch', 'pinches', 
    'dash', 'dashes', 
    'drop', 'drops', 
    'smidgen', 'smidgens', 
    'scruple', 'scruples', 
    'coffeespoon', 'coffeespoons', 
    'deciliter', 'deciliters', 
    'hectoliter', 'hectoliters', 
    'barrel', 'barrels', 
    'hogshead', 'hogsheads',
    'cupcake', 'cupcakes', 
    'jigger', 'jiggers', 
    'pony', 'ponies', 
    'shot', 'shots', 
    'drachm', 'drachms', 
    'tenth', 'tenths', 
    'firkin', 'firkins', 
    'gill', 'gills', 
    'pottle', 'pottles', 
    'quart', 'quarts', 
    'seam', 'seams', 
    'stere', 'steres', 
    'strike', 'strikes', 
    'peck', 'pecks', 
    'bushel', 'bushels', 
    'milliequivalent', 'milliequivalents', 
    'millicurie', 'millicuries', 
    'millilitre', 'millilitres', 
    'dekalitre', 'dekalitres', 
    'petalitre', 'petalitres', 
    'micrometre', 'micrometres', 
    'megagram', 'megagrams', 
    'kilometer', 'kilometers', 
    'yard', 'yards', 
    'fathom', 'fathoms', 
    'mile', 'miles', 
    'nauticalmile', 'nauticalmiles', 
    'gramforce', 'gramforces', 
    'kilopascal', 'kilopascals', 
    'atmosphere', 'atmospheres', 
    'pascal', 'pascals', 
    'poundforce', 'poundforces', 
    'newton', 'newtons', 
    'dyne', 'dynes'
]
#if empty its previous ingredients
def find_ingredients(instruction,ingredients):
    step_ingredients = []
    doc =  nlp(instruction)
    for chunk in doc.noun_chunks:
        for ingredient in ingredients:
            if chunk.root.text.lower() in ingredient and chunk.text not in step_ingredients and chunk.root.text.lower() != 'C' and chunk.root.text.lower() != 'F':
                    step_ingredients.append(ingredient)
                    
    return step_ingredients


#get time if any
def get_time(instruction):
    doc = nlp(instruction)
    time_adjectives = ['minute', 'minutes', 'hour', 'hours', 'second', 'seconds']
    time_limit_phrases = []
    for child in doc:
                if child.pos_ == 'NOUN' and child.text.lower() in time_adjectives:
                    time_phrase = ''
                    for grandchild in child.children:
                        if grandchild.pos_ == 'NUM' and grandchild.is_digit:
                            time_phrase += grandchild.text + ' '
                        elif grandchild.pos_ == 'SYM' and grandchild.text in ['-', 'to']:
                            time_phrase += grandchild.text + ' '
                    if time_phrase:
                        time_phrase += child.text
                        time_limit_phrases.append(time_phrase)
                        
    return time_limit_phrases

#get tools
def get_tools(instruction):
    doc = nlp(instruction)
    prepositions = ["in", "on","into"]
    pps = []
    for token in doc:
        # Try this with other parts of speech for different subtrees.
        if token.text in prepositions:
            pp = ' '.join([tok.orth_ for tok in token.subtree])
            pps.append(pp)

    return pps

#gets info like: "over high heat", "until browned", "to 370 degrees" ,"to a boil"
def get_extra(instruction):
    doc = nlp(instruction)
    prepositions = ["at", "to", "until","till"]
    pps = []
    for token in doc:
        # Try this with other parts of speech for different subtrees.
        if token.text in prepositions:
            pp = ' '.join([tok.orth_ for tok in token.subtree])
            pps.append(pp)

    return pps



def get_verb2(instruction):
    doc =  nlp(instruction)
    verbs = []
    for token in doc:
    # If the token is a verb
        if (token.pos_ == "VERB" and token.tag_ == "VB") or token.text.lower() in cooking_verbs:
            verbs.append(token.text)

    return verbs

def get_quantity(instruction_str, ingredients_list):
    ing_list = find_ingredients(instruction_str, ingredients_list)
    ingredients = []
    for ing in ing_list:
        quantity = None
        unit = None
        doc = nlp(ing)
        for token in doc:
            if token.pos_ == "NUM" and token.i < len(doc) - 1:
                quantity = token
                if doc[token.i + 1].text.lower() in cooking_units:
                    unit = doc[token.i + 1]
        ingredients.append({"quantity": quantity, "unit": unit})
    return ingredients
    