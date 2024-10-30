limit=int(input("enter limit:\n"))
first=0
second=1
third=1
print("Fibonocci series upto",limit,"is:")
print(first,end="")
for i in range(limit):
      print(third,end='')
      third=first+second
      first=second
      second=third
      
