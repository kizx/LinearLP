# -*- coding: utf-8 -*-
import numpy as np
import pyqtgraph as pg
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QTableWidgetItem

from core import LinearProgram
from gui import Ui_MainWindow
from inputgui import Ui_Dialog


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.hasLP = False
        self.ui.solve.clicked.connect(self.solve)
        self.ui.about.triggered.connect(self.about)

        # 设置上下左右的label
        self.ui.plot.setLabel("left", "Y")
        self.ui.plot.setLabel("bottom", "X")
        # 设置刻度范围
        self.ui.plot.setXRange(min=-100, max=100)
        self.ui.plot.setYRange(min=-100, max=100)
        # 显示表格线
        self.ui.plot.showGrid(x=True, y=True)
        # 背景色改为白色
        self.ui.plot.setBackground('w')
        # 抗锯齿
        pg.setConfigOptions(antialias=True)
        # 设置缩放最大范围
        self.ui.plot.setLimits(xMin=-1000, xMax=1000, yMin=-1000, yMax=1000)
        # 锁定缩放比（右键）
        self.ui.plot.setAspectLocked(lock=True, ratio=1)
        # 隐藏左下角缩放A
        self.ui.plot.hideButtons()

    def solve(self):
        self._fun = [self.ui.c1.value(), self.ui.c2.value()]
        self._limits = [self.ui.m1.value(), self.ui.m2.value()]
        self._lines = []
        for i in range(self.ui.table.rowCount()):
            line = [float(self.ui.table.item(i, 0).text()),
                    float(self.ui.table.item(i, 1).text()),
                    float(self.ui.table.item(i, 2).text())]
            self._lines.append(line)
        self.LP = LinearProgram(self._fun, self._limits, self._lines)
        self.p, ans = self.LP.main()
        self.hasLP = True
        if self.p is not None:
            self.ui.print.appendPlainText('目标点：({:.3f},{:.3f})\n'
                                          '函数值：[{:.3f}]\n'
                                          '---------------------------'.format(self.p[0], self.p[1], ans))
            self.plot()
        else:
            self.ui.print.appendPlainText('无解！\n'
                                          '---------------------------')
            QMessageBox.warning(self, '无解', '约束范围内无解！')

    def addline(self):
        line = [addDialog.ui.a.value(), addDialog.ui.b.value(), addDialog.ui.c.value()]
        row = self.ui.table.rowCount()
        self.ui.table.insertRow(row)
        for i in range(3):
            item = QTableWidgetItem()
            item.setText(f'{line[i]}')
            self.ui.table.setItem(row, i, item)
        addDialog.close()
        if self.hasLP is False:
            return
        else:
            self.p, ans = self.LP.add(line)
            if self.p is not None:
                self.ui.print.appendPlainText('目标点：({:.3f},{:.3f})\n'
                                              '函数值：[{:.3f}]\n'
                                              '---------------------------'.format(self.p[0], self.p[1], ans))
                self.plot()
            else:
                self.ui.print.appendPlainText('无解！\n'
                                              '---------------------------')
                QMessageBox.warning(self, '无解', '约束范围内无解！')

    def plot(self):
        x = [-self._limits[0], self._limits[0],
             self._limits[0], self._limits[0],
             self._limits[0], -self._limits[0],
             -self._limits[0], -self._limits[0]]
        y = [self._limits[1], self._limits[1],
             self._limits[1], -self._limits[1],
             -self._limits[1], -self._limits[1],
             -self._limits[1], self._limits[1]]
        self.ui.plot.plot(x, y, pen=(15, 164, 254), clear=True)  # 画范围限制框，顺便清空画布
        for i in self._lines:
            x = np.array([-1000, 1000])
            if i[1] == 0:
                x = [i[2] / i[0], i[2] / i[0]]
                print(x)
                y = [-1000, 1000]
                self.ui.plot.plot(x, y, pen=pg.mkPen('k'), fillLevel=-1000,
                                  brush=(50, 50, 200, 100))  # 画半平面直线
            else:
                y = (i[2] - i[0] * x) / i[1]
            if i[1] > 0:
                self.ui.plot.plot(x, y, pen=pg.mkPen('k'), fillLevel=-1000,
                                  brush=(50, 50, 200, 100))  # 画半平面直线
            elif i[1] < 0:
                self.ui.plot.plot(x, y, pen=pg.mkPen('k'), fillLevel=1000,
                                  brush=(50, 50, 200, 100))  # 画半平面直线
        self.ui.plot.plot([self.p[0]], [self.p[1]], pen=None, symbolBrush=(255, 0, 0), symbolPen='w')  # 标出目标点

    def about(self):
        html = """
<html><head><meta name="qrichtext" content="1" />
<style type="text/css">p, li { white-space: pre-wrap; }</style>
</head><body style=" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; color:#00aaff;">递增式线性规划</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#00aaff;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">学号：2019261331</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">姓名：张欣</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">编程语言：Python</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">界面基于Pyside2和pyqtgraph开发</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">                       --2020.07</p>
</body></html>
"""
        QMessageBox.about(self.ui.menubar, '关于', html)


class childWindow(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication()
    app.setWindowIcon(QIcon('logo.png'))
    window = Window()
    addDialog = childWindow()
    addDialog.ui.buttonBox.accepted.connect(window.addline)
    window.ui.add.clicked.connect(addDialog.show)
    window.show()
    app.exec_()
