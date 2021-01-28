"""
@Time    : 2021/1/20 15:09
@Author  : tangweibin
@FileName: FileOperation.py
@Function: 文件操作类
"""


def foo(num):
    print("starting...")
    while num < 5:
        res = yield num
        print(res)
        num = num + 1
# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:",res)

g = foo(0)
print(g.__next__())
print(g.send(888))
# print(g.__next__())

