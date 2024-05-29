from  evo.evo_framework.entity.EObject import EObject
from evo.evo_framework.core.evo_core_type.entity.EvoMap import EvoMap
from evo.evo_framework.core.evo_core_api.entity.EnumApiCrypto import EnumApiCrypto
from evo.evo_framework.core.evo_core_api.entity.EnumApiType import EnumApiType
from evo.evo_framework.core.evo_core_api.entity.EApi import EApi
from enum import Enum
import importlib
class EnumApiVisibility(Enum):
    PUBLIC = 0
    PRIVATE = 1

class EnumApiTunnel(Enum):
    LOCAL = 0
    CYBORGAI = 1
    NGROK = 2
    PINGGY = 3
    
class EApiConfig(EObject):
    def __init__(self):
        super().__init__()
        self.enumApiCrypto:EnumApiCrypto = EnumApiCrypto.ECC
        self.enumApiVisibility:EnumApiVisibility = EnumApiVisibility.PRIVATE
        self.enumApiTunnel:EnumApiTunnel = EnumApiTunnel.LOCAL
        self.publicKey:bytes = None
        self.label:str = None
        self.description:str = None
        self.urlLogo:str = None
        self.remoteUrl:str = None
        self.remotePort:int = 443
        self.os:str = None
        self.mapEApi:EvoMap = EvoMap()
        

        '''
        self.cryptoWallet:dict={
                            'bitcoin':"BITCOIN_ADDRESS",
                            'ethereum':"ETHEREUM_ADDRESS",
                            'polygon':"POLYGON_ADDRESS",
                            'bnb':"BNB_ADDRESS",
                            'paypal':"PAYPAL_EMAIL"
                            } 
        '''
        #NOT SERIALIZE
        self.cyborgaiToken:str = None
        self.secretKey:bytes = None
        self.isFirstStart:bool = True
        self.localAddress:str = "0.0.0.0"
        self.localPort:int = 8001
        self.mapSerialize = {}
        
    def getMapSerialize(self):
        self.mapSerialize[0]: EnumApiType.STRING
        self.mapSerialize[1]: EnumApiType.LONG
        
        
        
    def toStream(self, stream):
        super().toStream(stream)
        self._doWriteInt(self.enumApiCrypto.value, stream)
        self._doWriteInt(self.enumApiVisibility.value, stream)
        self._doWriteInt(self.enumApiTunnel.value, stream)
        self._doWriteBytes(self.publicKey, stream)
        self._doWriteStr(self.label, stream)
        self._doWriteStr(self.description, stream)
        self._doWriteStr(self.urlLogo, stream)
        self._doWriteStr(self.remoteUrl, stream)
        self._doWriteInt(self.remotePort, stream)
        self._doWriteStr(self.os, stream)
        self._doWriteMap(self.mapEApi, stream)
       
        
    def fromStream(self, stream):
        super().fromStream(stream) 
        self.enumApiCrypto = EnumApiCrypto(self._doReadInt(stream))
        self.enumApiVisibility = EnumApiVisibility(self._doReadInt(stream))
        self.enumApiTunnel = EnumApiTunnel(self._doReadInt(stream))
        self.publicKey = self._doReadBytes(stream)
        self.label = self._doReadStr(stream)
        self.description = self._doReadStr(stream)
        self.urlLogo = self._doReadStr(stream)
        self.remoteUrl = self._doReadStr(stream)
        self.remotePort = self._doReadInt(stream)
        self.os = self._doReadStr(stream)
        self.mapEApi = self._doReadMap(EApi, stream)
    
    def __str__(self) -> str:
        strReturn = "\n".join([
                            super().__str__(),
                            f"enumApiCrypto:{self.enumApiCrypto}",
                            f"enumApiVisibility:{self.enumApiVisibility}",
                            f"enumApiTunnel:{self.enumApiTunnel}",
                            f"publicKey:{self.publicKey!r}",
                            f"title:{self.label}",
                            f"description:{self.description}",
                            f"urlLogo:{self.urlLogo}",
                            f"remoteUrl:{self.remoteUrl}",
                            f"remotePort:{self.remotePort}",
                            f"os:{self.os}",
                            f"mapEApi:{self.mapEApi}",
                            ]) 
        return strReturn
#WRAPPER 

