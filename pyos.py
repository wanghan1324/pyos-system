import sys,datetime
from datetime import*
def startUser():
    while True:
        c = input("username:")
        d = "wanghan"
        if c == d:
            startPsword()
        else:
            continue
        break
def startPsword():
    while True:
        e = input("password:")
        f = "117123"
        if e == f:
            print("welcome to pyos!")
            function()
        else:
            continue
        break
def function():
    while True:
        a = input("/")
        b = "shutdown"
        h = "help"
        i = "nowtime"
        j = datetime.now()
        k = "ctr"
        l = "version"
        if a == b:
            sys.exit()
        elif a == h:
            print("shutdown:关机")
            print("nowtime:现在时间")
            print("ctr:计算器")
            print("version:系统版本")
        elif a == i:
            print(j)
        elif a == k:
            def add(x, y):
                return x + y
            def subtract(x, y):
                return x - y
            def multiply(x, y):
                return x * y
            def divide(x, y):
                return x / y
            # 用户输入
            print("选择运算：")
            print("1、相加")
            print("2、相减")
            print("3、相乘")
            print("4、相除")
            choice = input("输入你的选择(1/2/3/4):")
            num1 = int(input("输入第一个数字: "))
            num2 = int(input("输入第二个数字: "))
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            else:
                print("非法输入")
        elif a == l:
            print("version: pyos 1.0.1")
            print("composer's network mailbox: <https://2879790643@qq.com>")
        else:
            continue
startUser()