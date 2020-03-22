#!/usr/bin/env python
# coding: utf-8

# In[32]:


import random as r
import numpy as np
r.seed()


# In[33]:


moves = ( 
        (1,'Rock') , 
        (2,'Paper') ,
        (3,'Scissors')
)

outcome = ['Draw','Win!','Lost']

Wins = 0


# In[34]:


print('Welcome to Rock, Paper and Scissors!');


# In[35]:


def result(pc,user):
    if(user==pc):
        return 0
    elif(user == pc%3+1):
        return 1
    else:
        return -1


# In[36]:


def play():
    print ( 'Enter 1 for Rock, 2 for Paper, 3 for Scissors.' )
    user_move = input()
    pc_move = moves[r.randint(0,2)]
    res = result(int(pc_move[0]),int(user_move))
    print('PC move: '+pc_move[1]+'\nResult: '+outcome[res])
    global Wins
    if(res==1): Wins +=1


# In[37]:


for i in range(5):
    play()
print ('Number of Wins: '+ str(Wins))


# In[ ]:




