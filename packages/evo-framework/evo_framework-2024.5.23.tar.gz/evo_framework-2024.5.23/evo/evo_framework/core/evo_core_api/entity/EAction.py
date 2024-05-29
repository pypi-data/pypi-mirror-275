from evo.evo_framework.entity.EObject import EObject
from evo.evo_framework.core.evo_core_type.entity.EvoMap import EvoMap
from evo.evo_framework.core.evo_core_api.entity.EnumApiAction import EnumApiAction
from evo.evo_framework.core.evo_core_api.entity.EActionItem import EActionItem
from evo.evo_framework.core.evo_core_api.entity.EnumApiType import EnumApiType

class EAction(EObject):
    #annotation
  
    def __init__(self):
        super().__init__()
        self.enumApiAction:EnumApiAction = EnumApiAction.NONE
        self.action:str = None       
        self.input:bytes = None
        self.output:bytes = None
 
    def toStream(self, stream):
        super().toStream(stream)
        self._doWriteInt(self.enumApiAction.value, stream)
        self._doWriteStr(self.action, stream)
        self._doWriteBytes(self.input, stream)
        self._doWriteBytes(self.output, stream)
 
    def fromStream(self, stream):
        super().fromStream(stream)
        self.enumApiAction = EnumApiAction(self._doReadInt(stream))
        self.action = self._doReadStr(stream)
        self.input = self._doReadBytes( stream)
        self.output = self._doReadBytes(stream)

    def __str__(self) -> str:
        strReturn = "\n".join([
            super().__str__(),
            f"\tenumApiAction: {self.enumApiAction}",
            f"\taction: {self.action}",
            f"\tinput len: {len(self.input) if self.input else 'None'}",
            f"\toutput len: {len(self.output) if self.output else 'None'}"
        ])
        return strReturn