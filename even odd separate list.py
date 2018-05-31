EVEN=[]
ODD=[]
b=[]
a=int(input("Enter number of elements: "))
for i in range(a):
  items=int(input("Enter a number:"))
  b.append(items)
print(b)
for num in b:
  if (num%2)==0:
    EVEN.append(num)
  else:
    ODD.append(num)
print(EVEN)
print(ODD)
    
