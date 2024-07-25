#access tuple
newtuple=(12,34,"nayeem",23,"HABLU")
print(type(newtuple))
print(newtuple[1])

#negetive indexing
print(newtuple[-1])
print(newtuple[-3])

#RANGE OF INDEXING
print(newtuple[1:4])
print(newtuple[0:3])
print(newtuple[0:5]) #(0 theki suru hole last item pojonto print korar jonno index number theki 1 + korta hobe

#update tuple
thistuple=("nayeem","akram","vai")
print(type(list(thistuple)))
a=list(thistuple)
a.append("jibon")
print(a)
thistuple=tuple(a)
print(thistuple)

tuple1=(12,23,4,5)
 #x=list(tuple1)    exchange tuple=list
print(type(list(tuple1)))
x=list(tuple1)
x.append("ali")
tuple1=tuple(x)#list to tuple convart
print(tuple1)

#for loop in tuple
tuple2=(12, 23, 4, 5, 'ali')
for i in tuple2:
    print(i)
#join two tuple
tuple2=(12, 23, 4, 5, 'ali')
tuple3=(12,45,78)
x=tuple2+tuple3
print(x)