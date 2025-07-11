# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 09:49:24 2025
matrix print of file
@author: prasa
"""
from tabulate import tabulate
l_name=[]
f=open("E:\\filename.txt",'r') #file location
for i in f:
    w=i.split()
    l_name.extend(w)
f.close()

f=open("E:\sample2.txt",'r') #file location
l1=[]
for i in f:
    w=i.split()
    l1.extend(w)
f.close()
s1=set(l1)

f=open("E:\stopwords.txt",'r') #file location
l2=[]
for i in f:
    w=i.split()
    l2.extend(w)
f.close()
stp=set(l2)


print()
print()
print("Text file: sample2.txt")
data=[]
headers=["Filename","Total words","Common words","Percentage"]
for i in range(len(l_name)):
    l=[]
    a=l_name[i]
    f=open(a,'r')
    for i in f:
        w=i.split()
        l.extend(w)
    f.close()
    s2=set(l)
    a1=s1.difference(stp)
    a2=s2.difference(stp)
    common=a1.intersection(a2)
    union=a1.union(a2)
    len1=len(common)
    len2=len(union)
    p=(len1/len2)*100 
    data.append([a,len1,len2,p])
print(tabulate(data, headers=headers, tablefmt="grid"))