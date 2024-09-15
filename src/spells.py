from pydantic_xml import BaseXmlModel, element, attr
from pydantic import NonNegativeInt

class Spell(BaseXmlModel, tag="spell"):
    name: str = attr()
    level: str | int = attr()
    id: str = attr()
    always_prepared: bool = attr(name="always-prepared")
    known: bool = attr()
