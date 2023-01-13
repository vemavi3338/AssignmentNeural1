#!/usr/bin/env python
# coding: utf-8

# In[1]:


s2_str=input()
if(len(s2_str))>=2:
    s2_str=s2_str[2:]
s2_str=s2_str[::-1]
print(s2_str)


# In[2]:


num1=int(input())
num2=int(input())
print("Addition is: ",(num1+num2));
print("substraction is: ",(num1-num2));
print("Multiplication is: ",(num1*num2));
print("Division is: ",(num1//num2));
print("Percentile is: ",(num1%num2));


# In[3]:


s2_str=input()
s2_str=s2_str.replace("python","pythons")
print(s2_str)
        


# In[4]:


score=int(input("Enter the score to get grade out of 100"))
if score>=90 and score<=100:
    print("Your Grade is A")
elif score>=80 and score<=89:
     print("Your Grade is B")
elif score>=70 and score<=79:
     print("Your Grade is C")
elif score>=60 and score<=69:
     print("Your Grade is D")
else:
     print("Your Grade is F")


# In[ ]:




