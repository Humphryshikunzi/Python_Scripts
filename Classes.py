class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x+1;
        print('So far', self.x)

an = PartyAnimal()
i = 1;
while i<21:
    an.party()
    i+=1;


an.x