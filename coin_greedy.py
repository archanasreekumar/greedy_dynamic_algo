def find(amount,n):
	result=[]
	i=n-1
	while (i>=0):
		while(amount>=coins[i]):	
			amount=amount- coins[i]
			result.append(coins[i])
		i-=1

	
	print result
	print result #printing the list of coins
	print len(result) #printing the number of coins

print 'enter the no:of coins'
coin_number=input()
coins=[]
print 'enter the changes'
for i in range(coin_number):
	i=input()
	coins.append(i)
print 'enter the amount'
amount=input()
find(amount,coin_number)
