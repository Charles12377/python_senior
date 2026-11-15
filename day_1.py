class Car:

    owner='w'

    def __init__(self,color,number):
        self.color=color
        self.number=number
        self.__key=12345

    @classmethod
    def show1(cls):
        print(f'cls:{cls}')
        print(cls.owner)
        print('我是类方法')

    @staticmethod
    def show2():
        print(Car.owner)
        print('我是静态方法')

    def __str__(self):
        return f'颜色；{self.color},号码；{self.number}'

    def __del__(self):
        print(f'{self}对象被删除了')

    def run_car(self):
        print('汽车会跑')

class ElectricCar(Car):
    pass


c1=Car('red',1)
print(c1)
c1.show1()
c1.show2()
print('-'*34)

print('程序结束')

print('='*34)
c2=ElectricCar('blue','3')
