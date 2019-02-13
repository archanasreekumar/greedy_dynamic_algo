#python2 filename.py
def recDC(coinValueList,change,knownResults):
   minCoins = change
   #if the amount itself if present among values then return 1
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
      #recursive calls for each different coin value 
      #less than the amount of change we are trying to make
   else:
      for i in [c for c in coinValueList if c <= change]:
       #for i in coinValueList:
         #if c <= change:
         
         # print c
         # print str(i)+'hi'
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            #adding te result to the list ' knownResults'
            knownResults[change] = minCoins
   return minCoins
#driver function
print "enter the no:of coins"
n=input()
coinValueList=[]
#creating a list of coins
print "enter values"
for i in range(n):
   i=input()
   coinValueList.append(i)
print "enter the amount"
change=input()
print(recDC(coinValueList,change,[0]*(change+1)))