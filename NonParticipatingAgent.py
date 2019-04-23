from agent import Agent
import random


class NonParticipating(Agent):
    
    
    def __init__(self,marketValue):
        super(NonParticipating,self).__init__()
        self.idealBuyPrice = 0
        self.idealSellPrice = 0
        self.setBids()
        self.agentType= "NonParticipating"
       
        
    def update(self,marketValue):
        self.idealBuyPrice = 0
        self.idealSellPrice = 0
        self.bidsToBuy = []
        self.bidsToSell= []

        self.setBids()


    def setBids(self,marketPrice=0):
        pass
            










