lst = []
n=int(input("Enter the number of elements: "))

for i in range(n):
    num=int(input(f"\nEnter the element {i+1}:"))
    lst.append(num)

lst.sort()
print("\nInput List=", lst)
print(f"\nThe third largest element is: ",lst.pop(-3))
