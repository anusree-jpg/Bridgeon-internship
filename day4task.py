class InvalidMarkError(Exception):
   """raised when a mark is not between 0 and 100"""
   pass
def calculate_grade(name,*marks):
    if not marks:
       raise ValueError(f"no marks provided for{name}")
    for mark in marks:
       if mark<0 or mark >100:
          raise InvalidMarkError(
              f"invalid mark{mark}for{name}.marks must be between 0 and 100,"
              )
    average=sum(marks)/len(marks)
    if average>=90:
          grade= "A"
    elif average>=75:
          grade="B"
    elif average>=50:
          grade ="C"
    else:
          grade="F"
    return average,grade
def generate_report(students):
    print("\n"+"="*50)
    print(f"{'name':<15}{'average':<10}{'grade':<10}")
    print("=" * 50)
    for student in students:
           name=student[0]
           marks=student[1:]
           try:
             average,grade=calculate_grade(name,*marks)
             print(f"{name:<15}{average:<10.2f}{grade:<10}")
           except InvalidMarkError as e:
             print(f"{name:<15}ERROR{e}")
           except ValueError as e:
             print(f"{name:<15}ERROR{e}")
    print("=" * 50)
students=[("alice",98,87,77),
       ("alan",99,97,109),
      ("kiran",),
       ("alex",89,77,102),
      ("anu",44,56,45)
          ]
generate_report(students)