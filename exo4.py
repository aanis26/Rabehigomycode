#!/usr/bin/env python
# coding: utf-8

# In[1]:


l=[]
mot=input("donnez n'importe quelle mot : ")
index=input("donnez un nombre : ")
index=int(index)
if (index<0 and index >= len(mot)) :
    print("erreur !!!")
else :
    for i in mot :
        l.append(i)
    del l[index]
mot=""
for i in l :
    mot=mot+i
print(mot)


# In[ ]:




