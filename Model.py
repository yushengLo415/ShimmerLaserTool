from mysqlConnector import mysqlConnector

class Model:

    _productList = []
    _blackIronPrice = 0
    _whiteIronPrice = 0
    _aluminumPrice = 0
    _totalPrice = 0
    _dbConnector = mysqlConnector()
 
    #""中為厚度，[]中分為別黑鐵、白鐵、鋁切割長度/米的價格與打孔的價格
    #若孔徑 > 14mm，打孔的額外收費雙倍
    _laserCostDict = {
        "0":[0, 0, 0, 0],
        "1":[20, 40, 40, 2],
        "2":[20, 40, 40, 2],
        "3":[30, 60, 60, 2],
        "4":[40, 80, 80, 2],
        "5":[50, 100, 100, 3],
        "6":[60, 120, 120, 3],
        "8":[80, 160, 160, 4],
        "9":[90, 180, 180, 4],
        "10":[100, 200, 200, 4],
        "12":[120, 240, 240, 4],
        "16":[200, 400, 400, 6],
        "20":[300, 600, 600, 8]
    }

    #透過密度分辨為哪種金屬，以決定板材單價與雷射價格
    _materialInfoDict = {
        0.00000785:[_blackIronPrice, 0],
        0.00000793:[_whiteIronPrice, 1],
        0.00000271:[_aluminumPrice, 2]
    }

    def __init__(self):
        pass

    def AddProduct(self, product):
        self.tempProduct = product
        self._computeMetalSheetWeight()
        self._computePrice()
        self._computeDiscountAndTotal()
        self._productList.append(self.tempProduct)

    #重量 = 密度*面積*厚度
    def _computeMetalSheetWeight(self):
        metalSheet = self.tempProduct.GetMetalSheet()
        metalSheet.SetWeight(metalSheet.GetDensity() * metalSheet.GetArea() * metalSheet.GetThickness())

    def _computePrice(self):
        metalSheet = self.tempProduct.GetMetalSheet()
        laserInfo = self.tempProduct.GetLaserInfo()

        #板材費用 = 重量 * 單價 * 數量
        metalSheetPrice = metalSheet.GetWeight() * self._materialInfoDict[metalSheet.GetDensity()][0] * self.tempProduct.GetCount()
        self.tempProduct.SetMetalSheetPrice(metalSheetPrice)

        #直線切割長度工資
        try:
            lineCost = laserInfo.GetLength() * self._laserCostDict[str(metalSheet.GetThickness())][self._materialInfoDict[metalSheet.GetDensity()][1]]
        except KeyError:
            metalSheet.SetThickness(0)
            lineCost = 0
            print("Wrong Thickness")

        #切孔工資(若孔徑 > 14mm，打孔的額外收費雙倍)
        largeHoleCost = 2 * laserInfo.GetLargeHoleCount() * self._laserCostDict[str(metalSheet.GetThickness())][3]
        tinyHoleCost = laserInfo.GetTinyHoleCount() * self._laserCostDict[str(metalSheet.GetThickness())][3]
        
        #雷射工資 = (切割長度工資 + 大孔工資 + 小孔工資) * 數量
        laserCost = (lineCost + largeHoleCost + tinyHoleCost) * self.tempProduct.GetCount()
        self.tempProduct.SetLaserCost(laserCost)

    def _computeDiscountAndTotal(self):
        discountedMetalSheetPrice = self.tempProduct.GetMetalSheetPrice() * self.tempProduct.GetMetalSheetDiscount()
        discountedLaserCost = self.tempProduct.GetLaserCost() * self.tempProduct.GetLaserDiscount()
        self.tempProduct.SetDiscountedMetalSheetPrice(discountedMetalSheetPrice)
        self.tempProduct.SetDiscountedLaserCost(discountedLaserCost)
        self.tempProduct.SetTotal(discountedMetalSheetPrice + discountedLaserCost)
    
    def GetProductList(self):
        return self._productList
    
    #更新材料單價
    def SetNewPriceToModel(self, blackIronProce, whiteIronPrice, aluminumPrice):
        self._materialInfoDict[0.00000785][0] = int(blackIronProce)
        self._materialInfoDict[0.00000793][0] = int(whiteIronPrice)
        self._materialInfoDict[0.00000271][0] = int(aluminumPrice)

    #model因輸入而變更後要重算相關資料
    def ComputeAll(self):
        for product in self._productList:
            self.tempProduct = product
            self._computeMetalSheetWeight()
            self._computePrice()
            self._computeDiscountAndTotal()

    def GetTotalPrice(self):
        self._totalPrice = 0
        for product in self._productList:
            self._totalPrice += product.GetTotal()
            
        return self._totalPrice
    
    def SetClientsInfo(self, client, contactInfo, address, serialNumber):
        self._client = []
        self._client.append(client)
        self._client.append(contactInfo)
        self._client.append(address)
        self._orderID = serialNumber

    def UpdateDB(self):
        self._dbConnector.CreateClient(self._client)
        self._dbConnector.CreateOrder(self._orderID, self._client[0])