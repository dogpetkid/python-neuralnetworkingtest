##From: https://spin.atomicobject.com/2014/06/24/gradient-descent-linear-regression/
class POINT():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def Errorsolve(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        totalError += (points[i].y - (m * points[i].x + b)) ** 2
    return totalError / float(len(points))

m = -1
b = 2
points = [POINT(0,0),POINT(1,0)]
print(Errorsolve(b,m,points))
input()
