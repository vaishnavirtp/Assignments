#!/usr/bin/env python
# coding: utf-8

# In[13]:


def SumUsingFunction(numbers):
    sumn = 0
    addition = sum(numbers)
    return addition


# In[14]:


SumUsingFunction([2,3,2])


# In[15]:


def SumDirect(numbers):
    sumn = 0
    for i in numbers:
        sumn += i
    return sumn


# In[16]:


SumDirect([2,3,1,3,1])


# In[ ]:




