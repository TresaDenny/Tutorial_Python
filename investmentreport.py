"""
Rate of Investment= (current value-investment value/investment value)*100
when printing print it to two decimal places (rate_of_interest:.2f)

=> .2 represents move two decimal places 
=>f represents floating point

"""

current=float(input("Enter the current value : "))
investment=float(input("\nEnter the investment value:"))

if investment==0:
    print("Investment value cannot be zero")
else :
    rate_of_interest=float((current-investment/investment)*100)    
    print(f"\nReturn of Investment : {rate_of_interest :.2f}%")



