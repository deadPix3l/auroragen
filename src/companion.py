from pydantic_xml import BaseXmlModel, element, attr
from pydantic import NonNegativeInt

class Companion(BaseXmlModel, tag="character"):
    attributes: Stats = element()
    #saves: Saves = element()
    skills: Skills = element()
