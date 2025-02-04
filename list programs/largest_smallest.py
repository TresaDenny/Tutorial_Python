lst = []
n=int(input("Enter the number of elements: "))

for i in range(n):
    num=int(input(f"\nEnter the element {i+1}:"))
    lst.append(num)

lst.sort()
print(f"Largest element is :{lst[-1]}, smallest element is: {lst[0]}")