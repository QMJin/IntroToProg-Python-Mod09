# ---------------------------------------------------------- #
# Title: Listing 08
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    from DataClasses import Person as P
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = P("Bob", "Smith")
objP2 = P("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
Fp.save_data_to_file("PersonData.txt", lstTable)
lstFileData = Fp.read_data_from_file("PersonData.txt")
for row in lstTable:
    print(row.to_string(), type(row))

# Test IO classes
# TODO: create and test IO module
Eio.input_menu_options()
print(Eio.input_menu_options())
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())


