# []=set of charectars
import re
text="The Rain in spain"
pattern="[A-Z]" #[]=set of charectars
a=re.findall(pattern,text)
print(a)

import re
line=" 1 i am a student.2 of class 19"
#"[1-9]"
x=re.findall("[1-9]",line)
print(x)

import re
line=" 1 i am a student.2 of class 19"
pe="[a-s]"
p=re.findall(pe,line)
print(p)


# ^ = meta characters=first item print
import re
text1="1 is special  charactars"
y="^1" # ^ = meta characters=first item print
z=re.findall(y,text1)
if z:
    print("yes,1 is special charactars")
else:
    print("no,1 is not special charactars")


# $=last item print korbe
import re
tx="there are member of 5"
d=re.findall("5$",tx)
if d:
    print("yes,5 is tx")
else:
    print("not match")


import re
tex="1 is charectars special"
petren="special$" # $=last item print korbe
m=re.findall(petren,tex)
if m:
    print("yes, we finf specal charectars")
else:
    print("no,we definf specal charectars")