# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/son_link/proyectos/mpp/mpp/ui/config.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_configDialog(object):
    def setupUi(self, configDialog):
        configDialog.setObjectName("configDialog")
        configDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        configDialog.resize(420, 240)
        configDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        configDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(configDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cbUpdateInit = QtWidgets.QCheckBox(configDialog)
        self.cbUpdateInit.setObjectName("cbUpdateInit")
        self.gridLayout_2.addWidget(self.cbUpdateInit, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(configDialog)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        self.selDownFolder = QtWidgets.QPushButton(configDialog)
        self.selDownFolder.setObjectName("selDownFolder")
        self.gridLayout_2.addWidget(self.selDownFolder, 2, 2, 1, 1)
        self.themeSelector = QtWidgets.QComboBox(configDialog)
        self.themeSelector.setObjectName("themeSelector")
        self.gridLayout_2.addWidget(self.themeSelector, 3, 2, 1, 1)
        self.downFolderEdit = QtWidgets.QLineEdit(configDialog)
        self.downFolderEdit.setObjectName("downFolderEdit")
        self.gridLayout_2.addWidget(self.downFolderEdit, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(configDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(configDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(configDialog)
        self.buttonBox.accepted.connect(configDialog.accept)
        self.buttonBox.rejected.connect(configDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(configDialog)

    def retranslateUi(self, configDialog):
        _translate = QtCore.QCoreApplication.translate
        configDialog.setWindowTitle(_translate("configDialog", "Configure"))
        self.cbUpdateInit.setText(_translate("configDialog", "Update at init."))
        self.label.setText(_translate("configDialog", "Download folder:"))
        self.selDownFolder.setText(_translate("configDialog", "Select"))
        self.label_2.setText(_translate("configDialog", "Theme:"))
