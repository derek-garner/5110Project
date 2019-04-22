from randomAgent import RandomAgent
from hodlAgent import HodlAgent
from RSIAgent import TrendingAgent

def createAgent(type,marketValue):
    if type =="Random":
        return RandomAgent(marketValue)

    if type =="Hodl":
        return HodlAgent(marketValue)

    if type =="RSI":
        return TrendingAgent(marketValue)