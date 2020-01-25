import random as ran
class Hand:
    cards=[]
    value=0
    def draw_from(self,deck):
        deck.shuffle()
        c=deck.next_card()
        self.cards.append(c)
        self.value+=c.value
    def return_to(self,deck):
        c=self.cards.pop(-1)
        deck.append(c)
        self.value-=c.value
        
class Card:
    def __init__(self,face,suit,value):
        self.face=face
        self.suit=suit
        self.value=value
    def __str__(self):
        return f'{self.value} {self.suit} {self.face}'

class Deck:
    li=[] 
    def __init__(self,item):
        self.li=item.copy()        
    def shuffle(self):
        ran.shuffle(self.li)
    def next_card(self):
        return self.li.pop(0)
    def return_cards(self,crd):
        self.li.append(crd)

class Player:
    credit=0
    hand = Hand()
    def __init__(self,name,credit):
        self.name=name
        self.credit+=credit
    def play(self,deck):
        self.hand.draw_from(deck)
        if int(self.hand.value) > 20 :
            print(self.name,"Won")
            for i in self.hand.cards:
                print(i)
            exit()
        
   # def show_hand():

   # def hit_or_stand():
        
class  Game:
    dealer = 1
    def __init__(self,name):
        self.name=name
    def play(self,deck):
        player1=Player('aditya',0)
        player2=Player('priyanshu',0)
        while True:
            player1.play(deck)
            player2.play(deck)
        
        
        
    #def get_bust_probability(self):






        
cards=[]
for i in range(1,10):
    for j in range(4):
        if j==0:                               #clubs (♣), diamonds (♦), hearts (♥) and spades (♠),
            cards.append((Card(i,'club',i)))
        elif j==1:
            cards.append((Card(i,'diamond',i)))
        elif j==2:
            cards.append((Card(i,'heart',i)))
        elif j==3:
            cards.append((Card(i,'spade',i)))
    cards.append(Card('J','club',11))
    cards.append(Card('J','diamond',11))
    cards.append(Card('J','heart',11))
    cards.append(Card('J','spade',11))

    cards.append(Card('Q','club',12))
    cards.append(Card('Q','diamond',12))
    cards.append(Card('Q','heart',12))
    cards.append(Card('Q','spade',12))

    cards.append(Card('K','club',13))
    cards.append(Card('K','diamond',13))
    cards.append(Card('K','heart',13))
    cards.append(Card('K','spade',13))

deck= Deck(cards)
g = Game('MyGame')
g.play(deck)
