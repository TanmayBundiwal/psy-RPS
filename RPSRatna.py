#!/usr/bin/env python
# coding: utf-8

# In[19]:


import random as r
#import numpy as np
r.seed()


# In[20]:


moves = ( 
        (1,'Rock') , 
        (2,'Paper') ,
        (3,'Scissors')
)

outcome = ['Draw','Win!','Lost']

Wins = 0

last_state = [0,0,0]        #win/loss,pc_move,user_move


# In[21]:


print('Welcome to Rock, Paper and Scissors by Ratnasambhav!');


# In[22]:


def result(pc,user):
    if(user==pc):
        return 0
    elif(user == pc%3+1):
        return 1
    else:
        return -1


# In[23]:


def playfirst():
    print ( 'Enter 1 for Rock, 2 for Paper, 3 for Scissors.' )
    user_move = input()
    pc_move = moves[r.randint(0,2)]
    res = result(int(pc_move[0]),int(user_move))
    print('PC move: '+pc_move[1]+'\nResult: '+outcome[res])
    global Wins
    if(res==1): Wins +=1
    global last_state
    last_state = [res,pc_move[0],int(user_move)]
    #print(last_state)


# In[24]:


def get_third(n):
    if (n==1): return 3
    else:      return (n+2)%3
    


# In[25]:


def getPCmove(ls):
    if(ls[0]==1):
        return moves[ls[2]-1]  #choose the user's choice
    else:
        return moves[get_third(ls[2])-1]  #choose what would lose to user's choice


# In[26]:


def play():
   print ( 'Enter 1 for Rock, 2 for Paper, 3 for Scissors.' )
   user_move = input()
   global last_state
   pc_move = getPCmove(last_state)
   res = result(int(pc_move[0]),int(user_move))
   print('PC move: '+pc_move[1]+'\nResult: '+outcome[res])
   global Wins
   if(res==1): Wins +=1
   last_state = [res,pc_move[0],int(user_move)]


# In[29]:


playfirst()
for i in range(4):
    play()
print ('Number of Wins: '+ str(Wins))


# In[ ]:




