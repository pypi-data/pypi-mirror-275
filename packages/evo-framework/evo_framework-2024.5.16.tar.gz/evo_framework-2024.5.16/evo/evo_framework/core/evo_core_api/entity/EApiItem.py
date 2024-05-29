from evo.evo_framework.entity.EObject import EObject
from evo.evo_framework.core.evo_core_type.entity.EvoMap import EvoMap
from evo.evo_framework.core.evo_core_api.entity.EnumApiType import EnumApiType

class EApiItem(EObject):
    #annotation
    def __init__(self):
        super().__init__()
        self.enumApiType:EnumApiType = EnumApiType.STRING
        self.mapEApiItem = EvoMap()
        
        #TODO:ADD TO SERIALIZE  
        self.eClass = None
        self.rangeDefault = None
        self.rangeMin = None
        self.rangeMax = None
          
    def toStream(self, stream):
        super().toStream(stream)
        self._doWriteInt(self.enumApiType.value, stream)
        self._doWriteMap(self.mapEApiItem, stream)
           
    def fromStream(self, stream):
        super().fromStream(stream)
        self.enumApiType = EnumApiType(self._doReadInt(stream))
        self._doReadMap(EApiItem, stream)
        
    def __str__(self) -> str:
        strReturn = "\n".join([
                            super().__str__(),        
                            f"enumApiType:{self.enumApiType}",  
                            f"mapEApiItem:{self.mapEApiItem}",               
                            ]) 
        return strReturn