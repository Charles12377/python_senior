"""
细节
    装饰器的内部函数格式 要和 被装饰的原函数 保持一致
    即：原函数是无参无返回的，则 装饰器的内部函数也必须是 无参无返回的
    原函数是有参有返回的，则 装饰器的内部函数也必须是 有参无返回的
"""

def my_decorate(fun_name):

    def fun_inner(a,b):
        print('正在计算中...')
        fun_name(a,b)

    return fun_inner

@my_decorate
def get_sum(a,b):
    sum=a+b
    print(f'求和结果：{sum}')

#测试(两种方法不能一起调用，会导致装饰器重复调用)
#传统方式
#fun_inner=my_decorate(get_sum)
#fun_inner(15,20)
print('-'*34)

#语法糖
get_sum(a=3,b=4)