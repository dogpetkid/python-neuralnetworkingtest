##Neural network

import csv
from math import *
import synapsereset

def sigmoid(x):
    return (1/(1+exp(-x))) #A logic curve
    ##return x/sqrt(1+x*x) #A algebraic curve

def rectify(x):
    if x>0:
        return x
    else:
        return 0

def nodeaverage(column,node,average=True):
    global syndata
    global nodedata
    sum = 0
    ##The sum is calculated by repetitivly taking a weight and multiplying by the node it connects from
    for outnodenum in range(numofnodes[column-1]):
        weight = syndata[column][node][outnodenum]
        val = nodedata[column-1][outnodenum]
        sum+= weight*val
    if average:
        return sum/len(range(numofnodes[column-1]))
    else:
        return sum


##Reads the file and gets the weights out of it
def readandparse():
    with open("syndata.csv","r") as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        strsyndata = []
        for row in reader:
            strsyndata.append(row)
    
    syndata=[]
    ##Change all the strings to arrays of integers
    for i1 in strsyndata:
        d1=[]
        for i2 in i1:
            d2=[]
            ##Changes the string into an array of strings
            i2 = i2[1:len(i2)-1]
            i2 = i2.split(", ")
            for i3 in i2:
                ##Changes the strings into integers
                i3 = float(i3)
                d2.append(i3)
            d1.append(d2)
        syndata.append(d1)
    return syndata
syndata = readandparse()

def train():
    global syndata
    cachesyndata = syndata[:]
    synapsereset.reset()
    syndata = readandparse()
    fitnessB = boxmain()
    if fitnessA < fitnessB:
        if (fitnessA+100- cachesyndata[0][0][1]) < fitnessB:
            ##Updates Genome number
            syndata[0][0][0] = cachesyndata[0][0][0] + 1
            syndata[0][0][1] = cachesyndata[0][0][1]
            synapsereset.update(syndata)
        else:
            ##Updates Species number
            syndata[0][0][0] = cachesyndata[0][0][0]
            syndata[0][0][1] = cachesyndata[0][0][1] + 1
            synapsereset.update(syndata)
    else:
        cachesyndata[0][0][1]+= .01
        synapsereset.update(cachesyndata)


# # # # # # # # # #

numofnodes = [4,4,4,8,4]
template = [([[1,1,1,1]],[1,0,0,0]),([[0,0,0,0]],[1,0,0,0]),([[1,0,0,1]],[0,1,0,0]),([[0,1,1,0]],[0,1,0,0]),([[1,0,1,0]],[0,0,1,0]),([[0,1,0,1]],[0,0,1,0]),([[0,0,1,1]],[0,0,0,1]),([[1,1,0,0]],[0,0,0,1])]
##nodedata = [[1,1,0,0]]
##wanteddata = [0,0,0,1]

# # # # # # # # # #
def templatechoose():
    from random import choice
    choose = choice(template)
    global nodedata
    global wanteddata
    nodedata = choose[0][:]
    wanteddata = choose[1][:]
templatechoose()


def boxmain():
    def nodein1():
        global nodedata
        node1 = []
        ##For each node, it finds it value (via the average and sigmoid in this case)
        for nodenum in range(numofnodes[1]):
            node = nodeaverage(1,nodenum)
            node = sigmoid(node)
            node1.append(node)
        nodedata.append(node1)
    
    def nodein2():
        global nodedata
        node2 = []
        for nodenum in range(numofnodes[2]):
            node = nodeaverage(2,nodenum)
            node = sigmoid(node)
            node2.append(node)
        nodedata.append(node2)
    
    def nodein3():
        global nodedata
        node3 = []
        for nodenum in range(numofnodes[3]):
            node = nodeaverage(3,nodenum)
            node = rectify(node)
            node3.append(node)
        nodedata.append(node3)
    
    def nodein4():
        global nodedata
        node4 = []
        for nodenum in range(numofnodes[4]):
            node = nodeaverage(4,nodenum,False)
            node = rectify(node)
            node4.append(node)
        nodedata.append(node4)
    
    nodein1()
    nodein2()
    nodein3()
    nodein4()
    print(nodedata)
    fitnesstester = []
    i = 0
    for test in nodedata[len(nodedata)-1]:
        fitnesstester.append(abs(test-wanteddata[i])/10)
        i+=1
    
    fitness = 0
    for test in fitnesstester:
        fitness+= test
    fitness = 1/fitness
    input("Fitness of network: " + str(fitness))
    return fitness

# # # # # # # # # #


fitnessA = boxmain()
input("If you tested this, hit X now, else if you are training this, continue...")
while True:
    print()
    train()
    if input("\n- - - - -\n").lower() == "stop":
        break
    templatechoose()
    fitnessA = boxmain()

# # # # # # # # # #
