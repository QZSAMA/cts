from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets

class History(QWidget):
    def __init__(self, parent=None):
        super(History, self).__init__(parent)

        self.setupUi(self)

    def setupUi(self, QWidget):
        QWidget.setObjectName("QWidget")
        QWidget.resize(1018, 692)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(QWidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(QWidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.tableWidget_2)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.groupBox_4 = QtWidgets.QGroupBox(QWidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.groupBox_5)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        self.verticalLayout_3.addWidget(self.tableWidget_3)
        self.horizontalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.groupBox_6)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(4)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        self.verticalLayout_4.addWidget(self.tableWidget_4)
        self.horizontalLayout_2.addWidget(self.groupBox_6)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        self.groupBox_7 = QtWidgets.QGroupBox(QWidget)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.groupBox_7)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(5)
        self.tableWidget_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        self.verticalLayout_5.addWidget(self.tableWidget_5)
        self.verticalLayout_6.addWidget(self.groupBox_7)

        self.tableWidget.setSortingEnabled(True)
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget_3.setSortingEnabled(True)
        self.tableWidget_4.setSortingEnabled(True)
        self.tableWidget_5.setSortingEnabled(True)

        self.retranslateUi(QWidget)
        QtCore.QMetaObject.connectSlotsByName(QWidget)

    def retranslateUi(self, QWidget):
        _translate = QtCore.QCoreApplication.translate
        QWidget.setWindowTitle(_translate("QWidget", "QWidget"))
        self.groupBox.setTitle(_translate("QWidget", "Transaction History"))
        self.groupBox_2.setTitle(_translate("QWidget", "Send"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("QWidget", "Amount"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("QWidget", "Data"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("QWidget", "Receiver"))
        self.groupBox_3.setTitle(_translate("QWidget", "Receive"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("QWidget", "Amount"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("QWidget", "Data"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("QWidget", "Sender"))
        self.groupBox_4.setTitle(_translate("QWidget", "Project Reviews"))
        self.groupBox_5.setTitle(_translate("QWidget", "Send"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("QWidget", "Project ID"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("QWidget", "Receiver"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("QWidget", "Review"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("QWidget", "Rating"))
        self.groupBox_6.setTitle(_translate("QWidget", "Receive"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("QWidget", "Project ID"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("QWidget", "Sender"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("QWidget", "Review"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("QWidget", "Rating"))
        self.groupBox_7.setTitle(_translate("QWidget", "Project History"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("QWidget", "Project ID"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("QWidget", "Client"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("QWidget", "Developer"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("QWidget", "Detail"))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("QWidget", "Price"))