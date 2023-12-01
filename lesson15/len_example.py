class Building:
    def __init__(self, name, street):
        self.name = name
        self.street = street
        self.stages = {}

    def __len__(self):
        return len(self.stages)

    def __setitem__(self, key, value):
        self.stages[key] = value

    def __getitem__(self, item):
        return self.stages[item]

    def grand_opening(self):
        return 'Congratulations. prepare to live in horror world you built'


class Company:
    def __init__(self, name, industry):
        self.name = name
        self.industry=industry


if __name__ == '__main__':
    building1 = Building('EmpireStatePlazaElite', 'Khreshatyk')
    print(len(building1))
    tesla = Company('Tesla', 'automotive')
    hotels = Company('TrumpHotels', 'realestate')
    building1[1] = tesla
    building1[2] = hotels
    print(len(building1))
    print(building1[1].name)

