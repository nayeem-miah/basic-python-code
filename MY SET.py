myset={1,3,4,6,"3"}
print(myset)#ome item sceond time did not suppot
print(type(myset))
#print(len(myset))

#access set item
for i in myset:
    print(i)
print("3"in myset)

#add set item
myset1={"hablu","nayeem","vai","sakib"}
myset1.add("mama")
print(myset1)

#remove set item
myset3={1,2,3,4,5,6}
print(myset3)
myset3.remove(6)
print(myset3)

#discard mathode
myset4={"nayeem","riad","habibur"}
myset4.discard("nayeem")
print(myset4)
myset4.discard(11)
print(myset4)#remove =update  but kuno item jodi na takha tahole print korbo

#pop()methode
myset3={1,2,3,4,5}
myset3.pop()#set a index number show kora na
print(myset3)
#clear()methode
myset3.clear()
print(myset3)

#for loop in my set
friend={"ashraful","jibon","nayeem","saimum"}
for i in friend:
    print(i)

#join two set
#union() methode
set1={"nayeem","saimum"}
set2={"mridul","mahadi"}
c=set1.union(set2)
print(c)

#update() set
myset2={"hablu","nayeem","vai","sakib"}
set3={1,2,3,4}
list1=[10,12,23,45]
myset2.update(set3)
print(myset2)

myset2.update(list1)
print(myset2)#list change by set




#set excercics
fruts={"apple","banana","cherry"}
print("apple"in fruts)

#use the add()methode to add "orange" t the fruts set
fruts={"apple","banana","cherry"}
#fruts.add("orange")
# add to fruts add more fruts
morefruts={"mango","orange"}
fruts.update(morefruts)
print(fruts)
#use the remove mathode remove to "banana"
fruts={'apple', 'banana', 'orange', 'cherry', 'mango'}
fruts.remove('banana')
print(fruts)

#use the discard mathode remove to "apple"
fruts={'orange', 'apple', 'cherry', 'mango'}
fruts.discard("apple")
print(fruts)