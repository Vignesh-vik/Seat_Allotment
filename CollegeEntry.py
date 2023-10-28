# clg,stud = int(input("clg:")),int(input("stud:"))
clg =3
stud=3
seats=[]
def Num_seats():
    i=1
    while i <= clg:
        print("Enter number seats in college",i,":")
        a=int(input(""))
        seats.append(a)
        i+=1
Num_seats()
dets={}
def Studs_dets():
    i=1
    while i<=stud:
        print("Details of student",i,":")
        perc = input("enter percentage:")
        alot = input("enter Allotment:")
        alot = alot.split(" ")
        # print(alot)
        dets = [perc,alot]
        print(dets)
Studs_dets()



