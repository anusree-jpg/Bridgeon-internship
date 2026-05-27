list1=["arun","meera","anu"]
list2=["meera","kiran","varun"]
list3=list1+list2
print(list3)
new_list=list(set(list3))
print(new_list)
new_list.sort()
print(new_list)