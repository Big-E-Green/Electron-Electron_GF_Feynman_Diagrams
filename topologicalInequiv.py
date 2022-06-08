from dd import *
from generator2 import *
from functions import *
import itertools
from copy import deepcopy
import timeit


def swap(translation,numm):
    cc=[]
    for i in translation: 
        c=0
        for j in numm:
            c=c+1
            if j==i:
                cc.append(c)
                if len(cc)==2:
                    return cc
                    
def reparam(trans,inp,numm):
    c=-1
    ii=deepcopy(inp)
    for k in inp:
        c=c+1
        c2=-1
        for q in k:
            c2=c2+1
            if q==trans[0]:        
                ii[c][c2]=trans[1]
            if q==trans[1]:
                ii[c][c2]=trans[0]
    sw=swap(trans,numm)
    ii[sw[0]],ii[sw[1]]=ii[sw[1]],ii[sw[0]]
    return ii


def distinctDiagrams(n):
    s=timeit.default_timer()
    gen=genny(n)
    nums=[]
    for i in gen:
        for j in i:
            nums.append(j)
    lev=list(itertools.combinations(nums,2))
    c=0
    cool=[]
    for i in lev:
        c=c+1
        if c<2:
            dunce=list(itertools.combinations(lev,c))
            cool.append(dunce)
    print(cool)
    conn=connectedDiagrams(n)
    connn=deepcopy(conn)
    for i in connn:
        tmp=i
        for j in cool:
            for k in j:
                c=0
                while c!=len(k):
                    for q in k:
                        gens=reparam(q,tmp,nums)
                        tmp=gens                                  
                        c=c+1
                        if c==len(k):
                            if gens in connn:
                                if gens!=i:
                                    connn.remove(gens)
    con2=deepcopy(connn)
    for i in con2:
        for j in lev:
            gens=reparam(j,i,nums)
            if gens in con2:                                        
                if gens!=i:
                    con2.remove(gens)
    st=timeit.default_timer()
    print('Time Inequiv:',st-s)
    return con2
#print(distinctDiagrams(4))
print(len(distinctDiagrams(2)))