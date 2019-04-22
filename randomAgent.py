from agent import Agent
import random


class RandomAgent(Agent):
    
    
    def __init__(self,marketValue):
        super(RandomAgent,self).__init__()
        self.idealBuyPrice = marketValue +  random.randint( -marketValue/10,0)
        self.idealSellPrice = marketValue + random.randint(0,marketValue/2)
        self.setBids()
        agentType= "Random"
       
        
    def update(self,marketValue):
        self.idealBuyPrice = marketValue +  random.randint(-marketValue/10,0)
        self.idealSellPrice = marketValue + random.randint(0,marketValue)
        self.bidsToBuy = []
        self.bidsToSell= []

        self.setBids()


    def setBids(self,marketPrice=0):
        
        for i in range(10, self.funds//self.idealBuyPrice, 10):
            self.bidsToBuy.append((i, int(self.idealBuyPrice**(1-(i/(self.funds//self.idealBuyPrice))))))


        for i in range(10, self.numOwnedShares,10):
           preportionOfShares = (i/self.numOwnedShares)
           self.bidsToSell.append((i, int(self.idealSellPrice ** preportionOfShares)))
            










