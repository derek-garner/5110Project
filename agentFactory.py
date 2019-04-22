from randomAgent import RandomAgent
from hodlAgent import HodlAgent
from TrendingAgent import TrendingAgent
from TrendingAgent import TrendingAgent
from NonParticipatingAgent import NonParticipating

def createAgent(type,marketValue):
    if type =="Random":
        return RandomAgent(marketValue)

    if type =="Hodl":
        return HodlAgent(marketValue)

    if type =="Trending":
        return TrendingAgent(marketValue)

    if type =="NonParticipating":
        return NonParticipating(marketValue)


