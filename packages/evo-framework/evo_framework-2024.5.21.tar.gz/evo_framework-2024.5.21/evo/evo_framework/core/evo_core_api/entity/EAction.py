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
        self.inputData:bytes = None
        self.outputData:bytes = None
 
    def toStream(self, stream):
        super().toStream(stream)
        self._doWriteInt(self.enumApiAction.value, stream)
        self._doWriteStr(self.action, stream)
        self._doWriteBytes(self.inputData, stream)
        self._doWriteBytes(self.outputData, stream)
 
    def fromStream(self, stream):
        super().fromStream(stream)
        self.enumApiAction = EnumApiAction(self._doReadInt(stream))
        self.action = self._doReadStr(stream)
        self.inputData = self._doReadBytes( stream)
        self.outputData = self._doReadBytes(stream)

    def __str__(self) -> str:
        strReturn = "\n".join([
            super().__str__(),
            f"\tenumApiAction: {self.enumApiAction}",
            f"\taction: {self.action}",
            f"\tinputData: {len(self.inputData) if self.inputData else 'None'}",
            f"\toutputData: {len(self.outputData) if self.outputData else 'None'}"
        ])
        return strReturn