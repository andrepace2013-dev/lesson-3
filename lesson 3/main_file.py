import pygame

class Tech():
    def __init__(self,car,ai,phone,computer,smart_asisstent):
        self.car=car
        self.ai=ai
        self.phone=phone
        self.computer=computer
        self.smart_asisstent=smart_asisstent
    def show_details(self):
        print("car = ", self.car)
        print("ai = ", self.ai)
        print("phone = ", self.phone)
        print("computer = ", self.computer)
        print("smart_asisstent = ", self.smart_asisstent)
    def car_f(self):
        print("This car can drive you where very you want  yo u can custimise it and it has massumimum comfort with speeds that go over 300kmps")
t1=Tech("suv","on system running","calls","processing","AI")
t1.show_details()
t1.car_f()