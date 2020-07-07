# from day02 import module_1
# from day02.module_1 import  a as module_1_a,name,Test
#
#
# a = '我是模块2中的a变量'
#
# def name():
#     print('我是模块2中的name方法')
#
# class Test():
#     name='我是模块2中的Test类'
# if __name__ == '__main__':
#     print(module_1.a)
#
# print(module_l.a)
# name()
# print(Test.name)
#

# a = 123
# b = '456'
# #字符串转数字
# print(a + int(b))
# #数字转字符串
# print(str(a)+b)
#
# t = (1,2,3,4)
# l = [1,2,3,4,5,]
# s = {1,2,3,4,5,6,}
# #字符串转列表
# print(list(b))
# #元祖转列表
# print(list(b))
# #列表转元祖
# print(tuple(l))
# #元祖转集合
# print(set(t))
# #集合转列表
# print(list(s))
#
# # 打开模式： r读取 w清空写入 a追加写入 b二进制模式
# f = open('zkn.txt','w') #open打开文件
# f.write('hello,zhihua') #输出
# f.close() #关闭文件
#
# f = open('zkn.txt','a') # open打开文件
# f.write('\nhi,shuxians') # write写入内容至打开的文件
# f.close() #关闭文件
#
# f = open('zkn.txt','r')
# # print(f.read())      #默认读取全部数据
# # print(f.read(4))      #读取指定大小的数据
# # print(f.readline())   #按行读取，读取一行
# print(f.readlines())   #按行读取，读取所有行
# f.close()
#
# a = 'abcdefghijkl'
# print(a[0])
# print(a[-1])
# print(a[1:-2])
# print(a[1:-2:2])
# print(a[-1:0:-1])
# print(a[::])
# print(a[::-1])
# print(a[2:])
# print(a[:-2])
#
# a = 'abcdefghijkl'
# for i in a:
#     print(i)
#
# with open('zkn.txt','r') as f:  # with 使用一个上下文管理器
#     lines = f.readlines()
#     print(lines)
#     for i in lines:
#         print(i.replace('\n',''),end='')  # print 默认带一个换行

# # 通过占位符格式化
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d X %d = %d"%(j,i,i*j), end="\t")
#     print()
#
# # .format
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{} X {} = {}".format(j,i,i*j), end="\t")
#     print()

#
# l = [2,65,6,2,4,35,13,5,3,2,1,23,48]
#
# l[0] = 10
# print(l)
# l[0:7] = 66,55,44,33,22,11
# print(l)

#
# l = [3,56,1,31]
# l.append("王铁锤")
# l.append("王钢锤")
# l.extend({"王石锤","小锤锤",555})
# l.insert(4,"锤死你")
# print(l)
#
#
# print(l.pop())
# print(l)
# print(l.pop(1))
# print(l)
#
# l.remove(3)
# print(l)
#
# l.remove('王铁锤')
# print(l)
#
# l = [True,46,54,254]
# # l.remove(1)
# # print(l)
#
#
# a = [132,54,4,63,56,5,2,3,52,3,85]
# a.sort()
# print(a)
# a.sort(reverse)
# print(a)

# d = {'name':'王大锤','age':18,'sex':'男'}
# print(d)
# d.update({'addr':'上海静安','学历':'本科'})
# print(d)


# 今天到此结束
#
# def div(a,b):
#     try:
#         return a / b
#     except:
#         return
# print(div(10,5))


class CustomException(Exception):
    def __init__(self,value = "值不能为0"):
        self.value = value

    def __str__(self):
        return  self.value

a = 0

try:
    if a == 0:
        print("a = {}触发异常",format(a))
        raise CustomException
    print('a= {} 未触发异常'.format(a))
except CustomException as e:
    print(e)

