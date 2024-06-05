#definitions
employeeBonus = 50

#input information
employeeName = input("Enter the name of the Employee: ")
numShifts = input("How many shifts did the employee work? : ")
numTransactions = input("How many transactions did the employee make? : ")
valueTansactions = input("What was the total value of the transactions? : ")

# Calculate the productivity score
productScore = ((float(valueTansactions) / float(numTransactions))/float(numShifts))


if productScore < 200: 
  if productScore <70:
    if productScore <31:
      employeeBonus = 50
    else:
      employeeBonus = 75
  else:
    employeeBonus = 100
else:
  employeeBonus = 200

#output results
print("Employee name: " + str(employeeName))
print("Employee bonus: $" + str(employeeBonus))