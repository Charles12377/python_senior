"""
一个装饰器有且只能有一个参数
如果有多个参数，可在装饰器的外边再包裹一层，把该装饰器当作其 内部函数 返回即可
"""
def logging(flag):

    def my_decorate(fun_name):
    #def my_decorate(fun_name,flag):(报错)

        def fun_inner(a,b):
            if flag == '+':
                print('正在计算[加法]...')
            elif flag == '-':
                print('正在计算[减法]...')
            return fun_name(a,b)

        return fun_inner

    return my_decorate

@logging('+')
def get_sum(a,b):
    return a + b

@logging('+')
def get_sub(a,b):
    return a - b


print(get_sum(2,5))
print(get_sub(7,3))
print('-'*34)

#优化版
def my_decorate(fun_name):
    #def my_decorate(fun_name,flag):(报错)

        def fun_inner(a,b):
            if fun_name.__name__ == 'get_sum':
                print('正在计算[加法]...')
            elif fun_name.__name__ == 'get_sub':
                print('正在计算[减法]...')
            return fun_name(a,b)

        return fun_inner

@my_decorate
def get_sum(a,b):
    return a + b

@my_decorate
def get_sub(a,b):
    return a - b


print(get_sum(2,5))
print(get_sub(7,3))
print('-'*34)