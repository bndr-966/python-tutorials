# def total(cost, itmeQuantity, percent):
#     value=((cost* itmeQuantity)+(cost* itmeQuantity)* percent)
#      print(value)
# total(10,2,0.20) 

#calculet Quantity :
def itemQuantity( Quantity , cost): 
    totalquantity= Quantity*cost
    return totalquantity
    print(totalquantity)

# calculat VAT:

def vat(cost , persant):
    valuevat= cost * persant
    return valuevat
    print(valuevat)
# calculat Total:

def totalcost(Quantity , cost , persant):
    Total=itemQuantity(Quantity, cost) + vat(cost,persant)*Quantity
    print(Total)

totalcost(5,10,0.15)
