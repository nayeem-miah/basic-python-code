'''#write() method

#nayeem.html file open
wr=open("nayeem.html","w")
wr.write("<p>subsribe nayeem progammer </p> \n")

text=open("nayeem.html","a")
text.write("everything for alhamdullah \n")
text.write("hello")


#nayeem.text
wt=open("nayeem.text","w") #"w"=write()method
wt.write("tumii amake subscribe kro \n")

wri=open("nayeem.text","a")          # "a"=aponde method
wri.write(" my name is nayeem \n")   # \n=new lines
wri.write(" i am a single men \n")
wri.write("alhamdullah")


#read() method
tex=open("text.text","r") #"r"=file read
print(tex.read())'''



#dellate a file
import os
os.remove("nayeem.text") #remove this file

