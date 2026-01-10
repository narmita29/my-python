#make dictionary with studnt name and marks and print heighest marks and average marks:
student_marks={ "arvin": 78,
               "priya" : 67,
               "sonam" : 88,
               "neelam": 90,
               "priyansh" : 98,
               "eshaa" :    56,
               "rabta" : 89

} 

topper=max(student_marks,key=student_marks.get)
print('heighest marks student is',topper,'with marks',student_marks[topper],'marks')
total=sum(student_marks.values ())
count=len(student_marks)
average=total/count
print('average of student is',average)