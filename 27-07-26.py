#!/usr/bin/env python
# coding: utf-8

# In[10]:


a=int(input("enter 1 number :"))
b=int(input("enter second number: "))
print("1: Addition")
print("2: Substraction")
print("3: Multiplication")
print("4: Division ")
ch=int(input("enter you choice: "))
if ch==1:
    print(a+b)
elif ch==2:
    print(a-b)
elif ch==3:
    print(a*b)
else:
    print(a/b)


# In[15]:


a=int(input("enter first number: "))
b=int(input("enter second number: "))
print("a>b: ",a>b)
print("a<b :",a<b)
print("a>5 and b>10: ",a>5 and b>10)
print("a>5 or b>10: ",a>5 or b>10)
print("a not greater than 5: ",not(a>5))


# In[22]:


dict1={"name":"ammu","age":27}
dict2={"name":"achu","age":28}
dict3=[dict1, dict2]
print(dict3)


# In[23]:


a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if a>b and a>c:
    print("greatest = ",a)
elif b>a and b>c:
    print("greatest = ",b)
else:
    print("greatest = ",c)


# In[24]:


names=["ammu","manu"]
print(names)
names.append("achu")
print(names)


# In[ ]:




