# coding: utf-8
class Car():

    def __init__(self, num=0):
        self.num = num

    def set_num(self, num):
        self.num = num

    def get_num(self):
        return self.num

    _private_str = "private"
    def _private_method(self):
        print(self._private_str)

# car1のインスタンス．コンストラクタの初期値が設定される．
car1 = Car()
print(car1.get_num())
# car2のインスタンス．numを関数で与える．
car2 = Car()
car2.set_num(1111)
print(car2.get_num())
# car3のインスタンス．コンストラクタ使用．
car3 = Car(9999)
print(car3.get_num())
#print(car3._private_method())
