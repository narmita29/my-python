#WAP TO ENTER MARKS OF 4 SUBJECTS FROM USER AND STORE THEM IN DIC
marks={}
x=int(input("python : "))
marks.update({'python': x})
x=int(input("SAD : "))
marks.update({'SAD': x})
x=int(input("ASP.NET : "))
marks.update({'ASP.NET': x})
x=int(input("Operating system: "))
marks.update({'Operating system': x})
print(marks)
