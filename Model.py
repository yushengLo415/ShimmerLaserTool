from mysqlConnector import mysqlConnector

class Model:

    _productList = []
    _blackIronPrice = 0
    _whiteIronPrice = 0
    _aluminumPrice = 0
    _totalPrice = 0
    _dbConnector = mysqlConnector()

    def __init__(self):
        pass

    def AddProduct(self, product):
        self.tempProduct = product
        self._productList.append(self.tempProduct)
    
    def GetProductList(self):
        return self._productList

    def GetTotalPrice(self):
        self._totalPrice = 0
        for product in self._productList:
            self._totalPrice += product.GetPrice()
        return self._totalPrice
        
    def SetClientsInfo(self, client, contactInfo, address, serialNumber):
        self._client = []
        self._client.append(client)
        self._client.append(contactInfo)
        self._client.append(address)
        self._orderID = serialNumber

    def UpdateDB(self):
        self._dbConnector.CreateClient(self._client)
        self._dbConnector.CreateOrder(self._orderID)
        self._dbConnector.CreateProducts(self._productList)

        self._dbConnector.Disconnect()