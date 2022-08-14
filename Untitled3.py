#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Que01: write a python program to get the Fibonacci series between 0 to 50
# Answer: 
# fibonacci series
num1= int(input("Enter intial number of range:"))
num2= int(input("Enter final number of range"))
first= 0
second= 1
for kk in range(num1,num2):
    save= first
    first= second
    second= save + second
    print(first, end=" ")
    if second>num2:
        break


# In[ ]:





# In[ ]:




