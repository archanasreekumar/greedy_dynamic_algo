#python2 filename.py

def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] #creating matrix with extra row and column
    #print K
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0#assigning 0's to extra row column
            #considering the max value(using recursion formula)
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 
  
#driver function
val=[]
val1=0
wt=[]
wt1=0
W=0
print 'enter the no:of items'
items=input()
print 'enter the values'
for i in range(items):
    val1=input()
    val.append(val1)#list of values
#val = [10, 40, 30, 50] 
print 'enter the weights'
for i in range(items):
    wt1=input()
    wt.append(wt1)#list of weights
#wt = [5, 4, 6, 3]
print 'enter the max weight'
W =input()
# W=10
n = len(val) 
print'maximum value that can be put in a knapsack of capacity '+str(W)+' is '+str((knapSack(W, wt, val, n)))
  

