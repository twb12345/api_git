"""
@Time    : 2021/1/20 15:09
@Author  : tangweibin
@FileName: FileOperation.py
@Function: 文件操作类
"""


def foo(num):
    print("starting...")
    while num < 5:
        yield num +1
        num = num + 1
for n in foo(0):
    print(n)

