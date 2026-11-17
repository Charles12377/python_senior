#装饰器
def my_decorate(fun_name):

    def fun_inner(*args,**kwargs):
        print('正在计算...')
        return fun_name(*args,**kwargs)

    return fun_inner

@my_decorate
def get_sum(*args,**kwargs):
    """
    `*args`：接收**位置参数**，打包成元组
    `**kwargs`：接收**关键字参数**，打包成字典
    """
    """
    sum = 0
    # args 是位置参数元组，直接遍历
    for i in args:
        sum += i
    # kwargs 是关键字参数字典，遍历值
    for v in kwargs.values():
        sum += v
    return sum
    """

    #上述代码可以优化如下
    return sum(args) + sum(kwargs.values())

sum = get_sum(1,2,3,a=4,b=5,c=6)
print(sum)