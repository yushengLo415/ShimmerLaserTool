
class LaserInfo:
    
    def __init__(self, length, largeHoleCount, tinyHoleCount):
        self._length = float(length)
        self._largeHoleCount = int(largeHoleCount)
        self._tinyHoleCount = int(tinyHoleCount)

    def GetLength(self):
        return self._length
    
    def GetLargeHoleCount(self):
        return self._largeHoleCount
    
    def GetTinyHoleCount(self):
        return self._tinyHoleCount
    
    def SetLength(self, length):
        self._length = length
    
    def SetLargeHoleCount(self, largeHoleCount):
        self._largeHoleCount = largeHoleCount
    
    def SetTinyHoleCount(self, tinyHoleCount):
        self._tinyHoleCount = tinyHoleCount