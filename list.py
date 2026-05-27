list=[1,2,2,3,4,4,5]
mylist=[]
for i in list:
 if i not in mylist:
  mylist.append(i)
print(mylist)
