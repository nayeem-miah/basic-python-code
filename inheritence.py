#multiple inheritence
class baba:
    car="BMW"
    tk="1000k"
    home="10 floor"

class kaka(baba): #baba k call kora hoice
    brokenphon=""
    brokenhome=""

k=kaka()
print(k.car)
print(k.tk)

class student:
    study="6 hours"
    exam="first resula of a school"
class rahat(student):
    boy="good boy"
y=rahat()
print(y.boy)
print(y.study)
print(y.exam)




#MULTIPLE INHERETEMC :
class nayeem:
    phone="i phone"
    laptop="lenovo"

class basir:
    book="all department book"
    tk="100k"

class remen:
    bike="4B"
    smartphonr="redmi"

class santo(nayeem,basir,remen):
    brokenphone=" samsung"
    brokencaar="tata"

A=santo()
print(A.tk)
print(A.phone)
print(A.brokencaar)
print(A.smartphonr)



#MULTILEVEL INHERETENCE :
class father:
    home="10 floor"
    tk="1B"

class son1(father):
    phone="iphone"
    laptop="hp"

class son2(son1):
    dextop="samsung"
    microphone="g7"

class son3(son2):
    old="18"
    wight="50kg"

m=son3()
print(m.dextop)
print(m.tk)

n=son2()
print(n.laptop)