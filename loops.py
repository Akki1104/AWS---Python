#python programe to illistrate
#Iterating over a List
print("List Iteration")
l = ["geek","for","geeks"]
for i in l:
    print(i)


#Iterating over a Tuple
print("\nTuple Iteration")
t = ("geek","for","geeks")
for i in t:
    print(i)

#Iteration over a Dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 154
for i in d:
    print("%s %d"%(i,d[i]))

#Iteration over a Set
print("\nSet Iteration")
set1 = {1,2,3,4,5,6}
for i in set1:
    print(i)