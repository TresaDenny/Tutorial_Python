"""Write a python program to take a list of integers. 
Create another list to store all the even numbers from the master list and print the new list contents in ascending order """

master_lst=[]
while True:
    num=int(input("Enter a number:"))
    master_lst.append(num)
    ch=input("Do you want to continue (Y/N):")
    if ch!='Y':
        break

print(master_lst)
new_lst=[]
for element in master_lst:
    if element % 2 == 0 :
            new_lst.append(element)
new_lst.sort()
print("\n New list :" ,new_lst)

