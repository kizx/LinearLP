# -*- coding: utf-8 -*-
import numpy as np
import pyqtgraph as pg
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

        self.ui.solve.clicked.connect(self.solve)

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
        self.ui.print.appendPlainText('目标点：({:.3f},{:.3f})\n'
                                      '函数值：[{:.3f}]\n'
                                      '------------------------'.format(self.p[0], self.p[1], ans))
        self.plot()

    def addline(self):
        line = [addDialog.ui.a.value(), addDialog.ui.b.value(), addDialog.ui.c.value()]
        row = self.ui.table.rowCount()
        self.ui.table.insertRow(row)
        for i in range(3):
            item = QTableWidgetItem()
            item.setText(f'{line[i]}')
            self.ui.table.setItem(row, i, item)
        addDialog.close()
        self.p, ans = self.LP.add(line)
        self.ui.print.appendPlainText('目标点：({:.3f},{:.3f})\n'
                                      '函数值：[{:.3f}]\n'
                                      '------------------------'.format(self.p[0], self.p[1], ans))

        self.plot()

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
            x = np.array([-self._limits[0], self._limits[0]])
            y = (i[2] - i[0] * x) / i[1]
            if i[1] > 0:
                self.ui.plot.plot(x, y, pen=pg.mkPen('k'), fillLevel=-self._limits[1],
                                  brush=(50, 50, 200, 100))  # 画半平面直线
            elif i[1] < 0:
                self.ui.plot.plot(x, y, pen=pg.mkPen('k'), fillLevel=self._limits[1],
                                  brush=(50, 50, 200, 100))  # 画半平面直线
        self.ui.plot.plot([self.p[0]], [self.p[1]], pen=None, symbolBrush=(255, 0, 0), symbolPen='w')  # 标出目标点


class childWindow(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication()
    window = Window()
    addDialog = childWindow()
    addDialog.ui.buttonBox.accepted.connect(window.addline)
    window.ui.add.clicked.connect(addDialog.show)
    window.show()
    app.exec_()
