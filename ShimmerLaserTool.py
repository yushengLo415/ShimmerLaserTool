from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QFont
from PIL import ImageGrab
from ComboBox import ComboBox
from MetalSheet import MetalSheet
from LaserInformation import LaserInfo
from Product import Product
from Model import Model
import re
import UI

_model = Model()
_font = QFont()
_font.setFamily("Microsoft JhengHei")
_font.setPointSize(10)

def Init():
    header = ui._table.horizontalHeader()
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
    for i in range(7, 16):
        header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

def EventRegister():
    ui._plusButton.clicked.connect(PlusButtonClicked)
    ui._minusButton.clicked.connect(MinusButtonClicked)
    ui._computeButton.clicked.connect(ComputeButtonClick)
    ui._screenshotButton.clicked.connect(ScreenshotClicked)
    ui._blackIronPriceTextEdit.textChanged.connect(PriceUpdate)
    ui._whiteIronPriceTextEdit.textChanged.connect(PriceUpdate)
    ui._aluminumPriceTextEdit.textChanged.connect(PriceUpdate)

def PlusButtonClicked():
    ui._table.setRowCount(ui._table.rowCount() + 1)
    metalSheet = MetalSheet("0.00000785", 0, 0)
    laserInformation = LaserInfo(0, 0, 0)
    product = Product("請輸入件號/品名規格", 0, metalSheet, 1, laserInformation, 1)
    _model.AddProduct(product)
    SetItemToTable(product.GetName(), ui._table.rowCount() - 1, 0)
    SetItemToTable(product.GetCount(), ui._table.rowCount() - 1, 1)
    SetItemToTable(product.GetMetalSheet().GetArea(), ui._table.rowCount() - 1, 3)
    SetItemToTable(product.GetMetalSheet().GetThickness(), ui._table.rowCount() - 1, 4)
    SetItemToTable(product.GetMetalSheet().GetWeight(), ui._table.rowCount() - 1, 5)
    SetItemToTable(ui._blackIronPriceTextEdit.toPlainText(), ui._table.rowCount() - 1, 6)
    SetItemToTable(product.GetMetalSheetPrice(), ui._table.rowCount() - 1, 7)
    SetItemToTable(product.GetMetalSheetDiscount(), ui._table.rowCount() - 1, 8)
    SetItemToTable(product.GetDiscountedMetalSheetPrice(), ui._table.rowCount() - 1, 9)
    SetItemToTable(product.GetLaserInfo().GetLength(), ui._table.rowCount() - 1, 10)
    SetItemToTable(product.GetLaserInfo().GetLargeHoleCount(), ui._table.rowCount() - 1, 11)
    SetItemToTable(product.GetLaserInfo().GetTinyHoleCount(), ui._table.rowCount() - 1, 12)
    SetItemToTable(product.GetLaserCost(), ui._table.rowCount() - 1, 13)
    SetItemToTable(product.GetLaserDiscount(), ui._table.rowCount() - 1, 14)
    SetItemToTable(product.GetDiscountedLaserCost(), ui._table.rowCount() - 1, 15)
    SetItemToTable(product.GetTotal(), ui._table.rowCount() - 1, 16)

    #new a combo box
    combobox = ComboBox()
    combobox.initUI()
    combobox.currentIndexChanged.connect(ComboBoxIndexChanged)
    ui._table.setCellWidget(ui._table.rowCount() - 1, 2, combobox)

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
        _model.GetProductList()[ui._table.currentRow()].GetMetalSheet().SetDensity(0.00000785)
    elif index == 1:
        _model.GetProductList()[ui._table.currentRow()].GetMetalSheet().SetDensity(0.00000793)
    elif index == 2:
        _model.GetProductList()[ui._table.currentRow()].GetMetalSheet().SetDensity(0.00000271)     

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
            product.SetMetalSheetDiscount(float(ui._table.item(i, 8).text()))
            product.GetLaserInfo().SetLength(float(ui._table.item(i, 10).text()))
            product.GetLaserInfo().SetLargeHoleCount(int(ui._table.item(i, 11).text()))
            product.GetLaserInfo().SetTinyHoleCount(int(ui._table.item(i, 12).text()))
            product.SetLaserDiscount(float(ui._table.item(i, 14).text()))
    except ValueError:
        print("illgeal setting")

    _model.ComputeAll()
    UpdateView()

def UpdateView():
    if ui._table.rowCount() == 0:
        return

    for i in range(ui._table.rowCount()):
        product = _model.GetProductList()[i]
        metalSheet = product.GetMetalSheet()
        laserInfo = product.GetLaserInfo()

        ui._table.item(i, 1).setText(str(product.GetCount()))
        ui._table.item(i, 3).setText(str(metalSheet.GetArea()))

        ui._table.item(i, 4).setText(str(metalSheet.GetThickness()))
        ui._table.item(i, 5).setText(str(round(metalSheet.GetWeight(), 6)))

        #以密度決定單價
        if metalSheet.GetDensity() == 0.00000785:
            ui._table.item(i, 6).setText(ui._blackIronPriceTextEdit.toPlainText())
        elif metalSheet.GetDensity() == 0.00000793:
            ui._table.item(i, 6).setText(ui._whiteIronPriceTextEdit.toPlainText())
        else:
            ui._table.item(i, 6).setText(ui._aluminumPriceTextEdit.toPlainText())
            
        ui._table.item(i, 7).setText(str(round(product.GetMetalSheetPrice(), 6)))
        ui._table.item(i, 8).setText(str(round(product.GetMetalSheetDiscount(), 6)))
        ui._table.item(i, 9).setText(str(round(product.GetDiscountedMetalSheetPrice(), 6)))
        ui._table.item(i, 10).setText(str(round(laserInfo.GetLength(), 6)))
        ui._table.item(i, 11).setText(str(laserInfo.GetLargeHoleCount()))
        ui._table.item(i, 12).setText(str(laserInfo.GetTinyHoleCount()))
        ui._table.item(i, 13).setText(str(round(product.GetLaserCost(), 6)))
        ui._table.item(i, 14).setText(str(round(product.GetLaserDiscount(), 6)))
        ui._table.item(i, 15).setText(str(round(product.GetDiscountedLaserCost(), 6)))
        ui._table.item(i, 16).setText(str(round(product.GetTotal(), 6)))

        ui._total.setText(format(round(_model.GetTotalPrice(), 0), ","))


def ScreenshotClicked():
    qrect = Widget.pos()
    img = ImageGrab.grab(bbox=(qrect.x() + 150, qrect.y() + 50, qrect.x() + Widget.width(), qrect.y() + Widget.height()))

    options = QFileDialog.Options()
    options != QFileDialog.ReadOnly

    fileName, _ = QFileDialog.getSaveFileName(Widget, "Save Screenshot", "", "Images (*.png *.jpg *.bmp);;All Files (*)")

    if fileName:
            img.save(fileName)
            print(f'Saved screenshot as {fileName}')

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
    QtextShouldNotBeNonnumbericNeitherStartWithZero(ui._blackIronPriceTextEdit)
    QtextShouldNotBeNonnumbericNeitherStartWithZero(ui._whiteIronPriceTextEdit)
    QtextShouldNotBeNonnumbericNeitherStartWithZero(ui._aluminumPriceTextEdit)
    _model.SetNewPriceToModel(ui._blackIronPriceTextEdit.toPlainText(), ui._whiteIronPriceTextEdit.toPlainText(), ui._aluminumPriceTextEdit.toPlainText())

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

