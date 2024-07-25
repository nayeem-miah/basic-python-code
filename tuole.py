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


#unpack tuple
fruts=("apple","banana","cherry")
a,b,c=fruts
print(c)
(a,*b)=fruts
print(b)
(*b,a,c)=fruts
print(b)

#tuple loop
name=("abdullah","muhammed",("alamim"))
for i in name:
    print(i)
                      #for loop tuple
for x in range(len(name)):
    print(name[x])
#while loop
j=0
while j<len(name):
    print(name[j])
    j+=1
print("end ")

#join tuple
num1=(1,3,5,6)
num2=(2,7,8,9)

num3 = num1+num2
print(num3)

print(num3*2)

#tuple methode
number=num3 #num3=(1, 3, 5, 6, 2, 7, 8, 9)
print(number.index(9))#index number
#count methode
fruts=("apple","banana","cherry","apple","banana","cherry")
print(fruts.count("apple"))

#excercies tuple
num=("santo","absulbasir","ahammed")#print the first item
print(num[0])
#print the number of item in the num
print(len(num))
#negative indexind last item in the tuple
print(num[-1])
#use a range of index to print the third fourth and fifth item
fruts1=("apple",12,34,"banana",45,"kiwi")
print(fruts1[2:5])