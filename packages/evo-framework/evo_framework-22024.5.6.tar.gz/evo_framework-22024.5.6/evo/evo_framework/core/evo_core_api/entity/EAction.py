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
        self.mapInput:EvoMap = EvoMap()
        self.mapOutput:EvoMap = EvoMap()
        #NOT SERIALIZED
        self.mapItemTypeCache = {}
        
    def toStream(self, stream):
        super().toStream(stream)
        self._doWriteInt(self.enumApiAction.value, stream)
        self._doWriteStr(self.action, stream)
        self._doWriteMap(self.mapInput, stream)
        self._doWriteMap(self.mapOutput, stream)
    
        
    def fromStream(self, stream):
        super().fromStream(stream)
        self.enumApiAction = EnumApiAction(self._doReadInt(stream))
        self.action = self._doReadStr(stream)
        self.mapInput = self._doReadMap(EActionItem, stream)
        self.mapOutput = self._doReadMap(EActionItem, stream)

    
    def __str__(self) -> str:
        strReturn = "\n".join([
                            super().__str__(),
                            f"\tenumApiAction:{self.enumApiAction}",
                            f"\taction:{self.action}",
                            f"\tmapInput:{self.mapInput}",
                            f"\tmapOutput:{self.mapOutput}",
                            ]) 
        return strReturn
    
    #LOCAL WRAPPER EXTENSION
    def doSetInput(self, enumApiType:EnumApiType, idItem:str,  data, typeExt:str = None, isUrl:bool = False):
        from evo.evo_framework.core.evo_core_api.utility.IuApi import IuApi
        eActionItem = EActionItem()
        eActionItem.id = idItem
        eActionItem.enumApiType = enumApiType
        eActionItem.typeExt = typeExt
        eActionItem.doGenerateTime()
        eActionItem.data = IuApi.toData(enumApiType, data)
        self.mapInput.doSet(eActionItem)
        self.doGenerateTime()
    
    async def doGetInput(self, idItem:str, isRaw=False, ECLASS=None):
        from evo.evo_framework.core.evo_core_api.utility.IuApi import IuApi
        if idItem in self.mapInput.keys():
            eActionItem:EActionItem=self.mapInput.doGet(idItem)
        else:
            raise Exception(f"ERROR_ITEM_NOT_PRESENT_{idItem}")
        
        if eActionItem.enumApiType == EnumApiType.MAP:
            return eActionItem
        
        if isRaw :
            return await IuApi.fromItem(self, idItem, isRaw=isRaw, ECLASS=ECLASS)
        
        if idItem not in self.mapItemTypeCache:
           self.mapItemTypeCache[idItem] = await IuApi.fromItem(eActionItem.enumApiType, eActionItem.data, eActionItem.typeExt, ECLASS=ECLASS)
      
        return self.mapItemTypeCache[idItem]
    
    def doSetOutput(self, enumApiType:EnumApiType, idItem:str,  data, typeExt:str = None, isUrl:bool = False):
        from evo.evo_framework.core.evo_core_api.utility.IuApi import IuApi
        eActionItem = EActionItem()
        eActionItem.id = idItem
        eActionItem.enumApiType = enumApiType
        eActionItem.typeExt = typeExt
        eActionItem.doGenerateTime()
        eActionItem.data = IuApi.toData(enumApiType, data)
        self.mapOutput.doSet(eActionItem)
        self.doGenerateTime()
    
    async def doGetOutput(self, idItem:str, isRaw=False, ECLASS=None):
        from evo.evo_framework.core.evo_core_api.utility.IuApi import IuApi
        if idItem in self.mapOutput.keys():
            eActionItem:EActionItem=self.mapOutput.doGet(idItem)
        else:
            raise Exception(f"ERROR_ITEM_NOT_PRESENT_{idItem}")
        
        if eActionItem.enumApiType == EnumApiType.MAP:
            return eActionItem
        
        if isRaw :
            return await IuApi.fromItem(self, idItem, isRaw=isRaw, ECLASS=ECLASS)
        
        if idItem not in self.mapItemTypeCache:
           self.mapItemTypeCache[idItem] = await IuApi.fromItem(eActionItem.enumApiType, eActionItem.data, eActionItem.typeExt, ECLASS=ECLASS)
      
        return self.mapItemTypeCache[idItem]
    
    def doDelInput(self, idItem:str):
        self.mapInput.doDel(idItem)
        
    def doDelAllInput(self,) :    
        del self.mapInput
        self.mapInput = EvoMap()
        self.doGenerateTime()
        
    def doDelOutput(self, idItem:str):
        self.mapOutput.doDel(idItem)
        
    def doDelAllOutput(self,) :    
        del self.mapOutput
        self.mapOutput = EvoMap()
        self.doGenerateTime()
        
    def newMapInput(self, id:str) -> EActionItem:    
        eApiType = EActionItem()
        eApiType.id = id
        eApiType.enumApiType = EnumApiType.MAP
        eApiType.doGenerateTime()
        self.mapInput.doSet(eApiType)
        return eApiType
    
    def newMapOutput(self, id:str) -> EActionItem:    
        eApiType = EActionItem()
        eApiType.id = id
        eApiType.enumApiType = EnumApiType.MAP
        eApiType.doGenerateTime()
        self.mapOutput.doSet(eApiType)
        return eApiType