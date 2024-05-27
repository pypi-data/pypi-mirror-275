from __future__ import annotations

from typing import Literal

from markupsafe import Markup
from ormspace import model as md



class SpaceModel(md.Model):
    
    def __format__(self, format_spec: Literal["markup"]) -> str:
        if format_spec == "markup":
            return str(self.markup())
        return str(self)
    
    def markup(self) -> Markup:
        raise NotImplementedError
    
    async def setup_instance(self):
        pass


    
class SpaceSearchModel(SpaceModel, md.SearchModel):
    pass