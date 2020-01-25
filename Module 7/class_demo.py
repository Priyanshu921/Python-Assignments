import random,time
class Coin:
    def __init__(self):
        self.sideup='Heads'
    def toss(self):
        if random.randint(0,1)==0:
            self.sideup=='Heads'
        else:
            self.sideup='Tails'
    def get_sideup(self):
        return self.sideup
c1=Coin()
print('The Side Up is',c1.get_sideup())
print('I am now tossing the coin..........')
ch=input('Enter your choice')
c1.toss()
time.sleep(2)
print(c1.get_sideup())
if ch==(c1.get_sideup()):
    print('You Won')
else:
    print('You Loss')
    
