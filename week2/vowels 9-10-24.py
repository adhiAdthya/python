str=input("enter the string:")
vowels="aeiouAEIOU"
v=[]
for i in str:
    for j in vowels:
        if i==j:
            v.append(i)
print("vowels present in string",str,"=",v)
