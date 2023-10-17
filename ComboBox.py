from PyQt5 import QtWidgets   

class ComboBox(QtWidgets.QComboBox):
        
    def __init__(self):
        super(ComboBox, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.addItems(['黑鐵','白鐵','鋁'])
        self.setCurrentIndex(0)
        self.setStyleSheet("background-color: white;")

