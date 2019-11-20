# # 列表生城式
# lis = [x * x for x in range(10)]
# print(lis)
#
# # 生成器
# lis_generator = (x * x for x in range(10))
# print(lis_generator)
#
# print(lis_generator.__next__())
# print(lis_generator.__next__())
# print(lis_generator.__next__())
# print(lis_generator.__next__())
# print(lis_generator.__next__())
#
# generator_ex = (x * x for x in range(100))
# for i in generator_ex:
#     print(i)


# 用函数打印费波纳契数列

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b
        n += 1
        print(a)
    return 'done'


# a = fib(10)
print(fib(10))
