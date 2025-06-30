

#calcultes total cost for all items without vat
def itemQuantity(numberOfItems, cost): 
    totalItemCost=numberOfItems*cost
    return totalItemCost

#function calculates Vat only
def vat(cost, percent):
    value= cost * percent
    return value


##THis function calculates total cost
def totalCost(numberOfItems,cost, percent):
   total= itemQuantity(numberOfItems, cost) + vat(cost, percent)* numberOfItems
   print (total)

totalCost(2 ,10, 0.20) 