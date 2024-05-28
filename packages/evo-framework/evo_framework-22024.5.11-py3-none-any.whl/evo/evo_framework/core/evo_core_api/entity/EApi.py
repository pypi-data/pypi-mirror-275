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
        self.mapInput = EvoMap()
        self.mapOutput = EvoMap()
        
        #NOT_SERIALIZED
        self.context = {}
        self.callback = None
        self.isEnabled:bool = True
        
    def toStream(self, stream):
        super().toStream(stream)
        self._doWriteStr(self.description, stream)
        self._doWriteBool(self.isStream, stream)
        self._doWriteMap(self.mapInput, stream)
        self._doWriteMap(self.mapOutput, stream)
        
    def fromStream(self, stream):
        super().fromStream(stream)
        self.description = self._doReadStr(stream)
        self.isStream = self._doReadBool(stream)
        self.mapInput = self._doReadMap(EApiItem, stream)
        self.mapOutput = self._doReadMap(EApiItem, stream)
    
    def __str__(self) -> str:
        strReturn = "\n".join([
                            super().__str__(),        
                            f"isStream:{self.isStream}",
                            f"context:{self.context}",
                            f"mapInput:{self.mapInput}", 
                            f"mapOutput:{self.mapOutput}", 
                            f"callback:{self.callback}",                  
                            ]) 
        return strReturn
    

#WRAPPER EXTENSION
# ------------------------------------------------------------------------------------------------
    def addInput(self, id:str, enumApiType:EnumApiType , eClass=None, default:any=None, rangeMin:any=None, rangeMax:any=None):
        try: 
            eApiItem= EApiItem()
            eApiItem.id = id
            eApiItem.doGenerateTime()
            eApiItem.enumApiType = enumApiType
            
            
            if enumApiType == EnumApiType.EOBJECT:
                if eClass is None:
                    raise Exception("ERROR_ECLASS_NONE")
                eApiItem.eClass = eClass
            
            
            #TODO:check enumType
            eApiItem.rangeDefault = default
            eApiItem.rangeMin = rangeMin
            eApiItem.rangeMax = rangeMax 
            
            self.mapInput.doSet(eApiItem)
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise exception
# ------------------------------------------------------------------------------------------------     
    def addOutput(self, id:str, enumApiType:EnumApiType, eClass=None, default:any=None, rangeMin:any=None, rangeMax:any=None):
        try: 
            eApiItem= EApiItem()
            eApiItem.id = id
            eApiItem.doGenerateTime()
            eApiItem.enumApiType = enumApiType
            
            if enumApiType == EnumApiType.EOBJECT:
                if eClass is None:
                    raise Exception("ERROR_ECLASS_NONE")
                eApiItem.eClass = eClass
            
            
            #TODO:check enumType
            eApiItem.rangeDefault = default
            eApiItem.rangeMin = rangeMin
            eApiItem.rangeMax = rangeMax 
            
            self.mapOutput.doSet(eApiItem)
            
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise exception

# ------------------------------------------------------------------------------------------------
    def newMapInput(self, id:str ) -> EApiItem:
        try: 
            eApiItem= EApiItem()
            eApiItem.id = id
            eApiItem.doGenerateTime()
            eApiItem.enumApiType = EnumApiType.MAP
            #TODO:check enumType
            self.mapInput.doSet(eApiItem)
            return eApiItem      
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise exception
        
# ------------------------------------------------------------------------------------------------
    def newMapOutput(self, id:str ) -> EApiItem:
        try: 
            eApiItem= EApiItem()
            eApiItem.id = id
            eApiItem.doGenerateTime()
            eApiItem.enumApiType = EnumApiType.MAP
            self.mapOutput.doSet(eApiItem)

            return eApiItem      
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise exception
# ------------------------------------------------------------------------------------------------
    def addMapEntity(self,eApiItemMap:EApiItem, enumApiType:EnumApiType, id:str,  default:any = None, rangeMin:any = None, rangeMax:any = None):
        try: 
          
            if eApiItemMap.enumApiType.value == EnumApiType.MAP.value:
                eApiItem= EApiItem()
                eApiItem.id = id
                eApiItem.doGenerateTime()
                eApiItem.enumApiType = enumApiType
                
                #TODO:check enumType
                eApiItem.rangeDefault = default
                eApiItem.rangeMin = rangeMin
                eApiItem.rangeMax = rangeMax
                eApiItemMap.mapEApiItem.doSet(eApiItem)
                
            else:
                raise Exception("ERROR_NOT_VALID_MAP")
            
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise exception