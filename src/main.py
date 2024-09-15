#!/usr/bin/env python
from pydantic_xml import BaseXmlModel, element, attr
from pydantic import NonNegativeInt

from character import Character

if __name__=="__main__":
    with open("xmls/text.xml") as f:
        xmlfile = f.read()

    c = Character.from_xml(xmlfile)
    print(
        c.to_xml(
            pretty_print=True,
            encoding="UTF-8"
        )
        .decode("utf-8")
    )

