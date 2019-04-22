from agent import Agent
import queue 
import random


class TrendingAgent(Agent):
    
    
    def __init__(self,marketValue):
        super(TrendingAgent,self).__init__()
        self.idealBuyPrice = marketValue
        self.idealSellPrice = marketValue 
        self.lastFourBids = queue.Queue(maxsize=4)
        self.lastFourBids = []
        self.setBids(marketValue)
        
        self.agentType= "RSI"


    def update(self,marketValue):
        self.idealBuyPrice = marketValue 
        self.idealSellPrice = marketValue 
        self.lastFourBids.append(marketValue)
        self.setBids(marketValue)

    def setBids(self,marketValue):
        self.bidsToBuy =[]
        self.bidsToSell =[]

        if(len(self.lastFourBids)>4):
            if sorted(self.lastFourBids[-4:]):
                if self.funds>0:
                    self.bidsToBuy.append((self.funds//marketValue, marketValue))

                

            elif sorted(self.lastFourBids[-4:], reverse = True):
                if self.funds>0:
                    self.bidsToSell.append((self.numOwnedShares, marketValue))

               