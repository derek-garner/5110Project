import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import agentFactory
import math
import random
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



# ================Create agents =======================

#===================Demonstration Test Cases====================
def TestCase1():
    global agents
    for i in range (0,numAgents):
        testAgent = agentFactory.createAgent("Random",marketValue)
        agents.append(testAgent)



def TestCase2():
    global agents
    for i in range (0,numAgents):
        if i %2== 0:
            testAgent = agentFactory.createAgent("Random",marketValue)
        else:
            testAgent = agentFactory.createAgent("Hodl",marketValue)
        agents.append(testAgent)



def TestCase3():
    global agents
   
    choices = ["Random","Hodl","Trending","NonParticipating"]
    for i in range (0,numAgents):
        testAgent = agentFactory.createAgent(choices[random.randint(0,3)],marketValue)
        agents.append(testAgent)


def TestCase4():
    global agents
    for i in range (0,numAgents):
        if i %2== 0:
            testAgent = agentFactory.createAgent("Random",marketValue)
        else:
            testAgent = agentFactory.createAgent("Hodl",marketValue)
        agents.append(testAgent)


#===================Demonstration Test Cases====================



#==============Animate Graph Loop=====================
def animate(i):
    global buyPriceBook
    global marketShares
    global marketValue 
    getCurrentBids()
    marketValue = getMarketPrice()
    print ("Current market shares:  ",marketShares,"")
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
    closestI=[]
    closestJ=[]

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
    
    if(len(closestI)>0 and len(closestJ)>0):
        return (closestI[0] +closestJ[0]) /2

    else: return marketValue

# Determine current market price



def updateMarket():
    global marketShares
    marketValue=int(getMarketPrice())
    for agent in agents:
        marketShares+=agent.sellShares(marketValue)
        marketShares-=agent.buyShares(marketShares,marketValue)
        agent.update(marketValue)



TestCase3()

ani = animation.FuncAnimation(fig, animate, frames =15, interval =1000)
plt.show()

HighestValue=0 
agentTypeHighest=""
for agent in agents:
    if(agent.getTotalAssets(marketValue)>HighestValue):
        HighestValue=agent.getTotalAssets(marketValue)
        agentTypeHighest = agent.agentType

print("Most successful agent is type:",agentTypeHighest," \nTotal assets of most successful agent worth", HighestValue )

