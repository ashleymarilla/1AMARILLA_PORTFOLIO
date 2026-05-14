#!/usr/bin/env python
# coding: utf-8

# In[4]:


daily_allowance = 500
daily_expense = 260
print("-" * 35)
print("COMPARISON OPPERATIONS")
print("-" * 35)
print("Allowance : ₱", daily_allowance)
print("Expense   : ₱", daily_expense)
print("-" * 35)
print("Expense < Allowance  :", daily_expense < daily_allowance)
print("Expense > Allowance  :", daily_expense > daily_allowance)
print("Expense == 260      :", daily_expense == 260)
print("Expense != 300      :", daily_expense != 300)
print("Allowance >= 500    :", daily_allowance >= 500)


# In[5]:


print("-" * 35)
print("ONE-WAY DECISIONS")
print("-" * 35)
daily_expense = 260

print("Before")
if daily_expense < 300 :
    print("Is 260")
    print("Still 260")
    print("Third 260")

print("Afterwards")
if daily_expense > 200 :
    print("Is 260 still")
    print("Third 260 again")


# In[6]:


print("-" * 35)
print('TWO-WAY DECISIONS')
print("-" * 35)

daily_expense = 260
daily_allowance = 500

print("Check Budget:")
if daily_expense > daily_allowance :
    print("Over Budget")
else :
    print("Within Budget")


# In[7]:


print("-" * 35)
print('MULTI-WAY DECISIONS')
print("-" * 35)
daily_expense = 260

if daily_expense < 200 :
    print("Small")
elif daily_expense < 350 :
    print("Medium")
elif daily_expense < 500 :
    print("Large")
else :
    print("Very Large")


# In[8]:


print("-" * 35)
print('NESTED DECISIONS')
print("-" * 35)
daily_expense = 260
is_school_day = True

if is_school_day :
    print("It is school day")
    if daily_expense < 300 :
        print("Normal spending")
else :
    print("It is weekend")
    if daily_expense < 400 :
        print("Normal weekend spending")


# In[19]:


print("-" * 35)
print('TRY / EXCEPT')
print("-" * 35)
print("Start Program")
try:
    daily_allowance = 500
    daily_expense = 260
    savings = daily_allowance - daily_expense
    print("Calculation OK")
except:
    print("Something went wrong")


# In[18]:


daily_allowance = 500    
daily_expense = 260      
is_school_day = True    
print("=" * 35)
print("📊STUDENT EXPENSE SUMMARY REPORT:")
print("Student: Ashley M. Marilla | Bicol University")
print("=" * 35)


#1. COMPARISON OPERATORS
print("-" * 30)
print("Allowance =", daily_allowance)
print("Expense   =", daily_expense)

is_equal_260   = daily_expense == 260
is_more_200    = daily_expense > 200
is_less_300    = daily_expense < 300
is_within_limit = daily_expense <=daily_allowance

if is_equal_260 : print("My Expense is exactly 260")
if is_more_200  : print("My Expense is above 200")
if is_less_300  : print("My Expense is below 300")

#2. ONE-WAY DECISION(Runs ONLY if Step 1 result is TRUE)

print("-"*35)

print("Before checking:")
if is_within_limit :
    savings = daily_allowance - daily_expense 
    print("I have remaining money!")
    print("My Total Savings: ₱", savings)      

#3: TWO-WAY DECISION
print("Budget Status Check:")
if is_within_limit :
    print("WITHIN BUDGET!")
else :
    print("OVER BUDGET")


# 4: MULTI-WAY DECISION
print("-"*35)
print("Spending Level Check:")
if daily_expense < 200 :
    level = "LOW"
elif daily_expense < 350 :
    level = "MEDIUM"
elif daily_expense < 500 :
    level = "HIGH"
else :
    level = "VERY HIGH "

print("Expense Level:", level)

#5. NESTED DECISION
print("-"*35)
if is_school_day :
    print("Today is: SCHOOL DAY")
    if daily_expense <= 300 :
        print("→ Spending: NORMAL")
    else :
        print("→ Spending: HIGH")
else :
    print("→ Today is: WEEKEND")
    if daily_expense <= 400 :
        print("→ Spending: NORMAL")
    else :
        print("→ Spending: HIGH ")

# 6. TRY / EXCEPT STRUCTURE
print("-" * 35)
try:
    verified_savings = daily_allowance - daily_expense
    print("\n MY OFFICIAL STUDENT EXPENSE SUMMARY:")
    print("• Daily Allowance : ₱", daily_allowance)
    print("• Total Expense   : ₱", daily_expense)
    print("• Remaining Savings: ₱", verified_savings)
    print("• Spending Level  : ", expense_level)
    print("• Budget Status   : ", "WITHIN LIMIT" if is_within_budget else "OVER LIMIT")
except:
    print("❌ System Notice: Error encountered while generating summary")


# In[ ]:




