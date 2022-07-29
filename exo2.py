#!/usr/bin/env python
# coding: utf-8

# In[8]:


def fact(n) :
    if (n==0 or n==1) :
        return 1
    else :
        return (n*fact(n-1))
nbr=int(input("entrer un nombre : "))
f=fact(nbr)
print("le factoriel de ",nbr," est :",f)


# In[ ]:





# In[ ]:




