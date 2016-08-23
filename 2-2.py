'''
Peculiar balance
================
Can we save them? Beta Rabbit is trying to break into a lab that contains the only known zombie cure - but there's an
obstacle. The  door will only open if a challenge is solved correctly. The future of the zombified rabbit population is
at stake, so Beta reads the  challenge: There is a scale with an object on the left-hand side, whose mass is given in
some number of units. Predictably, the task is to  balance the two sides. But there is a catch: You only have this
peculiar weight set, having masses 1, 3, 9, 27, ... units. That is, one  for each power of 3. Being a brilliant
mathematician, Beta Rabbit quickly discovers that any number of units of mass can be balanced  exactly using this set.
To help Beta get into the room, write a method called answer(x), which outputs a list of strings representing where the
weights should be  placed, in order for the two sides to be balanced, assuming that weight on the left has mass x units.
The first element of the output list should correspond to the 1-unit weight, the second element to the 3-unit weight,
and so on. Each  string is one of:
"L" : put weight on left-hand side
"R" : put weight on right-hand side
"-" : do not use weight
To ensure that the output is the smallest possible, the last element of the list must not be "-".
x will always be a positive integer, no larger than 1000000000.
'''
import math

#Function creates list with all powers of 3 less then x
def LessPowerThreeList(x):
    powerList=[]
    powerofthree=0
    powerthree=0
    while powerthree<=x:
        powerList.append(int(math.pow(3, powerofthree)))
        powerofthree=powerofthree+1
        powerthree=int(math.pow(3,powerofthree))
    
    return powerList

#Function creates list with all powers of 3 less then x plus next power
def MorePowerThreeList(x):
    powerList=[]
    powerofthree=0
    powerthree=0
    while powerthree<=x:
        powerthree=int(math.pow(3,powerofthree))
        powerList.append(int(math.pow(3, powerofthree)))
        powerofthree=powerofthree+1 
    return powerList

#Function calculates sum of numbers in iList
def SumPowerThreeList(iList):
    sumofpowers=0
    for i in iList:
        sumofpowers=sumofpowers+i
    return sumofpowers

#Function defines on what side of scale should the weight be put
def DefSideOfScale(x):
    leftSiteScale=[]
    rightSiteScale=[]
    listOfPowers=[]
    while True:     
        leftsum=x
        for i in leftSiteScale:
            leftsum=leftsum+i
        rightsum=0
        for k in rightSiteScale:
            rightsum=rightsum+k
        if leftsum>rightsum:
            dif=leftsum-rightsum      
            if dif>SumPowerThreeList(LessPowerThreeList(dif)):
                listOfPowers=MorePowerThreeList(dif)
            else:
                listOfPowers=LessPowerThreeList(dif)
            rightSiteScale.append(listOfPowers[len(listOfPowers)-1])
        elif leftsum<rightsum:
            dif=rightsum-leftsum         
            if dif>SumPowerThreeList(LessPowerThreeList(dif)):
                listOfPowers=MorePowerThreeList(dif)
            else:
                listOfPowers=LessPowerThreeList(dif)
            leftSiteScale.append(listOfPowers[len(listOfPowers)-1])
        else:
            break
    return leftSiteScale, rightSiteScale


while True:
    line = input('Enter a number:')
    if line=='done':
        break
    try:
        x=int(line)
        leftscale, rightscale = DefSideOfScale(x)
        l=leftscale[0]
        r=rightscale[0]
        if l>r:
            maxweight=int(l)
        else:
            maxweight=int(r)

        k=0
        i=0
        while i<maxweight:
            i=int(math.pow(3,k))
            if i in leftscale:
                print("put ",i," on left-hand side")
            elif i in rightscale:
                print("put ",i," on right-hand side")
            else:
                print("do not use weight ",i)
            k=k+1
    except:
        print ("Invalid input")
                
