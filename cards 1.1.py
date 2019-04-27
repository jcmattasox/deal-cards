#cards V1.1
# JC Matteson
# testing functions and random by dealing cards
# to be fixed on future version, cards can repeat (fixed)
# to be fixed cant deal all 52 cards


import random   

used = []      
heartL=[]
spadeL=[]
clubL=[]
diamondL=[]
def card():           
        x =  (random.randint(1,13))
        while x  not in used:
            if x == 1:
                return ('Ace')
                used.append(x)            
            if x == 11:
                return ('Jack')
                used.append(x)            
            if x == 12:
                return ('Queen')
                used.append(x)            
            if x == 13:
                return ('King')
                used.append(x)            
            else:
                return (x)
                used.append(x)      
 


def heart():
        h = f'{card()} of Hearts'
        if h not in heartL:
                print (h)
                heartL.append(h)
        else:
                deal_cards()
        
def spade():
        s = f'{card()} of Spades'
        if s not in spadeL:
                print (s)
                spadeL.append(s)
        else:
                deal_cards()
        
def club():
        c = f'{card()} of Clubs'
        if c not in clubL:
                print (c)
                clubL.append(c)
        else:
                deal_cards()
        
def dimonds():
        d = f'{card()} of Diamonds'
        if d not in diamondL:
                print (d)
                diamondL.append(d)
        else:
                deal_cards()
def deal_cards():
        deal = (random.randint(1,4))
        if deal == 1:
                heart()
        if deal == 2:
                club()
        if deal == 3:
                dimonds()
        if deal == 4:
                spade()
        

num = int(input ('How many cards would you like? \n'))
for g in range (num):
        deal_cards()
    

    
