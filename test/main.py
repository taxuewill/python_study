#!/usr/bin/python3
# coding=utf-8

print("main ",__package__)

from package1 import Car

if __name__ == '__main__':
    print("this is main enter")
    car = Car()
    print("car is ",car.name)
