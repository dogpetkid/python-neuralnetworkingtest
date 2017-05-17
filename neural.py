##Neural network

import csv
from math import *
import synapsereset

def sigmoid(x):
    return (1/(1+exp(-x)))

def tanh(x):
    return 2*sigmoid(x) -1

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
    global fitnessA
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

        
def slopefind(address):
    


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
    def nodeinN(N):
        global nodedata
        nodeN = []
        ##For each node, it finds it value (via the average and tanh in this case)
        for nodenum in range(numofnodes[N]):
            node = nodeaverage(N,nodenum)
            node = tanh(node)
            nodeN.append(node)
        nodedata.append(nodeN)
    
    for i in range(1,5): nodeinN(i)
    print(nodedata)
    dataerror = 0
    i = 0
    for output in nodedata[len(nodedata)-1]:
        dataerror += abs(test-wanteddata[i])
        i+=1
    dataerror = dataerror/len(nodedata[len(nodedata)-1])
    
    fitness = 1/dataerror
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
    nodedata = None
    templatechoose()
    fitnessA = boxmain()

# # # # # # # # # #
