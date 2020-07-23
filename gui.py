# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1075, 722)
        self.about = QAction(MainWindow)
        self.about.setObjectName(u"about")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.c1 = QDoubleSpinBox(self.groupBox)
        self.c1.setObjectName(u"c1")
        self.c1.setMinimum(-1000.000000000000000)
        self.c1.setMaximum(1000.000000000000000)
        self.c1.setValue(1.000000000000000)

        self.horizontalLayout_2.addWidget(self.c1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.c2 = QDoubleSpinBox(self.groupBox)
        self.c2.setObjectName(u"c2")
        self.c2.setMinimum(-1000.000000000000000)
        self.c2.setMaximum(1000.000000000000000)
        self.c2.setValue(1.000000000000000)

        self.horizontalLayout_2.addWidget(self.c2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.m1 = QDoubleSpinBox(self.groupBox)
        self.m1.setObjectName(u"m1")
        self.m1.setMinimum(-1000.000000000000000)
        self.m1.setMaximum(1000.000000000000000)
        self.m1.setValue(100.000000000000000)

        self.horizontalLayout_3.addWidget(self.m1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.m2 = QDoubleSpinBox(self.groupBox)
        self.m2.setObjectName(u"m2")
        self.m2.setMinimum(-1000.000000000000000)
        self.m2.setMaximum(1000.000000000000000)
        self.m2.setValue(100.000000000000000)

        self.horizontalLayout_3.addWidget(self.m2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)

        self.verticalLayout.addWidget(self.label_7)

        self.table = QTableWidget(self.groupBox)
        if (self.table.columnCount() < 3):
            self.table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.table.rowCount() < 2):
            self.table.setRowCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table.setItem(1, 2, __qtablewidgetitem10)
        self.table.setObjectName(u"table")
        self.table.horizontalHeader().setDefaultSectionSize(80)

        self.verticalLayout.addWidget(self.table)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.solve = QPushButton(self.groupBox)
        self.solve.setObjectName(u"solve")
        self.solve.setMinimumSize(QSize(0, 36))

        self.horizontalLayout_4.addWidget(self.solve)

        self.add = QPushButton(self.groupBox)
        self.add.setObjectName(u"add")
        self.add.setMinimumSize(QSize(0, 36))

        self.horizontalLayout_4.addWidget(self.add)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.groupBox_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.print = QPlainTextEdit(self.groupBox_2)
        self.print.setObjectName(u"print")
        font1 = QFont()
        font1.setFamily(u"\u9ed1\u4f53")
        font1.setPointSize(13)
        self.print.setFont(font1)

        self.verticalLayout_2.addWidget(self.print)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.plot = PlotWidget(self.centralwidget)
        self.plot.setObjectName(u"plot")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(5)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.plot)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1075, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.about)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7ebf\u6027\u89c4\u5212", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.groupBox_3.setTitle("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u5165", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u51fd\u6570\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"X+", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7ea6\u675f\u6761\u4ef6\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"m1\uff1a", None))
#if QT_CONFIG(statustip)
        self.m1.setStatusTip(QCoreApplication.translate("MainWindow", u"X\u7684\u53d6\u503c\u8303\u56f4", None))
#endif // QT_CONFIG(statustip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"m2\uff1a", None))
#if QT_CONFIG(statustip)
        self.m2.setStatusTip(QCoreApplication.translate("MainWindow", u"Y\u7684\u53d6\u503c\u8303\u56f4", None))
#endif // QT_CONFIG(statustip)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u534a\u5e73\u9762\uff1aaX + bY <= c", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"c", None));
        ___qtablewidgetitem3 = self.table.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem4 = self.table.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"2", None));

        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.table.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem6 = self.table.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"-1", None));
        ___qtablewidgetitem7 = self.table.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem8 = self.table.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem9 = self.table.item(1, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem10 = self.table.item(1, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"10", None));
        self.table.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(statustip)
        self.table.setStatusTip(QCoreApplication.translate("MainWindow", u"\u7ea6\u675f\u6761\u4ef6", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.solve.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6839\u636e\u4e0a\u8868\u4e00\u6b21\u6027\u6c42\u89e3", None))
#endif // QT_CONFIG(statustip)
        self.solve.setText(QCoreApplication.translate("MainWindow", u"\u6c42\u89e3", None))
#if QT_CONFIG(statustip)
        self.add.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u7ea6\u675f\u9012\u589e\u5f0f\u6c42\u89e3", None))
#endif // QT_CONFIG(statustip)
        self.add.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u7ea6\u675f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa", None))
#if QT_CONFIG(statustip)
        self.print.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.plot.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5de6\u952e\u79fb\u52a8 \u4e2d\u952e\u7f29\u653e", None))
#endif // QT_CONFIG(statustip)
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

