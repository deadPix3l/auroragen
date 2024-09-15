from pydantic_xml import BaseXmlModel, element, attr
from pydantic import NonNegativeInt

# some meta stuff
class Element(BaseXmlModel, tag="element"):
    Element_type: str = attr(name="type")
    id: str = attr()
