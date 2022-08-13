#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1.What are the two values of the Boolean data type? How do you write them? 

ANS:- True and False , denoted by using first letter capital T and F.


# In[1]:


#eg:
a = True
b = False
print(a)
print(b)


# In[ ]:


Q2. What are the three different types of Boolean operators? 

Ans:- and , or and not


# In[ ]:


Q3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean 
    values for the operator and what it evaluate ).
    
Ans:- True and True is True
      True and False is False
      False and False is False
      False and True is False
        
      True or True is True
      True or False is True
      False or True is True
      False or False is Trrue  
        
      not True is Flase
      not False is True
        
      True = 1 AND False = 0
      
      Truth table for AND
       

        
    


# In[3]:


#4. What are the values of the following expressions?
print((5>4) and (3==5))
print(not(5>4))
print((5>4)or(3==5))
print(not(5>4) or (3==5))
print((True and True)  and (True == False))
print((not(False))or(not(True)))


# In[ ]:


get_ipython().set_next_input('Q5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')
 
Ans:- ==,!=,<,>,<= and >=


# In[ ]:


Q6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

Ans:- == is the equal to operator that compares two values and result to a boolean,where as = is the assignment operator that assigns values from right side operators to left side operators.


# In[12]:


#eg
#equal to operator
if(2==3):
    print("True")
else:
    print("Flase")
    
#Assignment operators
a = 1
b = 2
c = a+b
print(c)


# In[ ]:


7. Identify the three blocks in this code:


# In[4]:


spam =0
if spam == 10:
    print('eggs') # block 1
if spam > 5:
    print('bacon') # block 2
else:
    print('ham') #block 3
print('spam')
print('spam')


# In[ ]:


8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.


# In[6]:


def spamfun(spam):
    if spam == 1:
        print('Hello')
    elif spam == 2:
        print('Howdy')
    else:
        print('Greeting')

spamfun(1)
spamfun(2)
spamfun(3)


# In[ ]:


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')

Ans:- Press Ctrl-c to stop a program stuck in an infinite loop


# In[ ]:


get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')

Ans:-  Break statement is used to terminate the loop.It is used in loop and switch case.
       Continue statement is used to continue thenext iteration in the loop.


# In[ ]:


11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

Ans:- The range(10) call range from 0 to 9 (but not include 10)
      The range (0,10) explicitly tells the loop to start at 0
      The range(0,10,1) explicitly tells the loop to increase the variable by 1 on each iteration


# In[ ]:


12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop ?


# In[8]:


#By using for loop
print('FOR LOOP')
for i in range(1,11):
    print(i)
    
#By using while loop
print('WHILE LOOP')
a = 1
while a <= 10:
    print(a)
    a = a + 1


# In[ ]:


get_ipython().set_next_input('Q13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')

Ans:- spam.bacon()

