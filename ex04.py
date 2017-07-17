#coding=utf-8
#100俩汽车
cars = 100

#汽车空间4.0立方米
space_in_car = 4.0

#司机
drivers = 30

#乘客
passengers = 90

#没有分配到司机的汽车
cars_not_driven = cars - drivers

#分配到司机的汽车
cars_driven = drivers

#停车场空间
carpool_capacity = cars_driven * space_in_car

#平均每辆车搭载的乘客数量
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."

print "There are only", drivers, "drivers available."

print "There will be", cars_not_driven, "empty cars today."

print "We can transport", carpool_capacity, "people today."

print "We have", passengers, "to carpool today."

print "We need to put about", average_passengers_per_car, "in each car. "