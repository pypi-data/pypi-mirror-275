from evo.evo_framework.entity.EObject import EObject
from evo.evo_framework.core.evo_core_type.entity.EvoMap import EvoMap
from evo.evo_framework.core.evo_core_api.entity.EApiItem import EApiItem
from evo.evo_framework.core.evo_core_api.entity.EnumApiType import EnumApiType
from evo.evo_framework.core.evo_core_log.utility.IuLog import IuLog
class EApi(EObject):
    #annotation
    
    def __init__(self):
        super().__init__()
        self.description:str = None
        self.isStream:bool = False       
        self.input:str = None
        self.output:str = None

        #NOT_SERIALIZED
        self.context = {}
        self.callback = None
        self.isEnabled:bool = True
        
    def toStream(self, stream):
        super().toStream(stream)
        self._doWriteStr(self.description, stream)
        self._doWriteBool(self.isStream, stream)
        self._doWriteStr(self.input, stream)
        self._doWriteStr(self.output, stream)

    def fromStream(self, stream):
        super().fromStream(stream)
        self.description = self._doReadStr(stream)
        self.isStream = self._doReadBool(stream)
        self.input = self._doReadStr(stream)
        self.output = self._doReadStr(stream)

    def __str__(self) -> str:
        strReturn = "\n".join([
                            super().__str__(),        
                            f"\tisStream:{self.isStream}",
                            f"\tcontext:{self.context}",
                            f"\tinput:{self.input}", 
                            f"\toutput:{self.output}",
                            f"callback:{self.callback}",                  
                            ]) 
        return strReturn