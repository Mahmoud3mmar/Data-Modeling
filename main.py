

import pandas as pd
import  random


def CalculateCumProb(Prob):
    CumProb = []
    for i,prob in enumerate(Prob):
        if i == 0:
            CumProb.append(float(prob))

        else:
            CumProb.append(CumProb[i-1] + float (prob))


    return CumProb


def CalculateRange(CumProb):
    RangeStart = []
    RangeEnd = []


    for i,prob in enumerate(CumProb):
        if i == 0:
            RangeStart.append(1)
            RangeEnd.append(int(prob * 100))

        else:
            RangeStart.append(RangeEnd[i-1] +1)
            RangeEnd.append (int ((prob * 100)))


    return RangeStart,RangeEnd


def RandomNumbersDemandFinder(randomNums,Rstart,Rend,demands):
    Demand = []
    for rand in randomNumbs:
        for i, start in enumerate(Rstart):
            if rand >= start and rand < Rend[i]:
                print(start , " - " ,Rend[i] )


                Demand.append(int(demands[i]))
                break
    print("Calculated demand" , Demand)

# Define variable to load the wookbook

table = pd.read_excel (r'Test (2) (3).xlsx' )



Demands = table["Demand"]
ProbOfDemandLevel = table ["Prob."]


R1,R2 = CalculateRange(CalculateCumProb(ProbOfDemandLevel))


print("Range start" ,R1)
print("Range   end" ,R2)
MaxRandom = int (R1[-1])
randomNumbs = []

for i in range(0, 10):
    randomNumbs.append(random.randint(0, MaxRandom))

print("Random numbers :" ,randomNumbs)


RandomNumbersDemandFinder(randomNumbs,R1,R2,Demands)
