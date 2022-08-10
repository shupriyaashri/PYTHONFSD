class Car:
    def __init__(self,name,price,colour) -> None:
        self.car_name=name
        self.car_price=price
        self.car_colour = colour

    def __str__(self) -> str:
        return f"{self.car_name}-{self.car_dep}:-{self.car_code}"

obj=Car("name","skoda","10L")
arr=[]
for i in range(2):
    arr.append(Car(input("name"),input("price"),input("colour")))

    for cars in arr:
        print(cars)