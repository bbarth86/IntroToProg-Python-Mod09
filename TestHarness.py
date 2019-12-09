# ---------------------------------------------------------- #
# Title: Testing Harness
# Description: Primary Module for Testing
# ChangeLog (Who,When,What):
# bbarth,12.5.2019, Created Script
# ---------------------------------------------------------- #

if __name__ == "__main__":
    from DataClasses import Employee as EmployeeConst
    from DataClasses import Person as PersonConst
    from ProcessingClasses import FileProcessor as FPClass
    from IOClasses import EmployeeIO as EmpIO
else:
    raise Exception("This file was not created to be imported.")

# test data processing module - create person
per1 = PersonConst("Test", "Person")
testPeople = [per1]
for row in testPeople:
    print(row.to_string(), type(row))

# test data processing module - create employee
emp1 = EmployeeConst(1, "Beau", "Barth")
emp2 = EmployeeConst(2, "Dana", "Barth")
testData = [emp1, emp2]
for row in testData:
    print(row.to_string(), type(row))

#  test file processing - save data
FPClass.save_data_to_file("EmployeeData.txt", testData)

#  test file processing - read data
readfile = FPClass.read_data_from_file("EmployeeData.txt")  # read from file
testData.clear()  # clear testData before append, print
for row in readfile:
    testData.append(EmployeeConst(row[0], row[1], row[2].strip()))  # converts row to employee object
for row in testData:
    print(row.to_string(), type(row))

#  test employee IO processing - get new employee
testEmployee = EmpIO.input_employee_data()
print(testEmployee)
