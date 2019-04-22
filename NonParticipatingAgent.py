from agent import Agent
import random


class NonParticipating(Agent):
    
    
    def __init__(self,marketValue):
        super(NonParticipating,self).__init__()
        self.idealBuyPrice = marketValue +  random.randint( -marketValue/10,0)
        self.idealSellPrice = marketValue + random.randint(0,marketValue/2)
        self.setBids()
        self.agentType= "NonParticipating"
       
        
    def update(self,marketValue):
        self.idealBuyPrice = marketValue +  random.randint(-marketValue/10,0)
        self.idealSellPrice = marketValue + random.randint(0,marketValue)
        self.bidsToBuy = []
        self.bidsToSell= []

        self.setBids()


    def setBids(self,marketPrice=0):
     pass
            










