# -*- coding: utf-8 -*-
import numpy as np

Limits = [200, 100]
HalfPlanes = [[1, -1, 2], [1, 1, 2], [0, 2, -1]]
ObjFun = [1, 1]


class LinearProgram:
    def __init__(self):
        px = Limits[0] if ObjFun[1] > 0 else -Limits[0]
        py = Limits[1] if ObjFun[1] > 0 else -Limits[1]
        self.v = [px, py]  # 初始化v0
        print('v0', self.v)
        self.main()

    def main(self):
        for index, i in enumerate(HalfPlanes):
            if i[0] * self.v[0] + i[1] * self.v[1] <= i[2]:
                pass
            else:
                xrange = self.xrange(index)
                p, ans = self.getp(xrange, index)
                print(p, ans)

    @staticmethod
    def xrange(index):
        xleft = []
        xright = []
        for i in HalfPlanes[:index]:
            print(i, index)
            A_b = np.array([i, HalfPlanes[index]])
            A = A_b[:, :2]
            b = A_b[:, -1]
            x, y = np.linalg.solve(A, b)
            if i[0] < 0:
                xleft.append(x)
            elif i[0] > 0:
                xright.append(x)
            else:
                print('水平')
        xl = max(xleft) if xleft else -Limits[0]
        xr = min(xright) if xright else Limits[0]
        result = None if xl > xr else [xl, xr]
        print('xl,xr', result)
        return result

    @staticmethod
    def getp(xrange, index):
        if xrange is None:
            return None
        else:
            x1 = xrange[0]
            y1 = (HalfPlanes[index][2] - HalfPlanes[index][0] * x1) / HalfPlanes[index][1]
            x2 = xrange[1]
            y2 = (HalfPlanes[index][2] - HalfPlanes[index][0] * x2) / HalfPlanes[index][1]
            a = ObjFun[0] * x1 + ObjFun[1] * y1
            b = ObjFun[0] * x2 + ObjFun[1] * y2
            if a >= b:
                p = [x1, y1]
                ans = a
            else:
                p = [x2, y2]
                ans = b
        return p, ans


if __name__ == '__main__':
    test = LinearProgram()
