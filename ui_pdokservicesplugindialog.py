# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pdokservicesplugindialog.ui'
#
# Created: Fri Mar 14 13:05:31 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PdokServicesPlugin(object):
    def setupUi(self, PdokServicesPlugin):
        PdokServicesPlugin.setObjectName(_fromUtf8("PdokServicesPlugin"))
        PdokServicesPlugin.resize(1016, 728)
        self.gridLayout = QtGui.QGridLayout(PdokServicesPlugin)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(PdokServicesPlugin)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(PdokServicesPlugin)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.servicesView = QtGui.QTableView(self.tab_2)
        self.servicesView.setMinimumSize(QtCore.QSize(0, 0))
        self.servicesView.setObjectName(_fromUtf8("servicesView"))
        self.gridLayout_2.addWidget(self.servicesView, 1, 0, 1, 2)
        self.layerInfo = QtGui.QTextEdit(self.tab_2)
        self.layerInfo.setMaximumSize(QtCore.QSize(16777215, 200))
        self.layerInfo.setObjectName(_fromUtf8("layerInfo"))
        self.gridLayout_2.addWidget(self.layerInfo, 2, 0, 1, 2)
        self.layerSearch = QtGui.QLineEdit(self.tab_2)
        self.layerSearch.setObjectName(_fromUtf8("layerSearch"))
        self.gridLayout_2.addWidget(self.layerSearch, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.btnLoadLayer = QtGui.QPushButton(self.tab_2)
        self.btnLoadLayer.setEnabled(False)
        self.btnLoadLayer.setObjectName(_fromUtf8("btnLoadLayer"))
        self.gridLayout_2.addWidget(self.btnLoadLayer, 4, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.geocoderSearch = QtGui.QLineEdit(self.tab_3)
        self.geocoderSearch.setObjectName(_fromUtf8("geocoderSearch"))
        self.gridLayout_4.addWidget(self.geocoderSearch, 0, 0, 1, 2)
        self.geocoderSearchBtn = QtGui.QPushButton(self.tab_3)
        self.geocoderSearchBtn.setObjectName(_fromUtf8("geocoderSearchBtn"))
        self.gridLayout_4.addWidget(self.geocoderSearchBtn, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.geocoderResultSearch = QtGui.QLineEdit(self.tab_3)
        self.geocoderResultSearch.setObjectName(_fromUtf8("geocoderResultSearch"))
        self.gridLayout_4.addWidget(self.geocoderResultSearch, 1, 1, 1, 2)
        self.geocoderResultView = QtGui.QTableView(self.tab_3)
        self.geocoderResultView.setObjectName(_fromUtf8("geocoderResultView"))
        self.gridLayout_4.addWidget(self.geocoderResultView, 2, 0, 1, 3)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.webView = QtWebKit.QWebView(self.tab)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("qrc:/plugins/pdokservicesplugin/infotab.html")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout_3.addWidget(self.webView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(PdokServicesPlugin)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PdokServicesPlugin)

    def retranslateUi(self, PdokServicesPlugin):
        PdokServicesPlugin.setWindowTitle(_translate("PdokServicesPlugin", "PdokServicesPlugin", None))
        self.label.setText(_translate("PdokServicesPlugin", "Zoek in servicetitel, laagnaam en beschrijving:", None))
        self.btnLoadLayer.setText(_translate("PdokServicesPlugin", "Laad deze laag in QGIS (of dubbelklik op de regel)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("PdokServicesPlugin", "PDOK services", None))
        self.geocoderSearch.setText(_translate("PdokServicesPlugin", "postcode, adres of plaatsnaam", None))
        self.geocoderSearchBtn.setText(_translate("PdokServicesPlugin", "Zoek", None))
        self.label_2.setText(_translate("PdokServicesPlugin", "Filter resultaten op:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("PdokServicesPlugin", "PDOK geocoder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("PdokServicesPlugin", "OpenGeoGroep en PDOK", None))

from PyQt4 import QtWebKit
import resources_rc