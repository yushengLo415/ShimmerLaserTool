from MetalSheet import MetalSheet
from LaserInformation import LaserInfo

class Product:

    def __init__(self):
        self._name = "請輸入件號/品名規格"
        self._count = int(0)
        self._type = int(0)
        self._metalSheet = MetalSheet()
        self._laserInfo = LaserInfo()
    
    def GetName(self):
        return self._name
    
    def GetCount(self):
        return self._count
    
    def GetType(self):
        return self._type
    
    def GetTypeInString(self):
        if self._type == 0:
            return "黑鐵"
        elif self._type == 1:
            return "白鐵"
        else:
            return "鋁"
    
    def GetMetalSheet(self):
        return self._metalSheet
    
    def GetLaserInfo(self):
        return self._laserInfo
            
    def GetPrice(self):
        return (self._metalSheet.GetPrice() + self._laserInfo.GetPrice()) * self._count
        
    def SetName(self, name):
        self._name = name

    def SetCount(self, count):
        self._count = count

    def SetType(self, type):
        self._type = type
        self._metalSheet.SetType(type)
        self._laserInfo.SetType(type)
        

        


