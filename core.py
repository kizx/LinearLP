# -*- coding: utf-8 -*-
import numpy as np


class LinearProgram:
    def __init__(self, ObjFun, Limits, HalfPlanes):
        self.fun = ObjFun  # 目标函数
        self.limts = Limits  # 约束
        self.lines = HalfPlanes  # 半平面
        px = self.limts[0] if ObjFun[1] > 0 else -self.limts[0]
        py = self.limts[1] if ObjFun[1] > 0 else -self.limts[1]
        self.v = [px, py]  # 初始化v0
        print('v0=', self.v)

    def main(self):
        for index, i in enumerate(self.lines):
            if i[0] * self.v[0] + i[1] * self.v[1] <= i[2]:
                pass  # 如果v满足当前半平面则v不变
            else:
                xrange = self.xrange(index)  # l上x的取值区间
                if xrange is None:
                    return None, None
                p = self.getp(xrange, index)  # 根据区间求出l上最优的的p点
                self.v = p
            print(f'v{index + 1}=', self.v)
        ans = self.fun[0] * self.v[0] + self.fun[1] * self.v[1]  # 目标函数值
        return self.v, ans

    def add(self, newline):
        """添加约束条件时更新"""
        self.lines.append(newline)
        index = len(self.lines) - 1
        if newline[0] * self.v[0] + newline[1] * self.v[1] <= newline[2]:
            pass  # 如果v满足当前半平面则v不变
        else:
            xrange = self.xrange(index)  # l上x的取值区间
            if xrange is None:
                return None, None
            p = self.getp(xrange, index)  # 根据区间求出l上最优的的p点
            self.v = p
        print(f'v{index + 1}', self.v)
        ans = self.fun[0] * self.v[0] + self.fun[1] * self.v[1]  # 目标函数值
        return self.v, ans

    def xrange(self, index):
        """
        输入当前的直线，求出该直线与前面所有的直线的交点，返回x取值区间
        :index: 当前直线l的索引
        """
        xleft = []
        xright = []
        for i in self.lines[:index]:
            A_b = np.array([i, self.lines[index]])
            A = A_b[:, :2]
            if np.linalg.det(A) == 0:  # 平行无交点
                if self.lines[index][1] == 0:  # 竖直情况
                    _x = self.lines[index][2] / self.lines[index][0]
                    _y = 0
                else:
                    _x = 0
                    _y = self.lines[index][2] / self.lines[index][1]
                if i[0] * _x + i[1] * _y <= i[2]:  # 在l上任取一点测试l是否满足h
                    continue
                else:
                    return None
            else:
                b = A_b[:, -1]
                x, y = np.linalg.solve(A, b)
                if self.lines[index][1] == 0:  # 处理l竖直情况，这里获取得是y的范围
                    if i[1] > 0:
                        xright.append(y)
                    if i[1] < 0:
                        xleft.append(y)
                else:
                    if i[0] < 0:
                        xleft.append(x)
                    elif i[0] > 0:
                        xright.append(x)
                    elif i[0] == 0:  # 处理h水平线情况，利用l判断
                        if self.lines[index][0] > 0:
                            xright.append(x)
                        elif self.lines[index][0] < 0:  # 如果l也水平则平行前面已经处理
                            xleft.append(x)
        m = 1 if self.lines[index][1] == 0 else 0  # 限制取值范围
        xl = max(xleft) if xleft else -self.limts[m]
        xl = -self.limts[m] if xl < -self.limts[m] else xl
        xr = min(xright) if xright else self.limts[m]
        xr = self.limts[m] if xr > self.limts[m] else xr
        result = None if xl > xr else [xl, xr]
        return result

    def getp(self, xrange, index):
        """传入x左右值，比较哪个点更优"""
        if self.lines[index][1] == 0:  # 竖直情况
            x1 = x2 = self.lines[index][2] / self.lines[index][0]
            y1, y2 = xrange
        else:
            x1 = xrange[0]
            y1 = (self.lines[index][2] - self.lines[index][0] * x1) / self.lines[index][1]
            if y1 > self.limts[1]:
                y1 = self.limts[1]
            elif y1 < -self.limts[1]:
                y1 = -self.limts[1]

            x2 = xrange[1]
            y2 = (self.lines[index][2] - self.lines[index][0] * x2) / self.lines[index][1]
            if y2 > self.limts[1]:
                y2 = self.limts[1]
            elif y2 < -self.limts[1]:
                y2 = -self.limts[1]

        a = self.fun[0] * x1 + self.fun[1] * y1
        b = self.fun[0] * x2 + self.fun[1] * y2
        if a >= b:
            p = [x1, y1]
        else:
            p = [x2, y2]
        return p


if __name__ == '__main__':
    _ObjFun = [1, 1]
    _limts = [100, 100]
    _HalfPlanes = [[1, -1, 2], [1, 1, 2], [1, -1, -3]]
    test = LinearProgram(_ObjFun, _limts, _HalfPlanes)
    myresult = test.main()
    print('结果', myresult)
