#!/usr/bin/env python3
from lxml import etree
from collections import defaultdict
from icecream import ic
from pprint import pp
import random

from pydantic import BaseModel
from enum import Enum

import requests
from bs4 import BeautifulSoup


banner = """
LL     .d888b.  RRRRRRr. EEEEEEEE        dAA LL      IIIIII .d888b.  
LL    d8P" "Y8b RR   rRr EE             dAAA LL        II  d8P  Y88b 
LL    88     88 RR    RR EE            dAPAA LL        II  Y8b.      
LL    88     88 RR   rRR EEEEEE       dAP AA LL        II   "Y88b.   
LL    88     88 RRRRRP"  EE          dAP  AA LL        II      "Y8b. 
LL    88     88 RR TRb   EE         dAP   AA LL        II        "88 
LL    Y8b. .d8P RR  TRb  EE        dAAAAAAAA LL        II  Y8b  d8P 
LLLLLL "Y888P"  RR   TRb EEEEEEEE dAP     AA LLLLLLL IIIIII "Y888P"  

            A DND 5e Character Generator for Aurora
"""
from jinja2 import Environment, FileSystemLoader

class TemplateData(BaseModel):
    title: str
    heading: str
    content: str

# Load the Jinja template from the file system
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)
template = env.get_template('template.dnd5e')

# Create an instance of the Pydantic model with data
data = TemplateData(
    title="My Page Title",
    heading="Welcome to My Page",
    content="This is the content of my page."
)

class Gender(Enum):
    MALE = 1
    FEMALE = 2
    # add non binary options? does aurora require a binary choice or support omitting?


class Stats(BaseModel):
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    @staticmethod
    def rolldice(d: int = 6, n: int = 4, droplow: bool = True) -> int:
        """ defaults to 4d6 drop lowest """
        rolls = [random.randint(1, d + 1) for i in range(n)]
        total = sum(rolls)
        if droplow:
            total -= min(rolls)
        return total

    @classmethod
    def randomize(cls):
        rollsdict = {k: cls.rolldice() for k in cls.__annotations__.keys()}
        return cls(**rollsdict)


class PlayerCharacter(BaseModel):
    name: str
    playerName: str = ""
    className: str
    race: str
    background: str = ""
    gender: Gender
    stats: Stats
    spells: list[str] = []
    items: list[str] = []


phb = etree.parse("players-handbook.index")
files = phb.find("files")

choices = defaultdict(list)
aux = []

for link in files.getiterator():
    if link.tag != "file":
        continue
    if "-" in link.get("name"):
        bucket, _, option = link.get("name").partition("-")
        choices[bucket].append(link.get("url"))
    else:
        aux.append(link.get("url"))

aux.extend(choices["items"])
del choices["items"]


for k, v in choices.items():
    z = random.choice(v)
    print(k, z)
    #print(BeautifulSoup(requests.get(z).text, features="xml"))


print(aux)
print("---------------")


character = PlayerCharacter(
    name="dave", className="paladin", race="gnome", gender=Gender.MALE, stats=Stats.randomize()
)


rendered_template = template.render(character.dict())

with open("output.dnd5e", "w") as f:
    f.write(rendered_template)

