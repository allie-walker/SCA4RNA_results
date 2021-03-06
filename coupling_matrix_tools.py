# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:36:47 2020

@author: allison
"""

def readATS(filename):
    infile = open(filename)
    ats = []
    for line in infile:
        ats.append(line.replace("\n",""))
    infile.close()
    return ats

def readCouplingMatrix(filename):
    infile = open(filename)
    Csca = []
    i = 0
    for line in infile:
        Csca.append([])
        entries = line.split(",")
        entries = entries[0:len(entries)-1]
        for v in entries:
            Csca[i].append(float(v))
        i+=1
    return Csca

def getPairwiseCouplingValues(Csca, ats):
    coupling_values = []
    for i in range(0, len(ats)):
        for j in range(i+1, len(ats)):
            coupling_values.append(Csca[i][j])
    coupling_values.sort()
    return coupling_values

def getCouplingInfo(pos1, pos2):
    ats = readATS("Data/ats.txt")
    if str(pos1) not in ats:
        return (None, 1)
    if str(pos2) not in ats:
        return (None, 2)
    
    Csca = readCouplingMatrix("Data/SCA_matrix.csv")
    coupling_values = getPairwiseCouplingValues(Csca, ats)
    index1 = ats.index(str(pos1))
    index2 = ats.index(str(pos2))
    coupling = Csca[index1][index2]
    first_index = coupling_values.index(coupling)
    last_index = len(coupling_values) - 1 - coupling_values[::-1].index(coupling)
    if first_index == -1:
        return (coupling, -1)
    percentile = 100.0*(first_index+last_index)/(2*len(coupling_values))
    return (coupling, percentile)

#position1 = 4
#position2 = 11
#(coupling, percentile) = getCouplingInfo(position1,position2)