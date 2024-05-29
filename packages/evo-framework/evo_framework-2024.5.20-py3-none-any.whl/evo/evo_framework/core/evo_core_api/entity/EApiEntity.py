from evo.evo_framework.entity.EObject import EObject
from evo.evo_framework.core.evo_core_type.entity.EvoMap import EvoMap
from evo.evo_framework.core.evo_core_api.entity.EnumApiType import EnumApiType
from evo.evo_framework.core.evo_core_api.entity.EApi import EApi
from evo.evo_framework.core.evo_core_api.entity.EApiItem import EApiItem
from evo.evo_framework.core.evo_core_api.utility.IuApi import IuApi
from evo.evo_framework.core.evo_core_log.utility.IuLog import IuLog
class EApiEntity(EObject):
    #annotation
  
    def __init__(self, eApi:EApi):
        super().__init__()
        self.eApi:EApi = eApi
        self.id = self.eApi.id
        
      
    # ------------------------------------------------------------------------------------------------
    def addInput(self, id:str, enumApiType:EnumApiType , default:any = None, rangeMin:any = None, rangeMax:any = None):
        try: 
            eApiItem= EApiItem()
            eApiItem.id = id
            eApiItem.doGenerateTime()
            eApiItem.enumApiType = enumApiType
            
            #TODO:check enumType
            eApiItem.rangeDefault = default
            eApiItem.rangeMin = rangeMin
            eApiItem.rangeMax = rangeMax 
            self.eApi.mapInput.doSet(eApiItem)
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise exception
# ------------------------------------------------------------------------------------------------     
    def addOutput(self,eApi:EApi, id:str, enumApiType:EnumApiType ):
        try: 
            eApiItem= EApiItem()
            eApiItem.id = id
            eApiItem.doGenerateTime()
            eApiItem.enumApiType = enumApiType
            eApi.mapOutput.doSet(eApiItem)
            
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
            self.eApi.mapInput.doSet(eApiItem)
            
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
            self.eApi.mapOutput.doSet(eApiItem)

            return eApiItem      
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise exception
# ------------------------------------------------------------------------------------------------
    def addMapItem(self,eApiItemMap:EApiItem, id:str, enumApiType:EnumApiType , default:any = None, rangeMin:any = None, rangeMax:any = None):
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
         
    def toStream(self, stream):
        self._doWriteEObject(self.eApi, stream)
      
        
    def fromStream(self, stream):
        self.eApi= self._doReadEObject(EApi, stream)
    
    def __str__(self) -> str:
        strReturn = "\n".join([
                            super().__str__(),
                            f"input:\n{self.eApi.mapInput}",
                            f"output:\n{self.eApi.mapOutput}",
                            ]) 
        return strReturn
    