from random import *
import csv
##Reset synapses weights...

seed(random())
##Put in the number of nodes in each row (including the input row)
numofnodes = [4,4,4,8,4]

def reset():
    with open('syndata.csv', 'w', newline='') as csvfile:
        syn = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        c = 0
        ##Each column is its own row on the csv
        for nodecolumn in numofnodes:
            weightcolumn = []
            if c == 0:
                c+=1
                ##Is the needed blank column + serves as the genome/species counter
                weightcolumn.append([1,1])
                syn.writerow(weightcolumn)
                continue
            n = 0
            ##Each weight connects from the current node to...
            for nodenum in range(nodecolumn):
                nodeconnections = []
                ##a previous node.
                for previousnode in range(numofnodes[c-1]):
                    weight = random()*2-1
                    nodeconnections.append(weight)
                weightcolumn.append(nodeconnections)
                n+=1
            syn.writerow(weightcolumn)
            c+=1

def update(data):
    version = data[0]
    with open('syndata.csv', 'w', newline='') as csvfile:
        syn = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        c = 0
        ##Each column is its own row on the csv
        for nodecolumn in numofnodes:
            weightcolumn = []
            if c == 0:
                c+=1
                ##Is the needed blank column + serves as the genome/species counter
                syn.writerow(version)
                continue
            n = 0
            ##Each weight connects from the current node to...
            for nodenum in range(nodecolumn):
                nodeconnections = []
                ##a previous node.
                p = 0
                for previousnode in range(numofnodes[c-1]):
                    weight = data[c][n][p]
                    nodeconnections.append(weight)
                    p+=1
                weightcolumn.append(nodeconnections)
                n+=1
            syn.writerow(weightcolumn)
            c+=1

if __name__ == "__main__":
    reset()