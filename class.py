#class creation
class Vehicle:
    color="Black"#attributes
    petrolOrDiesel="petrol"
    mileage="10"
    def start():#methods of function inside classes
        print("When you press clutch and accelerator then vehicle is started")
#object creation
car=Vehicle()
car.color="white"
print(car.color)

bike=Vehicle()
print(bike.color)
aeroplane=Vehicle()
print(aeroplane.mileage)
#we created one class and 3 objects of that class
