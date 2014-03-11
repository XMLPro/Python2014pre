# coding: utf-8
# 継承されるクラス
class Car():

    def __init__(self, num=0000):
        self.num = num

    def set_num(self, num):
        self.num = num

    def get_num(self):
        return self.num

# 継承したクラス
class SuperCar(Car):

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

# 継承したクラスでインスタンスを作成
supercar = SuperCar(9999)
# SuperCarで定義したメソッドはもちろん使える
supercar.set_speed(100)
# 継承されるクラスで定義していたメソッドも使える
print(supercar.get_num())
print(supercar.get_speed())
