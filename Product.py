
class Product:

    def __init__(self, name, count, metalSheet, metalSheetDiscount, laserInfo, laserDiscount):
        self._name = name
        self._count = int(count)
        self._metalSheet = metalSheet
        self._laserInfo = laserInfo
        #下列兩項代表原始價格
        self._metalSheetPrice = 0
        self._laserCost = 0
        #下列兩項代表多少折扣
        self._metalSheetDiscount = metalSheetDiscount
        self._laserDiscount = laserDiscount
        #下列兩項代表折扣完的價格
        self._discountedMetalSheetPrice = 0
        self._discountedLaserCost = 0
        self._total = 0

    def GetName(self):
        return self._name
    
    def GetCount(self):
        return self._count
    
    def GetMetalSheet(self):
        return self._metalSheet
    
    def GetLaserInfo(self):
        return self._laserInfo
 
    def GetMetalSheetPrice(self):
        return self._metalSheetPrice
  
    def GetLaserCost(self):
        return self._laserCost
    
    def GetMetalSheetDiscount(self):
        return self._metalSheetDiscount

    def GetLaserDiscount(self):
        return self._laserDiscount
    
    def GetDiscountedMetalSheetPrice(self):
        return self._discountedMetalSheetPrice

    def GetDiscountedLaserCost(self):
        return self._discountedLaserCost
    
    def GetTotal(self):
        return self._total
        
    def SetName(self, name):
        self._name = name

    def SetCount(self, count):
        self._count = count

    def SetMetalSheetPrice(self, metalSheetPrice):
        self._metalSheetPrice = metalSheetPrice

    def SetLaserCost(self, laserCost):
        self._laserCost = laserCost
      
    def SetMetalSheetDiscount(self, metalSheetDiscount):
        self._metalSheetDiscount = metalSheetDiscount

    def SetLaserDiscount(self, laserDiscount):
        self._laserDiscount = laserDiscount

    def SetDiscountedMetalSheetPrice(self, discountedMetalSheetPrice):
        self._discountedMetalSheetPrice = discountedMetalSheetPrice

    def SetDiscountedLaserCost(self, discountedLaserCost):
        self._discountedLaserCost = discountedLaserCost

    def SetTotal(self, total):
        self._total = total
        


