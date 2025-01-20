"""
enter a binary number
initialize decimal and initial power to zero

look into the binary number and reverse it 
=>binary[::1]
=>eg: 10011
    rev= 11001
    first digit is 1
eg: in for loop(digit=1)
       {
            decimal=0+1*2^0
       }    


"""
binary = input("Enter a binary number: ")
decimal = 0
power = 0

for digit in binary[::-1]:  
    decimal = decimal+ int(digit) * (2 ** power)
    power= power+1

print("The decimal equivalent of", binary,"is",decimal)