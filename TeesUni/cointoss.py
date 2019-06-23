import random

Outcomes= []
headrun=[0,]
tailrun=[0,]
TCount=0
HCount=0

def coinToss ():
  outcome = random.randint(1,2)
  if outcome == 1:
      return "T"
  else:
      return "H"



def hundred():
  n=0
  while n<100:
    Outcomes.append(coinToss())  
    n=n+1

hundred()
print(Outcomes)

for o in range(0, len(Outcomes), 20):
    print(''.join(Outcomes[o:o+20]))


for o in range(0, len(Outcomes), 1):
    
    if Outcomes[o]=='H':
            headrun[TCount] = (headrun[TCount]+1)
            if Outcomes[o] != Outcomes[o-1]:
                tailrun.append(0)
                HCount = HCount+1
    elif Outcomes[o]=='T':
        tailrun[HCount] = (tailrun[HCount]+1)
        if Outcomes[o] != Outcomes[o-1]:
            headrun.append(0)
            TCount = TCount+1

print(headrun)

print(tailrun)
print("The longest run of heads is ", str(max(headrun)),
                                          " and the longest tail run is ", str(max(tailrun)))        
    
    
