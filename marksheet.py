#marksheet

import random

print("INTERMEDIATE MARKSHEET")
print("")
print("PYTHON SCHOOL OF SECONDARY EDUCATION","              ","Marksheet No.",random.randint(35468,65478))
print()
year=int(input("Year of Appearance       : "))
roll=int(input("Roll Number of Candidate : "))
name=input("Name of Candidate        : ")
school_code=input("School Code              : ")
print("School Name              : ULLU LULULU SCHOOL OF PYHTON")
stream=input("Stream(PCM/PCB/PCMB/CM/CWM/H) : ")
opt_s=input("Optional Subject (CS/PE/M/None) : ")
print("")
print("")

opt=random.randint(90,100)
eng=random.randint(70,100)

if stream=='PCM':
    phys=random.randint(30,100)
    chem=random.randint(30,100)
    math=random.randint(30,100)
    a=(phys+chem+math+eng+opt)/5
    print("Mathematics (041) : ",math)
    print("Physics     (052) : ",phys)
    print("Chemistry   (053) : ",chem)
    print("English     (003) : ",eng)
    print(opt_s,"         (666) : ",opt)
elif stream=='PCB':
    phy=random.randint(30,100)
    che=random.randint(30,100)
    bio=random.randint(30,100)
    a=(phy+che+bio+eng+opt)/5
    print("Biology    (085) : ",bio)
    print("Physics    (052) : ",phy)
    print("Chemistry  (053) : ",che)
    print("English    (003) : ",eng)
    print(opt_s,"       (666) : ",opt)
elif stream=='PCMB':
    phy=random.randint(30,100)
    che=random.randint(30,100)
    bio=random.randint(30,100)
    math=random.randint(30,100)
    a=(phy+che+bio+eng+opt)/5
    print("Biology       (085) : ",bio)
    print("Physics       (052) : ",phy)
    print("Chemistry     (053) : ",che)
    print("Mathematics   (041) : ",math)
    print("English       (003) : ",eng)
elif stream=='CWM':
    acc=random.randint(30,100)
    eco=random.randint(30,100)
    bst=random.randint(30,100)
    a=(acc+eco+bst+eng+opt)/5
    print("Accounts          (125) : ",acc)
    print("Economics         (542) : ",eco)
    print("Bussiness Studies (264) : ",bst)
    print("English           (003) : ",eng)
    print(opt_s,"               (666) : ",opt)
elif stream=='CM':
    acc=random.randint(30,100)
    eco=random.randint(30,100)
    bst=random.randint(30,100)
    mat=random.randint(30,100)
    a=(acc+eco+bst+eng+opt)/5
    print("Accounts          (125) : ",acc)
    print("Economics         (542) : ",eco)
    print("Bussiness Studies (264) : ",bst)
    print("Mathematics       (041) : ",mat)
    print("English           (003) : ",eng)
elif stream=='H':
    his=random.randint(30,100)
    pol=random.randint(30,100)
    eco=random.randint(30,100)
    a=(his+pol+eco+eng+opt)/5
    print("History           (147) : ",his)
    print("Political Science (213) : ",pol)
    print("Economics         (542) : ",eco)
    print("English           (003) : ",eng)
    print(opt_s,"               (666) : ",opt)
else:
    print("Invalid Data")
print("")
print("Net Score : ",a)


