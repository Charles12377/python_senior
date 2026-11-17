#校验登录装饰器
def check_login(fun_name):

    def fun_inner():
        print('校验登录...登陆成功！')
        fun_name()

    return fun_inner

#校验验证码装饰器
def check_code(fun_name):

    def fun_inner():
        print('校验验证码...校验成功！')
        fun_name()

    return fun_inner

#@check_login
#@check_code
def comment():
    print('发表评论')

#测试

#传统写法
cc=check_code(comment)
cl=check_login(cc)
cl()

#语法糖写法
#comment()