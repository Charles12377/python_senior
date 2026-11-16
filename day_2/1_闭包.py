#闭包


def get_sum(a,b):
    return(a+b)

print(get_sum)  #函数对象
print(get_sum(3,5))  #调用函数，获取返回值
print('-'*34)

#闭包演示
def fun_outer(num1):



    def fun_inner(num2):
        sum=num1+num2
        print(f'求和结果为{sum}')

    return fun_inner

#调用
fun_inner=fun_outer(29)
fun_inner(20)
print('-'*34)
fun_outer(4)(5)
