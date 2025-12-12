#Nesting dictionary
student={
          'Name' : 'urmi',
          'Roll no' : 7640,
          'subject' :{                   #other dictionary
                      'java': 87,
                      'SAD' : 76,
                      'English' : 66
              
          }
}

print(student)
print(student['subject']['java'])