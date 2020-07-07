# a = 10
# b = 20
# print(a + b)
#
# a,b,c = [1,2,3,]
# print(a)
# print(b)
# print(c)
#
# x,y,*z = (1,2,3,4,5)
# print(x)
# print(y)
# print(z)
#
# a = 10
# b = 20
# print(a)
# print(b)
#
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)
# print(a//b)
#
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)
#
# print(a and b)
# print(a or b)
#
# z = 11
# print(z % 2 == 1)
# print(z % 2 == 0)
#
# z = 123456
# print(z % 10)
# # z //= 10
# z = z // 10
# print(z)
# print(z % 10)
#
# l = ['水果','饮料','调料','肉类','鱼类']
# if ('大米' in l):
#     print('打折')
# else:
#     print('不打折')
#
#
# C = 82
# if (0<=C<=59):
#     print("不及格")
# if (60<=C<=70):
#     print("及格")
# if (71<=C<=80):
#     print("良好")
# if (81<=C<=100):
#     print("优秀")
#
# score_l = [50,40,80,79,99,66]  #可迭代对象
#
# for score in score_l:
#     if (score > 0 and score < 60):
#         print('不及格')
#     elif (score >= 60 and score <= 70):
#         print('及格')
#     elif (score > 70 and score <= 80):
#         print('良好')
#     elif (score > 80 and score <= 100):
#         print('优秀')
#     else:
#         print('请输入正确成绩')


# s = 0
# for i in range(100):
#     s = s + i
# print(s)
#
# # range()
#
# for i in range(1,100,2):
#     print(i)
#
# s = 1
# for i in range(10,0,-1):
#     s = s * i
# print(s)

#
# flag = True
# a = 555
# while   flag:
#     b = int(input('请输入数字'))
#     if b > a :
#         print('大了')
#     elif(b < a):
#         print('小了')
#     else:
#         print('猜对了')
#         flag = False


# 找出100内能被3整除的整数

# for i in range(1,100):
#     if(i % 3 != 0):
#         continue
#     print(i)


#定义一个求两个数相除的商和余数的方法

# def level(a,b):
#     print(a // b)
#     print(a % b)
# level(100,7)
# level(7,187)
#
# def shang_yu(a,b):
#     if(b == 0):
#         print('除数不能为0')
#     else:
#         print('商:', a // b , ',余数', a % b)
#
# shang_yu(44,8)
# shang_yu(4,89)
# shang_yu(99,0)


#
# def level(a,b):  #形参
#     print(a // b)
#     print(a % b)
# level(100,7)
# level(7,187)

# def shang_yu(a,b):
#     if(b == 0):
#         return None  #return 返回值
#     else:
#         return(a // b , a % b)
#
# #res = shang_yu(80,10)  #按照位置传参
# res = shang_yu(b=10,a=2) #按照关键字传参
#
# if res is None:
#     print('参数错误')
# else:
#     print('商为：',res[0],'余数为:',res[1])
#
# def sunl(*args):
#     s = 0
#     for i in args:
#         s+=i
#     return  s
# print(sunl(1,2,3,465,46,45,32,132,564))


#面向对象
# class calc():
#     a=None
#     b=None
#     res=None
#     def input(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
# c = calc()  # 类的实例化 c对象
#
# c.input(10,20)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()

# class calc():
#     res=None
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
# c = calc(29,39)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()



# 九九乘法表
# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'X',i,'=',i*j,end='\t')
#     print()

#
# # 冒泡排序
#
# l = [1,2,3,4,5,6]
# length = len(l)
# for i in range(length-1,0,-1): #外出循环确定排好序的数据下标
#     for j in range(i): #遍历未排好序的列表
#         if (l[j] > l[j+1]): #判断相邻两个数据，前边的如果大于后边的，则交换两个数据的位置
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

# 99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         if j <= i:
#             print(j,"x",i ,"=",i*j,end='\t')
#             # print("%d*%d=%d" % (j, i, i * j), end=" ")
#     print()
#

# 冒泡排序
# a = [7,8,2,4,78,8,3,4,1]
# # len()获取序列长度
# length = len(a)  # 9
# # 利用range函数逆序截取遍历获取列表的每一个的个数
# for i in range(length-1,0,-1):  # length-1 因为列表索引是从0开始索引的,所以需要-1
#     # 遍历列表中每个索引值
#     for j in range(0,i):
#         # 判断每个索引的值的大小,如果前面的值比后面的值大
#         if a[j] > a[j+1]:
#             # 交换位置,将前后位置互换
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)
#




# a = [4,78,6,32,8,3,14,9]
# length = len(a)
# for i in range(length-1 , 0 , -1):
#     for j in range(0 , i):
#         if a[j] > a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)


#继承

class Parent():
    money = 100000000
    house = 100
    __yi_wu = '三妻四妾'

    def shou_yi(self):
        print('葵花宝典')

class Child(Parent):
    ai_hao = '吃喝玩乐'
    super().__init__()
    def shou_yi(self):
        print('吃喝嫖赌')

c = Child()
print(c.ai_hao)
print(c.money)
print(c.house)















