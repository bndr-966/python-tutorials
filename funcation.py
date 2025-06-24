def monthSalary(name,weeklyWorkingHours,overtime):
    # weeklyWorkingHours
    # overtime
    # time=input("enter the time of the day :")
    # print("good "    + time + ", " + name + " ❤!" )
    # name
    hoursWorked=weeklyWorkingHours*4 + overtime * 2
    totalSalary=(hoursWorked*50)
    output= name+" "+str(totalSalary) 
    print(output)

monthSalary("Bandar",40,6)

monthSalary("Zekry",38,3)

monthSalary("Mahomud",40,0)

monthSalary("wadee",10,3)

monthSalary("maleek",40,10)
