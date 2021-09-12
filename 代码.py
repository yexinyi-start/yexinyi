#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
odds=[ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
      21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
      41, 43, 45, 47, 49, 51,  53, 55, 57, 59 ]

right_this_minute = datetime.today().minute 

if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute")


# In[10]:


from datetime import datetime

import random
import time

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for i in range(5): # （若当前分钟数属于odds），会执行循环五遍的命令
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
            print("This minute seems a little odd.")
else:
    print("Not an odd minute.")
    wait_time = random.randint(1,60)
    time.sleep(wait_time)


# In[11]:


word = "bottles" # 创建变量并赋值
for beer_num in range(99,0,-1): # (即 开始，结束，步长) #beer_num 即 啤酒数量
    print(beer_num,word,"of beer on the wall.")
    print(beer_num,word,"of beer.") # 从 99 至 1
    print("Take one down.")
    print("Pass it around.") 
    if beer_num == 1: # 从这里开始实施 if 条件
        print("No more bottles of beer on the wall.")
    else:
        new_num = beer_num - 1 # 新的啤酒数量 = 啤酒数量 - 1 （除了数量为1，“99-1即98瓶啤酒在墙上”）
        if new_num == 1:
            word = "bottle"
        print(new_num,word,"of beer on the wall.")
        print() 


# In[ ]:




