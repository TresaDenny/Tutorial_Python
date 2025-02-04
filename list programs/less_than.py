"""Write a python program to take a list of integers. 
Create another list with those numbers in the master list that are less than a number entered by the user. Print the new list contents."""

master_lst=[]
while True:
    num=int(input("Enter a number:"))
    master_lst.append(num)
    ch=input("Do you want to continue (Y/N):")
    if ch!='Y':
        break

print(master_lst)
new_lst=[]
n=int(input("Enter a number to filter:"))
for element in master_lst:
    if(element<n):
        new_lst.append(element)

print("/n New List: ",new_lst)