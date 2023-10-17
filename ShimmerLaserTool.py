from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QFont
from PIL import ImageGrab
from ComboBox import ComboBox
from Product import Product
from Model import Model
import re
import UI
import atexit

_model = Model()
_font = QFont()
_font.setFamily("Microsoft JhengHei")
_font.setPointSize(10)

def Init():
    header = ui._table.horizontalHeader()
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
    for i in range(8, 11):
        header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

def EventRegister():
    ui._plusButton.clicked.connect(PlusButtonClicked)
    ui._minusButton.clicked.connect(MinusButtonClicked)
    ui._computeButton.clicked.connect(ComputeButtonClick)
    ui._screenshotButton.clicked.connect(ScreenshotClicked)
    ui._blackIronPriceTextEdit.textChanged.connect(IntValidator)
    ui._whiteIronPriceTextEdit.textChanged.connect(IntValidator)
    ui._aluminumPriceTextEdit.textChanged.connect(IntValidator)
    ui._blackIronPriceTextEdit.textChanged.connect(PriceUpdate)
    ui._whiteIronPriceTextEdit.textChanged.connect(PriceUpdate)
    ui._aluminumPriceTextEdit.textChanged.connect(PriceUpdate)
    atexit.register(exit_handler)

def PlusButtonClicked():
    ui._table.setRowCount(ui._table.rowCount() + 1)
    
    product = Product()
    _model.AddProduct(product)

    SetItemToTable("請輸入件號/品名規格", ui._table.rowCount() - 1, 0)

    #新增combo box
    combobox = ComboBox()
    combobox.currentIndexChanged.connect(ComboBoxIndexChanged)
    ui._table.setCellWidget(ui._table.rowCount() - 1, 2, combobox)

    #initialize 1~12格
    for i in range(1, 13):
        SetItemToTable(0, ui._table.rowCount() - 1, i)
    
def SetItemToTable(content, i, j):
    item = QtWidgets.QTableWidgetItem()
    
    if is_int(str(content)):
        item.setText(format(int(content), ","))
    elif is_float(str(content)):
        item.setText(format(float(content), ","))
    else:
        item.setText(str(content))

    item.setFont(_font)
    ui._table.setItem(i, j, item)

def ComboBoxIndexChanged(index):
    if index == 0:
        _model.GetProductList()[ui._table.currentRow()].SetType(0)
    elif index == 1:
        _model.GetProductList()[ui._table.currentRow()].SetType(1)
    elif index == 2:
        _model.GetProductList()[ui._table.currentRow()].SetType(2)
    PriceUpdate()

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def MinusButtonClicked():
    if ui._table.rowCount() == 0 or ui._table.rowCount() == -1:
        return
    if ui._table.currentRow() != -1:
        del _model.GetProductList()[ui._table.currentRow()]
        ui._table.removeRow(ui._table.currentRow())

def ComputeButtonClick():
    if ui._table.rowCount() == 0:
        return
    try:
        for i in range(ui._table.rowCount()):
            product = _model.GetProductList()[i]
            product.SetName(ui._table.item(i, 0).text())
            product.SetCount(int(ui._table.item(i, 1).text()))
            product.GetMetalSheet().SetArea(float(ui._table.item(i, 3).text()))
            product.GetMetalSheet().SetThickness(int(ui._table.item(i, 4).text()))
            product.GetLaserInfo().SetThickness(int(ui._table.item(i, 4).text()))
            product.GetMetalSheet().SetUnitPrice(int(ui._table.item(i, 6).text()))
            product.GetLaserInfo().SetLength(float(ui._table.item(i, 8).text()))
            product.GetLaserInfo().SetLargeHoleCount(int(ui._table.item(i, 9).text()))
            product.GetLaserInfo().SetTinyHoleCount(int(ui._table.item(i, 10).text()))
        UpdateView()
    except ValueError:
        print("illgeal setting")
        ui._table.item(i, 0).setText("這筆訂單輸入格式有誤!!!!!" + product.GetName())

    

def UpdateView():
    if ui._table.rowCount() == 0:
        return

    try:
        for i in range(ui._table.rowCount()):
            product = _model.GetProductList()[i]
            ui._table.item(i, 5).setText(str(round(product.GetMetalSheet().GetWeight(), 6)))
            ui._table.item(i, 7).setText(str(round(product.GetMetalSheet().GetPrice(), 6)))
            ui._table.item(i, 11).setText(str(round(product.GetLaserInfo().GetPrice(), 6)))
            ui._table.item(i, 12).setText(str(round(product.GetPrice(), 6)))
        ui._total.setText(format(round(_model.GetTotalPrice(), 0), ","))
    except KeyError as ke:
        print("Wrong thickness! It should not be ", ke)
        ui._table.item(i, 0).setText("不支援此厚度!!!!!" + product.GetName())
    

def ScreenshotClicked():
    qrect = Widget.pos()
    img = ImageGrab.grab(bbox=(qrect.x() + 150, qrect.y() + 50, qrect.x() + Widget.width(), qrect.y() + Widget.height()))

    options = QFileDialog.Options()
    options != QFileDialog.ReadOnly

    fileName, _ = QFileDialog.getSaveFileName(Widget, "Save Screenshot", "", "Images (*.png *.jpg *.bmp);;All Files (*)")

    if fileName:
            img.save(fileName)
            print(f'Saved screenshot as {fileName}')

def IntValidator():    
    #限制價格只能輸入整數
    QtextShouldNotBeNonnumbericNeitherStartWithZero(ui._blackIronPriceTextEdit)
    QtextShouldNotBeNonnumbericNeitherStartWithZero(ui._whiteIronPriceTextEdit)
    QtextShouldNotBeNonnumbericNeitherStartWithZero(ui._aluminumPriceTextEdit)

def QtextShouldNotBeNonnumbericNeitherStartWithZero(qtext):
    #remove first word if is 0
    if qtext.toPlainText() == "":
        qtext.setText("0")
        qtext.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    if qtext.toPlainText().isdigit() == False:
        qtext.setText(re.sub("[^0-9]", "", qtext.toPlainText()))
        qtext.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    if qtext.toPlainText() != "0":
        if qtext.toPlainText()[0] == "0":
            qtext.setText(qtext.toPlainText()[1:])
            qtext.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

def PriceUpdate():
    #更新所有商品的單價
    for i in range(ui._table.rowCount()):
        if _model.GetProductList()[i].GetType() == 0: #黑鐵
            ui._table.item(i, 6).setText(ui._blackIronPriceTextEdit.toPlainText())
        elif _model.GetProductList()[i].GetType() == 1: #白鐵
            ui._table.item(i, 6).setText(ui._whiteIronPriceTextEdit.toPlainText())
        elif _model.GetProductList()[i].GetType() == 2: #鋁
            ui._table.item(i, 6).setText(ui._aluminumPriceTextEdit.toPlainText())
        else:
            print("ComboBox index error")

def exit_handler():
    _model.SetClientsInfo(ui._clientName.text(), ui._phone.text(), ui._address.text(), ui._serialNumber.text())
    _model.UpdateDB()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = UI.Ui__form()
    ui.setupUi(Widget)

    Init()
    EventRegister()

    Widget.show()
    
    sys.exit(app.exec_())

