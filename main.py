import matplotlib.pyplot as plt
from randomAgent import RandomAgent
import matplotlib.animation as animation
from matplotlib import style
import agentFactory
import math
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
plt.plot([1,2,3], label="test1")
plt.plot([3,2,1], label="test2")
agents = []
bidsToBuy = []
bidsToSell = []
numAgents = 100
buyPriceBook = [0]*5000 
sellPriceBook = [0]*500*numAgents 
marketValue =250
marketShares =1000;

# ================Create agents =======================

# Situation One lots of HODL agents mixed evenly with random
#TEST 1
for i in range (0,numAgents):
    
    testAgent = agentFactory.createAgent("Random",marketValue)
    agents.append(testAgent)


'''
      if i %2== 0:
        testAgent = agentFactory.createAgent("Random",marketValue)
    else:
        testAgent = agentFactory.createAgent("Hodl",marketValue)
    agents.append(testAgent)
# Situation One lots of HODL agents mixed evenly with random
'''


# ================Create agents =======================





#==============Animate Graph Loop=====================
def animate(i):
    global buyPriceBook
    global marketShares
    global marketValue 
    getCurrentBids()
    marketValue = getMarketPrice()
    print ("Current market shares:  ",marketShares,"\n")
    print("Current market price:  ",marketValue,"\n")

    ax1.clear()

    xs1 = []
    ys1 = []
    for i in range (1, len(buyPriceBook)):           
       
        if(buyPriceBook[i]!=0):
            ys1.append(i)
            xs1.append(buyPriceBook[i])

    ax1.plot(xs1,ys1, label = "Demand")


    xs2 = []
    ys2 = []
    for i in range (1, len(sellPriceBook)):           
       
        if(sellPriceBook[i]!=0):
            ys2.append(i)
            xs2.append(sellPriceBook[i])

    ax1.plot(xs2,ys2,label = "Supply")
    plt.ylabel('Price')
    plt.xlabel('Quantity')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    updateMarket()
    getCurrentBids()

#==============Animate Graph=====================

#==============Distance function to find point lines intersect=================
def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def getCurrentBids():
    global buyPriceBook
    global sellPriceBook
    global agents
    buyPriceBook = [0]*5000 
    sellPriceBook = [0]*500*numAgents 
    for i in  range(0,len(agents)):    
        for bid in agents[i].getBidsToBuy():
            buyPriceBook[bid[0]]+=bid[1]


        for bid in agents[i].getBidsToSell():
            if(agents[i].numOwnedShares>=10):
                sellPriceBook[bid[0]]+=bid[1]
            
            
#==============Distance function to find point lines intersect=================

# Determine current market price
def getMarketPrice():
    global marketValue
    global buyPriceBook
    global sellPriceBook
    validBuyOrders=[]
    validSellOrders = []

    for i in range(0,len(buyPriceBook)):
        if(buyPriceBook[i]!=0):
            validBuyOrders.append((i,buyPriceBook[i]) )

    for i in range(0,len(sellPriceBook)):
        if(sellPriceBook[i]!=0):
            validSellOrders.append((i,sellPriceBook[i]) )    
            
    minDist = math.inf
    for i in validBuyOrders:
        for j in validSellOrders:
            dist =distance(i,j)
            if(dist< minDist):
                minDist = dist
                closestI= i
                closestJ= i
    

    return (closestI[0] +closestJ[0]) /2

# Determine current market price







def updateMarket():
    global marketShares
    marketValue=int(getMarketPrice())
    for agent in agents:
        marketShares+=agent.sellShares(marketValue)
        marketShares-=agent.buyShares(marketShares,marketValue)
        agent.update(marketValue)





ani = animation.FuncAnimation(fig, animate, interval =1000)
plt.show()

HighestValue=0 
for agent in agents:
    if(agent.getTotalAssets(marketValue)>HighestValue):
        print(marketValue)
        HighestValue=agent.getTotalAssets(marketValue)




