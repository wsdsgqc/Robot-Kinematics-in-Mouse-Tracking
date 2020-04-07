#Ik test
import math

def rad2deg(rad):
    return rad*(180/math.pi) 
def deg2rad(deg):
    return deg*(math.pi/180)
#方案一
# def Ik(L1,L2,x0,y0,select): #这个x y 是正常的坐标系 不是y=-y那种坐标系
#     if L1+L2 < math.sqrt(x0**2+y0**2):
#         return 0,0
#     seta2 = math.acos(((x0**2+y0**2)-L1**2-L2**2)/(2*L1*L2)) #acos返回-pi/2 到 pi/2
#     beta = math.atan2(y0,x0) #注意！！！！atan2 参数先y后x
#     pesai = math.acos((x0**2+y0**2+L1**2-L2**2)/(2*L1*math.sqrt(x0**2+y0**2)))
#     if select == 1:
#         seta1 = beta + pesai
#         return seta1,-seta2,beta,pesai
#     elif select == 2:
#         seta1 = beta - pesai
#         return seta1,seta2,beta,pesai
# seta1,seta2,beta,pesai = Ik(100,100,170,70,1)

#方案2
# def Ik(L1,L2,x0,y0,select): #这个x y 是正常的坐标系 不是y=-y那种坐标系
#     if L1+L2 < math.sqrt(x0**2+y0**2):
#         return 0,0
#     seta2 = math.acos((L1**2+L2**2-(x0**2+y0**2))/(2*L1*L2)) #acos返回-pi/2 到 pi/2
#     seta2 = math.pi - seta2
#     beta = math.atan2(y0,x0) #注意！！！！atan2 参数先y后x
#     pesai = math.acos((x0**2+y0**2+L1**2-L2**2)/(2*L1*math.sqrt(x0**2+y0**2)))
#     if select == 1:
#         seta1 = beta + pesai
#         return seta1,-seta2,beta,pesai
#     elif select == 2:
#         seta1 = beta - pesai
#         return seta1,seta2,beta,pesai

seta1,seta2,beta,pesai = Ik(100,100,170,70,2)

print("seta1:"+str(rad2deg(seta1)))
print("seta2:"+str(rad2deg(seta2)))
print("beta:"+str(rad2deg(beta))) 
print("pesai:"+str(rad2deg(pesai)))   