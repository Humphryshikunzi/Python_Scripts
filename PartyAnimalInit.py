class PartAnimal:
    x = 0;
    name = ""
    def __init__(self, nam, x = 140):
        self.name = nam
        self.x = x
        print(self.name,'Constructed')
    def party(self):
        self.x = self.x+1
        print(self.name,'party count',self.x)
s = PartAnimal('Sally')
j = PartAnimal('Jim',10)
s.party()
j.party()
s.party()