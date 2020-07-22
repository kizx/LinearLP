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
                    return None
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
                return None
            p = self.getp(xrange, index)  # 根据区间求出l上最优的的p点
            self.v = p
        print(f'v{index + 1}', self.v)
        ans = self.fun[0] * self.v[0] + self.fun[1] * self.v[1]  # 目标函数值
        return self.v, ans

    def xrange(self, index):
        xleft = []
        xright = []
        for i in self.lines[:index]:
            A_b = np.array([i, self.lines[index]])
            A = A_b[:, :2]
            if np.linalg.det(A) == 0:  # 平行无交点
                _x = 0
                _y = self.lines[index][2] / self.lines[index][1]
                if i[1] * _y <= i[2]:  # 在l上任取一点测试l是否满足h
                    continue
                else:
                    return None
            else:
                b = A_b[:, -1]
                x, y = np.linalg.solve(A, b)
                if i[0] < 0:
                    xleft.append(x)
                elif i[0] > 0:
                    xright.append(x)
                else:
                    print('水平')
        xl = max(xleft) if xleft else -self.limts[0]
        xl = -self.limts[0] if xl < -self.limts[0] else xl
        xr = min(xright) if xright else self.limts[0]
        xr = self.limts[0] if xr > self.limts[0] else xr
        result = None if xl > xr else [xl, xr]
        return result

    def getp(self, xrange, index):
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
