#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import *
from sympy.plotting import plot
from random import uniform
init_printing()


# In[2]:


x = Symbol('x')
f = (x ** 2 + 3) / (3 * (x + 1))
f


# In[3]:


solveset(f, x, Reals).evalf(3)


# In[4]:


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


fun1 = plot(f, (x, -7,-1.1), show = False)
fun2 = plot(f, (x, -0.9,7), show = False)
fun1.append(fun2[0])
fun1.show()


# In[7]:


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


# In[8]:


print('f > 0')
solveset(f>0, x, Reals).evalf(3)


# In[9]:


print('f < 0')
solveset(f<0, x, Reals).evalf(3)

