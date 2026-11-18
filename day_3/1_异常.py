def fun_1():
    print('函数1执行')
    num=1/0
    print('函数1结束')

def fun_2():
    print('函数2执行')
    fun_1()
    print('函数2结束')

def main():
    try:
        fun_2()
    except Exception as e:
        print(f'异常：{e}')

main()