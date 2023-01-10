# 可以将可能发生异常的代码放到try中，使用except采取措施
""""
try:
    open("D:/SummerStar/Desktop/111.txt",'r',encoding='utf-8');
except: #这里是对所有的异常类型进行处理
    open("D:/SummerStar/Desktop/222.txt", 'w', encoding='utf-8');
"""

# 指定类型的处理
"""
try:
    print(name)
except NameError as a: # 指定变量名进行处理，如果是其他得则不执行下面的代码
    print("出错，名称未定义")
"""

#异常的传递性 - 异常可通过函数传递
"""
def fun1():
    1 / 0
def fun2():
    fun1()
fun2()
"""

# 捕捉多个异常
# 第一种写法：太麻烦
"""
try:
    a = 5 / 0
    print(name)
except ZeroDivisionError: # 指定变量名进行处理，如果是其他得则不执行下面的代码
    print('不能除0除0')
except NameError :
    print("出错，名称未定义")
"""
# 第二种写法
try:
    a = 5 / 0
    print(name)
except (ZeroDivisionError,NameError): #
    print('除0或未定义名称')
