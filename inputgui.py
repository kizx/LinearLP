# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inputgui.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(302, 95)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.a = QDoubleSpinBox(Dialog)
        self.a.setObjectName(u"a")
        self.a.setMinimum(-1000.000000000000000)
        self.a.setMaximum(1000.000000000000000)
        self.a.setValue(1.000000000000000)

        self.horizontalLayout.addWidget(self.a)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.b = QDoubleSpinBox(Dialog)
        self.b.setObjectName(u"b")
        self.b.setMinimum(-1000.000000000000000)
        self.b.setMaximum(1000.000000000000000)
        self.b.setValue(1.000000000000000)

        self.horizontalLayout.addWidget(self.b)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.c = QDoubleSpinBox(Dialog)
        self.c.setObjectName(u"c")
        self.c.setMinimum(-1000.000000000000000)
        self.c.setMaximum(1000.000000000000000)
        self.c.setValue(0.000000000000000)

        self.horizontalLayout.addWidget(self.c)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u7ea6\u675f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"X+", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Y<=", None))
    # retranslateUi

