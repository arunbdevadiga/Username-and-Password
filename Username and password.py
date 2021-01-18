#!/usr/bin/env python
# coding: utf-8

# # username and password login with 4 attemptes

# In[16]:


username="Arun" 
password="1234"

print('Enter correct username and password to login')

count=0
while count<4:
    Username=input("Enter your username:  ")
    Password=input("Enter your password:  ")
    if Username==username and Password==password:
         print("login succesfully, welocme")
         break
    
    if Username!=username:
        print("wrong username tryagain ")
        count+=1
    elif Password!=password:
        print("wrong password try again")
        count+=1
    
else:
    print("you reached maximum level you are blocked")


# In[ ]:





# In[ ]:





# In[ ]:




