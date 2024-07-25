li=[1,3,5,"nayeem","Islam"]
print(li)
li[4]="SARJIL"
print(li)                 #LIST is muteable
lis=["saimum","mridul"]
print(lis[1])
list=[True,False,True]
print(type(list))

#ACCESS LIST ITEM
nayeem=["banana","mango","apple","orange"]
print(nayeem[3])

#change list
nayeem[3]="abdul basir"
print(nayeem)
print(nayeem[3])

#add list
nayeem.append(10) #append methode
print(nayeem)

nayeem.insert(4,23) #Insert methode
print(nayeem)

hablu=["webside","playstore",1123]
hablu.append("kobita")
hablu.insert(1,"firebox")     #  append  &  insert methode
hablu[3]="google"
print(hablu)

#remove() mathode
newlist=["anik","robi","santo",12,600]
newlist.remove(12)
print(newlist)

#pop() mathode remove the specfied index :
newlist=["anik","robi","santo",12,600]
newlist.pop(1)
print(newlist)
newlist.pop()
print(newlist)
#the del keyward remove the specfied index :
newlist=["anik","robi","santo",12,600]
del newlist[0]
print(newlist)


#clear the list
asfif=[12,13,15]
asfif.clear()
print(asfif)

#you can loop throught list item by using a for loop:
looplist=["adnan","azhari","asif","mamunul"]
for islamic_speaker in looplist:
    print(islamic_speaker)
    #range()&len() function
for i in range(len(looplist)):   #index number
    print(i)

#you can loop throught list item by using a while loop:
looplist=["adnan","azhari","asif","mamunul"]
y=0
while y<len(looplist):
    print(looplist[y])
    y=y+1

er=[12,23,45,67]
i=0
while i<3:
    print(er[i])
    i=i+1

#list COMPRTEHENSON :
NUM=[1,2,3,4,5]
#for i in NUM:
    #print(i*2)
k=[i*2 for i in NUM]
print(k)
z=[i**2 for i in NUM]
print(z)
j=[i+4 for i in NUM]
print(j)


#sort list
number=[1,4,2,5,7,6,8,5]
number.sort()
print(number) #searial mantain kora

eng=["s","a","e","b"]
eng.sort()
print(eng)

#rb=[1,2,3,4,5,6]
numb.sort(reverse=True)
print(numb)
everse list
num

#python copy()list
NUm=[1,2,8,6,5,4]
NUm1=NUm.copy()
print(NUm1)
print(NUm)

#PYTHON JOIN LIST
LIST1=[1,3,9,7]
LIST2=[2,5,6,8]
#LIST3=LIST1+LIST2
#print(LIST3)
LIST1.extend(LIST2)
print(LIST1)

list1=["kamal","jamal"]
list2=["sakib","rakib"]
list1.extend(list2)
print(list1)
