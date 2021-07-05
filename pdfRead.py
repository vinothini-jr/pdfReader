import PyPDF2
import re
import urllib.request
import io

memoryfile=open(filename,'rb')
object=PyPDF2.PdfFileReader(memoryfile)
num=object.getNumPages()
print(num)
string=input('enter word')
for i in range(0,num):
    pageob=object.getPage(i)
    text=pageob.extractText()
    if re.search(string,text):
        print("found at ",i+1)