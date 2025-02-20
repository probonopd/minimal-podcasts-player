# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/son_link/proyectos/mpp/mpp/ui/gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("Minimal Podcasts Player")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.playerLayout = QtWidgets.QHBoxLayout()
        self.playerLayout.setContentsMargins(6, -1, 6, -1)
        self.playerLayout.setSpacing(0)
        self.playerLayout.setObjectName("playerLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.curPCLabel = QtWidgets.QLabel(self.centralwidget)
        self.curPCLabel.setObjectName("curPCLabel")
        self.verticalLayout_3.addWidget(self.curPCLabel)
        self.curTrackName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.curTrackName.setFont(font)
        self.curTrackName.setWordWrap(True)
        self.curTrackName.setObjectName("curTrackName")
        self.verticalLayout_3.addWidget(self.curTrackName)
        self.playerLayout.addLayout(self.verticalLayout_3)
        self.queuePrevBtn = QtWidgets.QPushButton(self.centralwidget)
        self.queuePrevBtn.setEnabled(False)
        self.queuePrevBtn.setText("")
        icon = QtGui.QIcon.fromTheme("media-skip-backward")
        self.queuePrevBtn.setIcon(icon)
        self.queuePrevBtn.setFlat(True)
        self.queuePrevBtn.setObjectName("queuePrevBtn")
        self.playerLayout.addWidget(self.queuePrevBtn)
        self.back10Btn = QtWidgets.QPushButton(self.centralwidget)
        self.back10Btn.setText("")
        icon = QtGui.QIcon.fromTheme("media-seek-backward")
        self.back10Btn.setIcon(icon)
        self.back10Btn.setFlat(True)
        self.back10Btn.setObjectName("back10Btn")
        self.playerLayout.addWidget(self.back10Btn)
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setText("0:00:00")
        self.timeLabel.setObjectName("timeLabel")
        self.playerLayout.addWidget(self.timeLabel)
        self.timeSlider = QtWidgets.QSlider(self.centralwidget)
        self.timeSlider.setMaximum(100)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.playerLayout.addWidget(self.timeSlider)
        self.totalTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalTimeLabel.setText("0:00:00")
        self.totalTimeLabel.setObjectName("totalTimeLabel")
        self.playerLayout.addWidget(self.totalTimeLabel)
        self.playBtn = QtWidgets.QPushButton(self.centralwidget)
        self.playBtn.setStyleSheet("")
        self.playBtn.setText("")
        icon = QtGui.QIcon.fromTheme("media-playback-start")
        self.playBtn.setIcon(icon)
        self.playBtn.setFlat(True)
        self.playBtn.setObjectName("playBtn")
        self.playerLayout.addWidget(self.playBtn)
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setText("")
        icon = QtGui.QIcon.fromTheme("media-playback-stop")
        self.stopBtn.setIcon(icon)
        self.stopBtn.setFlat(True)
        self.stopBtn.setObjectName("stopBtn")
        self.playerLayout.addWidget(self.stopBtn)
        self.for10Btn = QtWidgets.QPushButton(self.centralwidget)
        self.for10Btn.setText("")
        icon = QtGui.QIcon.fromTheme("media-seek-forward")
        self.for10Btn.setIcon(icon)
        self.for10Btn.setFlat(True)
        self.for10Btn.setObjectName("for10Btn")
        self.playerLayout.addWidget(self.for10Btn)
        self.queueNextBtn = QtWidgets.QPushButton(self.centralwidget)
        self.queueNextBtn.setEnabled(False)
        self.queueNextBtn.setWhatsThis("")
        self.queueNextBtn.setText("")
        icon = QtGui.QIcon.fromTheme("media-skip-forward")
        self.queueNextBtn.setIcon(icon)
        self.queueNextBtn.setFlat(True)
        self.queueNextBtn.setObjectName("queueNextBtn")
        self.playerLayout.addWidget(self.queueNextBtn)
        self.optionsBtn = QtWidgets.QToolButton(self.centralwidget)
        icon = QtGui.QIcon.fromTheme("applications-system")
        self.optionsBtn.setIcon(icon)
        self.optionsBtn.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.optionsBtn.setAutoRaise(True)
        self.optionsBtn.setObjectName("optionsBtn")
        self.playerLayout.addWidget(self.optionsBtn)
        self.volumeBtn = QtWidgets.QToolButton(self.centralwidget)
        icon = QtGui.QIcon.fromTheme("audio-volume-high")
        self.volumeBtn.setIcon(icon)
        self.volumeBtn.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.volumeBtn.setAutoRaise(True)
        self.volumeBtn.setObjectName("volumeBtn")
        self.playerLayout.addWidget(self.volumeBtn)
        self.playerLayout.setStretch(0, 1)
        self.playerLayout.setStretch(4, 1)
        self.verticalLayout.addLayout(self.playerLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget_2 = QtWidgets.QWidget(self.splitter)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.podcastsList = QtWidgets.QListWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.podcastsList.sizePolicy().hasHeightForWidth())
        self.podcastsList.setSizePolicy(sizePolicy)
        self.podcastsList.setMinimumSize(QtCore.QSize(240, 0))
        self.podcastsList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.podcastsList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.podcastsList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.podcastsList.setObjectName("podcastsList")
        self.verticalLayout_2.addWidget(self.podcastsList)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.splitter)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setBaseSize(QtCore.QSize(92, 92))
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.podcastCover = QtWidgets.QLabel(self.widget_5)
        self.podcastCover.setMinimumSize(QtCore.QSize(128, 128))
        self.podcastCover.setText("")
        self.podcastCover.setPixmap(QtGui.QPixmap(":/img/no-cover.svg"))
        self.podcastCover.setScaledContents(False)
        self.podcastCover.setObjectName("podcastCover")
        self.horizontalLayout_2.addWidget(self.podcastCover)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.podcastTitle = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.podcastTitle.setFont(font)
        self.podcastTitle.setObjectName("podcastTitle")
        self.verticalLayout_4.addWidget(self.podcastTitle)
        self.podcastWeb = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.podcastWeb.setFont(font)
        self.podcastWeb.setOpenExternalLinks(True)
        self.podcastWeb.setObjectName("podcastWeb")
        self.verticalLayout_4.addWidget(self.podcastWeb)
        self.podcastDesc = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.podcastDesc.setFont(font)
        self.podcastDesc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.podcastDesc.setWordWrap(True)
        self.podcastDesc.setOpenExternalLinks(True)
        self.podcastDesc.setObjectName("podcastDesc")
        self.verticalLayout_4.addWidget(self.podcastDesc)
        self.verticalLayout_4.setStretch(2, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.setStretch(1, 1)
        self.gridLayout_8.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.widget_5, 0, 0, 1, 1)
        self.episodesTable = QtWidgets.QTableWidget(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.episodesTable.setFont(font)
        self.episodesTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.episodesTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.episodesTable.setProperty("showDropIndicator", False)
        self.episodesTable.setDragDropOverwriteMode(False)
        self.episodesTable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.episodesTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.episodesTable.setObjectName("episodesTable")
        self.episodesTable.setColumnCount(0)
        self.episodesTable.setRowCount(0)
        self.episodesTable.horizontalHeader().setVisible(True)
        self.episodesTable.verticalHeader().setVisible(False)
        self.gridLayout_6.addWidget(self.episodesTable, 1, 0, 1, 1)
        self.gridLayout_6.setRowStretch(1, 1)
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.tab_2)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.splitter_2 = QtWidgets.QSplitter(self.widget_4)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.queueList = QtWidgets.QListWidget(self.splitter_2)
        self.queueList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.queueList.setProperty("showDropIndicator", False)
        self.queueList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.queueList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.queueList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.queueList.setObjectName("queueList")
        self.infoEpisodeLabel = QtWidgets.QTextBrowser(self.splitter_2)
        self.infoEpisodeLabel.setObjectName("infoEpisodeLabel")
        self.gridLayout_7.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_4, 0, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setRowStretch(0, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.curPCLabel.setText(_translate("MainWindow", "Podcast"))
        self.curTrackName.setText(_translate("MainWindow", "Episode Title"))
        self.optionsBtn.setText(_translate("MainWindow", "..."))
        self.volumeBtn.setText(_translate("MainWindow", "..."))
        self.podcastTitle.setText(_translate("MainWindow", "Podcasts"))
        self.podcastWeb.setText(_translate("MainWindow", "Web"))
        self.podcastDesc.setText(_translate("MainWindow", "Description"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Queue"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Downloads"))
from . import images_rc
