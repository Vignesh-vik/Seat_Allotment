#Inputs


clg, stud = int(input("clg:")), int(input("stud:"))
# clg =3
# stud=3
seats = []


def Num_seats():
    i = 1
    while i <= clg:
        print("Enter number seats in college", i, ":")
        a = int(input(""))
        seats.append(a)
        i += 1
    print(seats)
Num_seats()


S_dets = list()

def Studs_dets():
    i = 1
    while i <= stud:
        print("Details of student", i, ":")
        perc = input("enter percentage:")
        alot = input("enter Allotment: \n  \t")
        alot = alot.split(",")
        # print(alot)
        dets = [perc, alot]
        S_dets.append(dets)
        i += 1
        # print(S_dets)
Studs_dets()

# print(S_dets)


#Algorithm
max = S_dets[0][0]
for i in S_dets:
    if i[0] > max:
        max=i
    print(max)





