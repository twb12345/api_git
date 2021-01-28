"""
@Time    : 2021/1/20 15:09
@Author  : tangweibin
@FileName: FileOperation.py
@Function: 文件操作类
"""


def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)

g = foo()
print(next(g))
print("*"*20)
print(next(g))