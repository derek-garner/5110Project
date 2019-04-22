from randomAgent import RandomAgent
from hodlAgent import HodlAgent


def createAgent(type,marketValue):
    if type =="Random":
        return RandomAgent(marketValue)

    if type =="Hodl":
        return HodlAgent(marketValue)