count=0
employeePay=0
employee0={'name':'Mary','payRate':'15.00','hoursWorked':'40'}
employee1={'name':'John','payRate':'22.00','hoursWorked':'25'}
employee2={'name':'Bob','payRate':'35.00','hoursWorked':'4'}
employee3={'name':'Mel','payRate':'43.00','hoursWorked':'62'}
employee4={'name':'Jen','payRate':'17.00','hoursWorked':'33'}
employee5={'name':'Sue','payRate':'29.00','hoursWorked':'45'}
employee6={'name':'Ken','payRate':'40.00','hoursWorked':'36'}
employee7={'name':'Dave','payRate':'20.00','hoursWorked':'17'}
employee8={'name':'Beth','payRate':'37.00','hoursWorked':'37'}
employee9={'name':'Ray','payRate':'16.50','hoursWorked':'80'}
employees=[employee0,employee1,employee2,employee3,employee4,employee5,employee6,employee7,employee8,employee9]
while count<10:
    employee=employees[count]
    if float(employee['hoursWorked'])<41:
        employeePay=float(employee['payRate'])*float(employee['hoursWorked'])
    if float(employee['hoursWorked'])>40:
        basePay=float(employee['payRate'])*40.00
        overtimeHours=(float(employee['hoursWorked'])-40.00)
        employeePay=basePay+float(employee['payRate'])*overtimeHours*1.5
    print(employee['name']+' '+str(employeePay))
    count+=1