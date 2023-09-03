#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import *
from sympy.plotting import plot
from random import uniform
init_printing()


# In[2]:


x = Symbol('x')
f = -18 * x ** 3 + 5 * x ** 2 + 10 * x - 30
f


# In[3]:


solveset(f, x, Reals).evalf(3)


# In[6]:


dif_list = [-oo, oo]
dif_list[1:1] = solveset(diff(f), x, Reals).evalf(3)
inc_list, dec_list = [], []
for i in range(1, len(dif_list)):
    if is_increasing(f, Interval.open(dif_list[i-1], dif_list[i])):
        inc_list.append((dif_list[i-1], dif_list[i]))
    else:
        dec_list.append((dif_list[i-1], dif_list[i]))
print('Возрастает', *inc_list)
print('Убывает', *dec_list)


# In[5]:


plot(f, (x, -1,1))


# In[28]:


dataset = sorted(solveset(diff(f), x, Reals).evalf(3))
dataset.insert(0, dataset[0]-1)

differ = diff(f)
func_stat_list = []

for index, value in enumerate(dataset):
    func_stat_list.append(differ.subs(x, uniform(value, dataset[index]+1)))
    if index != 0:
        if func_stat_list[index - 1] < 0 < func_stat_list[index]:
            print('Минимум', value, f.subs(x, value).evalf(3))
        elif func_stat_list[index - 1] < 0 < func_stat_list[index]:
            print('Максимум', value, f.subs(x, value).evalf(3))


# In[29]:


print('f > 0')
solveset(f>0, x, Reals).evalf(3)


# In[30]:


print('f < 0')
solveset(f<0, x, Reals).evalf(3)

