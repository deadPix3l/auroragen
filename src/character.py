from pydantic_xml import BaseXmlModel, element, attr, wrapped
from pydantic import NonNegativeInt, PositiveInt

from inventory import Item


class Appearance(BaseXmlModel, tag="appearance"):
    portrait: str = element()
    age: PositiveInt = element()
    height: str = element()
    weight: str = element()
    eyes: str = element()
    skin: str = element()
    hair: str = element()

class Stats(BaseXmlModel):
    strength: NonNegativeInt = element(default=10)
    dexterity: NonNegativeInt = element(default=10)
    constitution: NonNegativeInt = element(default=10)
    intelligence: NonNegativeInt = element(default=10)
    wisdom: NonNegativeInt = element(default=10)
    charisma: NonNegativeInt = element(default=10)

class Skill(BaseXmlModel, tag="skill"):
    name: str = attr()
    value: NonNegativeInt

class Skills(BaseXmlModel, tag="skills"):
    skills: list[Skill] = element(tag="skill")

class Character(BaseXmlModel, tag="character"):
    name: str = element()
    race: str = element()
    className: str = element(tag="class")
    archetype: str = element(default="")
    background: str = element(default="")
    level: PositiveInt = element()
    appearance: Appearance = element()
    abilities: Stats = element(tag="abilities")
    skills: list[Skill] = wrapped("skills", wrapped("a", element()))
    #equipment: list[Item] = element()
