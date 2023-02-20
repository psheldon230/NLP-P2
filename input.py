from bs4 import BeautifulSoup
import requests
from recipe_scrapers import scrape_me
scraper = scrape_me("https://www.allrecipes.com/recipe/223382/chicken-stir-fry/")

instructions = scraper.instructions_list()

print(instructions[3])
