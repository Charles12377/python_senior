"""
装饰器
本质是一个闭包函数，目的是在不改变原有功能的前提下，对其功能做增强
"""

def check_login(fun_name):

    def fun_inner():
        print('校验登录...登录成功！')
        fun_name()

    return fun_inner

@check_login  #装饰器语法糖写法
def comment():
    #print('登录中')  #需要添加的功能
    print('发表评论')

def payment():
    print('支付中...')

#测试
comment()
print('-'*34)

#传统方式
fun_inner=check_login(comment)
fun_inner()
print('-'*34)

payment=check_login(payment)  #被装饰函数使用原函数名
payment()

payment()  #被装饰函数使用原函数名后会导致原函数无法调用
print('='*34)

#语法糖
comment()