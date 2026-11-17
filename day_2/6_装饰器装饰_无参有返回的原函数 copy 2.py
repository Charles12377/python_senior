"""
细节
    装饰器的内部函数格式 要和 被装饰的原函数 保持一致
    即：原函数是无参无返回的，则 装饰器的内部函数也必须是 无参无返回的
    原函数是有参有返回的，则 装饰器的内部函数也必须是 有参无返回的
    原函数是无参有返回的，则 装饰器的内部函数也必须是 无参有返回的
"""

def my_decorate(fun_name):

    def fun_inner():
        print('正在计算中...')
        return fun_name()

    return fun_inner

@my_decorate
def get_sum():
    a=10
    b=35
    return a+b

#测试(两种方法不能一起调用，会导致装饰器重复调用)
#传统方式
#fun_inner=my_decorate(get_sum)
#sum=fun_inner()
#print(sum)
print('-'*34)

#语法糖
print(get_sum())