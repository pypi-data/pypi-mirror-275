from evo.evo_framework.entity.EObject import EObject
from evo.evo_framework.core.evo_core_type.entity.EvoMap import EvoMap
from evo.evo_framework.core.evo_core_api.entity.EnumApiType import EnumApiType

class EActionItem(EObject):
    #annotation
    def __init__(self):
        super().__init__()
        self.enumApiType:EnumApiType = EnumApiType.STRING
        self.isUrl:bool = False
        self.typeExt:str = None
        self.data:bytes =None
        self.mapEActionItem = EvoMap()
        #NOT SERIALIZED
        self.mapItemType = {}
          
    def toStream(self, stream):
        super().toStream(stream)
        self._doWriteInt(self.enumApiType.value, stream)
        self._doWriteBool(self.isUrl, stream)
        self._doWriteStr(self.typeExt, stream)
        self._doWriteBytes(self.data, stream)
        self._doWriteMap(self.mapEActionItem, stream)
        
    def fromStream(self, stream):
        super().fromStream(stream)
        self.enumApiType = EnumApiType(self._doReadInt(stream))
        self.isUrl = self._doReadBool(stream)
        self.typeExt = self._doReadStr(stream)
        self.data = self._doReadBytes(stream)
        self.mapEActionItem = self._doReadMap(EActionItem,stream)
        
    def __str__(self) -> str:
        strReturn = "\n".join([
                            super().__str__(),
                            f"\tenumApiType:{self.enumApiType}",
                            f"\tisUrl:{self.isUrl}",
                            f"\ttypeExt:{self.typeExt}",
                            f"\tdata:{ len(self.data) if self.data is not None else None}",
                            f"\tmapEActionItem:{self.mapEActionItem}",
                            ]) 
        return strReturn
    
    #LOCAL WRAPPER EXTENSION
    def newEntity(self,id:str):    
        eActionItem = EActionItem()
        eActionItem.id = id
        eActionItem.enumApiType = EnumApiType.MAP
        eActionItem.doGenerateTime()
        self.mapEActionItem.doSet(eActionItem)
        self.doGenerateTime()
        return eActionItem
    
    def doSet(self, enumApiType:EnumApiType,idItem:str, data, typeExt:str = None, isUrl:bool = False ):
        from evo.evo_framework.core.evo_core_api.utility.IuApi import IuApi
        eActionItem = EActionItem()
        eActionItem.id = idItem
        eActionItem.enumApiType = enumApiType
        eActionItem.typeExt = typeExt
        eActionItem.doGenerateTime()
        eActionItem.data = IuApi.toData(enumApiType, data)
        self.mapEActionItem.doSet(eActionItem)
        self.doGenerateTime()
    
    async def doGet(self, idItem:str, isRaw=False, ECLASS=None):
        from evo.evo_framework.core.evo_core_api.utility.IuApi import IuApi 
        eActionItem:EActionItem = self.mapEActionItem.doGet(idItem)    
        
        if eActionItem is None:
            raise Exception(f"ERROR_ITEM_NOT_PRESENT_{idItem}")
        
        if eActionItem.enumApiType == EnumApiType.MAP:
            return eActionItem
        
        
        if isRaw :
            return eActionItem.data
        else:
            if idItem not in self.mapItemType:
                self.mapItemType[idItem] =  await IuApi.fromItem(eActionItem.enumApiType, eActionItem.data, eActionItem.typeExt, ECLASS=ECLASS)
            return self.mapItemType[idItem]  
    
    def doDel(self, idItem:str):
        self.mapEActionItem.doDel(idItem)
            
