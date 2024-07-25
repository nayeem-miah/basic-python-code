def function(a,b):
    sum=a+b
    print(sum)
function(10,40)

#same resule in lamda function & function
x=lambda a,b: a+b
print(x(10,40))


y=lambda a,b,c,d: (a+b)*(c-d)
print(y(10,20,10,5))

z=lambda x,y: x%y
print(z(10,50))