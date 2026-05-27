students_marks=[12,34,56,45,32,59,45,23,44]
total=sum(students_marks)
print("total marks:",total)
average=sum(students_marks)/len(students_marks)
print("average marks:",average)
highest=max(students_marks)
print("highest marks:",highest)
lowest=min(students_marks)
print("lowest marks:",lowest)
unique=list(set(students_marks))
print("unique marks:",unique)
above=[i for i in students_marks if i>average]
print("above averge marks:",above)