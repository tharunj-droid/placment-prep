
# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expenses=[
2200,
2350,
2600,
2130,
2190]


exp_extra=expenses[1]-expenses[0]
print(exp_extra)

print("the total expenditure for first quarter is ",expenses[0]+expenses[1]+expenses[2])

if 2000 in expenses:
    print("you have spent 2000")
else:
    print("no expenditure of 2000")
expenses.append(1980) 
print(expenses)


expenses[3]=expenses[3]-200
print(expenses)

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))
heros.append('black panter')
heros.remove('black panter')

heros.insert(3, 'black panter')
print(heros)

heros[1:3]=['doctor strange']
print(heros)
heros.sort()
print(heros)

max=int(input("enter a number greater than 1"))
odd_num=[]
for i in range(1, max):
    if i % 2 == 1:
        odd_num.append(i)
print(odd_num)


