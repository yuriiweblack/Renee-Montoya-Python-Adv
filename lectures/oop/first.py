class ToyotaCamry:
    engine = "2.5 Gasoline"
    year = "2021 year"

    def __init__(self, owner_name, owner_second):
        self.owner_name = owner_name
        self.owner_second = owner_second

    def get_owner_info(self):
        print("Owner_1:", self.owner_name)
        print("Owner_2:", self.owner_second)

    def get_car_info(self):
        print(self.engine)
        print(self.year)

    def move(self):
        print('move', self.owner_name,'and', self.owner_second)


car = ToyotaCamry("Vasyl","Julia")
car.move()
car.get_owner_info()
car.get_car_info()
#
car2 = ToyotaCamry("Petro","Julia")
car2.get_owner_info()

car3 = ToyotaCamry("Jek","Nika")
car3.move()
car3.get_owner_info()