# -*- coding: utf-8 -*-
from PySide2.QtWidgets import *

from gui import Ui_MainWindow
import pyqtgraph as pg


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.plot()

    def plot(self):
        self.ui.plot.setTitle("线性规划", color='008080', size='12pt')

        # 设置上下左右的label
        self.ui.plot.setLabel("left", "Y")
        self.ui.plot.setLabel("bottom", "X")

        # 设置Y轴刻度范围
        self.ui.plot.setYRange(min=-10, max=50)

        # 显示表格线
        self.ui.plot.showGrid(x=True, y=True)

        # 背景色改为白色
        self.ui.plot.setBackground('w')

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        self.ui.plot.plot(hour, temperature, pen=pg.mkPen('b'))


if __name__ == "__main__":
    app = QApplication()
    window = Window()
    window.show()
    app.exec_()
