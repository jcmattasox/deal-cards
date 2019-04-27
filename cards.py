#cards V1
# JC Matteson



# testing functions and random by dealing cards
#JC Matteson
# to be fixed on future version, cards can repeat



import random   

used = []      

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
        print ( card(), 'of Hearts')
def spade():    
        print ( card(), 'of Spades')
def club():
        print ( card(), 'of Clubs')
def dimonds():
        print ( card(), 'of Diamonds')

num = int(input ('How many cards would you like? \n'))
for g in range (num):
    deal = (random.randint(1,4))
    if deal == 1:
        heart()
    if deal == 2:
        spade()
    if deal == 3:
        club()
    if deal == 4:
        dimonds()

    
