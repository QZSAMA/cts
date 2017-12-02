""" Message Manager """

from PyQt5.QtWidgets import QTabWidget
from PyQt5 import QtCore, QtGui, QtWidgets

class Messages(QTabWidget):
    def __init__(self, parent=None):
        super(Messages, self).__init__(parent)

        self.setupUi(self)

    def setupUi(self, QTabWidget):
        QTabWidget.setObjectName("QTabWidget")
        QTabWidget.resize(913, 662)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignTop)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        QTabWidget.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab1)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableWidget_2)
        QTabWidget.addTab(self.tab1, "")

        self.retranslateUi(QTabWidget)
        QTabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(QTabWidget)

    def retranslateUi(self, QTabWidget):
        _translate = QtCore.QCoreApplication.translate
        QTabWidget.setWindowTitle(_translate("QTabWidget", "QTabWidget"))
        self.pushButton.setText(_translate("QTabWidget", "Search"))
        self.pushButton_2.setText(_translate("QTabWidget", "Refresh"))
        self.pushButton_4.setText(_translate("QTabWidget", "New Email"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("QTabWidget", "Sender"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("QTabWidget", "Time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("QTabWidget", "Content"))
        QTabWidget.setTabText(QTabWidget.indexOf(self.tab), _translate("QTabWidget", "Inbox"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("QTabWidget", "Receiver"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("QTabWidget", "Time"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("QTabWidget", "Content"))
        QTabWidget.setTabText(QTabWidget.indexOf(self.tab1), _translate("QTabWidget", "Sent Items"))