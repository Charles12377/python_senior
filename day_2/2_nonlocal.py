#nonlocal（声明可以让内部函数修改外部函数的变量值）

def fun_outer():
    a=10

    def fun_inner():
        nonlocal a
        a=a+1
        print(f'a:{a}')

    return fun_inner

#测试
if __name__ =='__main__':
    fun_inner=fun_outer()
    fun_inner()
    fun_inner()
    fun_inner()