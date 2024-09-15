from pydantic_xml import BaseXmlModel, element, attr
from pydantic import NonNegativeInt

class Details(BaseXmlModel, tag="details"):
    card: bool =  attr(default=True)
    name: str = element(default="")
    notes: str = element(default="")

class Item(BaseXmlModel, tag="item"):
    id: str = attr()
    identifier: str = attr()
    name: str = attr()
    equipped: bool = element()
    details: Details = element()

class Currency(BaseXmlModel, tag="currency"):
    copper: NonNegativeInt = element()
    silver: NonNegativeInt = element()
    electrum: NonNegativeInt = element()
    gold: NonNegativeInt = element()
    platinum: NonNegativeInt = element()
    equipment: str = element(default="")
    treasure: str = element(default="")

