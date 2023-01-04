expenses={
"January" : 2200,
"February" : 2350,
"March" : 2600,
"April" : 2130,
"May" : 2190
}


exp_extra=expenses["February"]-expenses["January"]
print(exp_extra)

# for x in range(0,4):
#     y=sum(x)
#     print(y)

if 2000 in expenses:
    print("you have spent 2000")
else:
    print("no expenditure of 2000")
expenses["june"]=1980 
print(expenses)

for x in range(len(expenses)):
    if expenses.keys=="April":
        expenses.values=expenses+200

print(expenses)

