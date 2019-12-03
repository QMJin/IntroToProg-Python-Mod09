# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# QimingJin,12.03.2019,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of employee objects
    # Let user add data to the list of employee objects
    # let user save current data to file
    # Let user exit program
lstEmployeeTable=[]
lstFileData = []

# Main Body of Script  ---------------------------------------------------- #
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
for row in lstFileData:
    lstEmployeeTable.append(Emp(row[0], row[1], row[2].strip()))

while True:
    Eio.print_menu_items()
    strChoice = Eio.input_menu_options()
    if strChoice.strip() == '1':
        Eio.print_current_list_items(lstEmployeeTable)
        continue
    elif strChoice.strip() == '2':
        lstEmployeeTable.append(Eio.input_employee_data())
        continue
    elif strChoice.strip() == '3':
        Fp.save_data_to_file("EmployeeData.txt", lstEmployeeTable)
        continue
    elif strChoice.strip() == '4':
        break
