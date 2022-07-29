#!/usr/bin/env python
# coding: utf-8

# In[9]:


import math as mt
c=50
h=30
resultat=[]
final=[]
d=input("entrer plusieurs nombres separé par une virgule : ")
d=d.split(",")
print(d)
for i in d :
    tint=int(i)
    s=2*c*tint
    res=s/h
    res=mt.sqrt(res)
    resultat.append(res)
for i in resultat :
    i=int(i)
    strr=str(i)
    final.append(strr)
sep=","
fin=sep.join(final)
print(fin)


# In[ ]:




