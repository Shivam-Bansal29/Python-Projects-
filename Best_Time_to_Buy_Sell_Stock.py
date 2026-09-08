# Best Time to Buy and Sell Stock
prices =[1,2]
purchase = prices[0]
profit = 0 
for i in range(1,len(prices)):
        print(85)
        if(prices[i]<purchase):
                purchase = prices[i]
        
        cprofit = prices[i+1] - purchase
        
        if(cprofit > profit):
                profit = cprofit
        
print(prices)
print(profit)

