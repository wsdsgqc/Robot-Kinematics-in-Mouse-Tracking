from graphics import GraphWin,Line,Point,Text

import math
baseX = 250
baseY = 450
win = GraphWin('RobotKinematicsSimulation',500,500)
def FK(L1,L2,seta1,seta2):#
    x0 = math.cos(seta1-seta2)*L2+L1*math.cos(seta1)
    y0 = math.sin(seta2-seta1)*L2+L2*math.sin(seta1)
    return x0,y0

#return value in deg 根据书上几何解内容编写
def Ik(L1,L2,x0,y0,select):
    if L1+L2 < math.sqrt(x0**2+y0**2):
        return 0,0
    seta2 = math.acos((L1**2+L2**2-(x0**2+y0**2))/(2*L1*L2))
    seta2 = math.pi-seta2
    beta = math.atan2(y0,x0)
    pesai = math.acos((x0**2+y0**2+L1**2-L2**2)/(2*L1*math.sqrt(x0**2+y0**2)))
    if select == 1:
        seta1 = beta + pesai
        return seta1,-seta2
    elif select == 2:
        seta1 = beta - pesai
        return seta1,seta2

def rad2deg(rad):
    return rad*(180/math.pi) 
def deg2rad(deg):
    return deg*(math.pi/180)
#下面的代码是为了画图 所以无法用FK来做 因为FK没办法获取到每个连杆的位置
def drawLeg():
    link1length = float(input("Plz input your link1 length:"))
    link2length = float(input("Plz input your link2 length:"))
    print("Plz click a point that you wanna caculate IK")
    p = win.getMouse()
    seta1,seta2 = Ik(link1length, link2length, p.getX()-baseX, baseY-p.getY(), 2)#因为要输入长度,所以减去基坐标
    if seta1 == 0 and seta2 == 0:
        print("out of range cannot reach the point")
    x1 = link1length*math.cos(seta1) #使用增量  未用实际量
    y1 = math.sqrt(link1length**2-x1**2)
    x2 = link2length*math.cos(seta1+seta2)#
    y2 = math.sqrt(link2length**2-x2**2)
    link1 = Line(Point(baseX,baseY),Point(x1+baseX,baseY-y1))
    link2 = Line(Point(x1+baseX,baseY-y1),Point(baseX+x1+x2,baseY-y1-y2))

    link1.draw(win)
    link2.draw(win)
    win.getMouse()
    win.close()
drawLeg()


