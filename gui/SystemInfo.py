""" panel for system information """

from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets


class SystemInfo(QTabWidget):
    def __init__(self, parent=None):
        super(SystemInfo, self).__init__(parent)

        self.unknownUser = "../img/unknown-user.png"
        # self.lcdNumber (developer numbers)
        # self.lcdNumber_2 (client numbers)

        #

        self.setupUi(self)

    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(460, 335)
        TabWidget.setMinimumSize(QtCore.QSize(460, 335))
        TabWidget.setTabBarAutoHide(False)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget_3)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_2.addWidget(self.lcdNumber)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.widget_2)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout_3.addWidget(self.lcdNumber_2)
        self.verticalLayout.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.widget)
        TabWidget.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.tab1)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget_5)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.widget_6)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.widget_6)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.verticalLayout_3.addWidget(self.widget_6)
        self.verticalLayout_2.addWidget(self.widget_4)
        TabWidget.addTab(self.tab1, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        self.label.setText(_translate("TabWidget", "Developer Numbers:"))
        self.label_2.setText(_translate("TabWidget", "Client Numbers:"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "User Number"))
        self.label_3.setText(_translate("TabWidget", "Client with most projects:"))
        self.label_5.setText(_translate("TabWidget", "TextLabel"))
        self.label_5.setScaledContents(True)
        self.label_5.setFixedSize(60, 60)
        self.label_6.setText(_translate("TabWidget", "TextLabel"))
        self.label_4.setText(_translate("TabWidget", "Developer with most income"))
        self.label_8.setText(_translate("TabWidget", "TextLabel"))
        self.label_8.setScaledContents(True)
        self.label_8.setFixedSize(60, 60)
        self.label_7.setText(_translate("TabWidget", "TextLabel"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "User Rank"))

    def setTop(self, top_client_id, top_dev_id):
        """ set pic to the path image"""
        # set client
        pixmap = QPixmap("../resources/pictures/" + top_client_id)
        # when path not found
        if (pixmap.isNull()):
            pixmap = QPixmap(self.unknownUser)
        # scaled and set
        pixmap.scaled(60, 60, Qt.KeepAspectRatio)
        self.label_5.setPixmap(pixmap)
        self.label_6.setText(top_client_id)
        # set dev
        pixmap = QPixmap("../resources/pictures/" + top_dev_id)
        # when path not found
        if (pixmap.isNull()):
            pixmap = QPixmap(self.unknownUser)
        # scaled and set
        pixmap.scaled(60, 60, Qt.KeepAspectRatio)
        self.label_8.setPixmap(pixmap)
        self.label_7.setText(top_dev_id)
