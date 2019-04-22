import abc


class Agent(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def __init__(self):
        self.bidsToBuy =[]
        self.bidsToSell =[]
        self.numOwnedShares =500
        self.funds = 100000
        self.maxBuyPrice =5000

    def getBidsToBuy(self):
        return self.bidsToBuy

    def getBidsToSell(self):
        return self.bidsToSell

    @abc.abstractclassmethod
    def setBids(marketPrice):
        return

    def getTotalAssets(self,marketValue):
        return self.funds + (marketValue * self.numOwnedShares)

    def buyShares(self,marketShares,marketPrice):
        for bid in self.bidsToBuy:
            if bid[1] == marketPrice:
                if(bid[0]<marketShares):
                    self.numOwnedShares+=bid[0]
                    self.funds-= bid[0]*bid[1]
                    print("Buying",bid[0])
                    print(self.numOwnedShares)
                    return bid[0]

                else:
                    print("Buying",marketShares)
                    print(self.numOwnedShares)
                    self.numOwnedShares+=marketShares
                    self.funds-= marketShares*bid[1]
                    return marketShares

        return 0


    def sellShares(self,marketPrice):
        if(self.numOwnedShares<0): print("ERROR")
        for bid in self.bidsToSell:
            if bid[1] == marketPrice:
                self.numOwnedShares-=bid[0]
                self.funds+= bid[0]*bid[1]
                return bid[0]
    
        return 0
























