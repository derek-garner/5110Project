from agent import Agent
import random


class HodlAgent(Agent):
    
    
	def __init__(self,marketValue):
		super(HodlAgent,self).__init__()
		self.idealBuyPrice = marketValue +  random.randint( -marketValue/10,0)
		self.idealSellPrice = marketValue + random.randint(0,marketValue/2)
		self.setBids(marketValue)
		self.agentType= "Hodl"


	def update(self,marketValue):
		self.idealBuyPrice = marketValue +  random.randint(-marketValue/10,0)
		self.idealSellPrice = marketValue + random.randint(0,marketValue)

		self.setBids(marketValue)

	def setBids(self,marketValue):
		self.bidsToBuy=[]
		self.bidsToSell= []
		if self.funds>0:
			self.bidsToBuy.append((self.numOwnedShares, marketValue))

		else:
			self.bidsToBuy=[]