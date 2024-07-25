import datetime
a=datetime.datetime.now()
print(a.strftime("%A"))
print(a.strftime("%m")) # %m=month  , %A=day
print(a) #date time



x=datetime.datetime.now()
print(x)
print(x.strftime("%B"))  #%B= month
print(x.strftime("%C")) # %C=censury
print(x.strftime("%d")) #%d=date

x=datetime.datetime.now()
print(x.strftime("%B"))