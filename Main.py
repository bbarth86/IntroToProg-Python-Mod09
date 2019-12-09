# ---------------------------------------------------------- #
# Title: Assignment 09
# Description: Assignment 09
# ChangeLog (Who,When,What):
# bbarth,12.5.2019, Created Script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    from DataClasses import Employee as EmployeeClass
    from ProcessingClasses import FileProcessor as FPClass
    from IOClasses import EmployeeIO as IOClass
else:
    raise Exception("This file was not created to be imported.")

empList = []  # list of employees

# On load, read data from text file and append each row to data list in context
readfile = FPClass.read_data_from_file("EmployeeData.txt")
for row in readfile:
    empList.append(EmployeeClass(row[0], row[1], row[2].strip()))

#  Operations
while True:
    IOClass.print_menu_items()  # display menu
    choice = IOClass.input_menu_options()  # determine choice
    if choice == "1":
        IOClass.print_current_list_items(empList)  # print data list in context
        continue
    elif choice == "2":
        dataAdded = IOClass.input_employee_data()  # execute input_employee_data to determine data to be added
        empList.append(dataAdded)  # add employee data to data list in context
        continue
    elif choice == "3":
        FPClass.save_data_to_file("EmployeeData.txt", empList)  # save data list in context to file
        continue
    elif choice == "4":
        break  # exit program
