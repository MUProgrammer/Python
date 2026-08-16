fruits=["apple","banana","mango","mango","mango","orange"]
veg=["patato","tomato","onion"]
numbers=[1,2,3,4,5]
color=("red","green","blue","yellow")
# list methods
# append
# fruits.append("grapes")     # add the in last
# insert
# fruits.insert(1,"cheery")      # add the in specific index
# fruits.insert(0,45)         # add the in first index

# remove
# fruits.remove("apple")         # remove the specific value
# pop 
# fruits.pop(1)           # remove the specific index
# clear
# fruits.clear()          # clear the list
# sort
# fruits.sort()           # sort the list
# fruits.sort(reverse=True)       # sort the list reverse
# reverse
# fruits.reverse()              # reverse the list
# copy
# x=fruits.copy()                 # copy the list
# x=fruits[0:2]                 # copy the list in specific range
# extend
# fruits.extend(veg)              # extend the list
# index
# x=fruits.index("mango")         # return the index
# x=fruits.index("mango",1,6)         # return the index
# count
# x=fruits.count("mango")         # return the count
# len
# x=len(fruits)                   # return the length
# max
# x=max(numbers)                   # return the max value
# min
# x=min(numbers)                   # return the min value
# print(fruits)

# print(x)
color_list=list(color)            # convert the tuple in list
print(color_list)
