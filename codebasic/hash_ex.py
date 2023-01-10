"""nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem

Solution

nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
What was the temperature on Jan 9?
What was the temperature on Jan 4?
Figure out data structure that is best for this problem

Solution

poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
 'diverged': 2,
 'in': 3,
 'I': 8
Solution

Implement hash table where collisions are handled using linear probing. We learnt about linear probing in the video tutorial. Take the hash table implementation that uses chaining and modify methods to use linear probing. Keep MAX size of arr in hashtable as 10."""


arr = []
with open('codebasic/nyc_weather.csv') as f:
    for line in f:
        tokens = line.split(',')
        try:
            temp = int(tokens[1])
            arr.append(temp)
        except:
            print("invalid temperature")


avg_week=sum(arr[0:7])/len(arr[0:7])
print("the avg for the week in jan is",avg_week)

print(avg_week)

avg=0  

for t in arr:
    avg+=t
print(max(arr[0:10]))
print("the max temp in jan is",avg)


weather_dict = {}
with open('codebasic/nyc_weather.csv') as f:
    for line in f:
        tokens = line.split(',')
        day=tokens[0]
        try:
            temp = int(tokens[1])
            weather_dict[day]=temp
        except:
            print("invalid temperature")

print(weather_dict)

print(weather_dict['Jan 9'])
print(weather_dict['Jan 4'])



'''with open('codebasic/poem.txt') as f:
    for line in f:
        print(line)'''


wordcount={}

with open('codebasic/poem.txt') as f:
    for line in f:
        tokens=line.split(' ')
        for token in tokens:
            token=token.replace('\n','')
            if token in wordcount:
                wordcount[token]+=1
            else:
                wordcount[token]=1

print(wordcount)
print(max(wordcount))

