#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


n1=np.array([1,2,3,4,5,6])
n1


# In[3]:


type(n1)


# In[4]:


n2=np.array([[1,2,3,4],[5,6,7,8]])
n2


# In[5]:


type(n2)


# In[6]:


n3=np.zeros((1,2)) # 1 row and 2 columns for that we have used zeros() method
n3


# In[7]:


n4=np.zeros((5,5))
n4


# In[8]:


n5=np.full((2,2),4)#We used full() method first parametr for rows & col and second for num for duplicate same num
n5


# In[9]:


n6=np.arange(10,21)# arange() method used for showing numbers from that range not include last num 
n6


# In[10]:


n7=np.arange(10,50,5)#it will go towards 50 with gap for each as 5 and not include 50
n7


# In[12]:


n7=np.arange(2,20,2)
n7


# In[16]:


n9=np.random.randint(1,100,5) #random numbers using  random.randint() method
n9


# In[30]:


n8=np.array([[1,23,3],[45,44,4]]) # check the shape with shape() method
n8.shape


# In[32]:


n8.shape=(2,3) # changing the shape of arrray using shape() method
n8.shape


# In[28]:


n8


# In[29]:


n10=np.array([[1,2,3]])
n10.shape


# In[ ]:




