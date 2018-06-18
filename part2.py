# NAME: Ana Maria Cardenas Gasca
# ID: amcard

# these should be the only imports you need
import sys
import sqlite3

# write your code here
# usage should be 
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>

conn = sqlite3.connect('Northwind_small.sqlite')
c = conn.cursor()

command = sys.argv[1]

if (command == 'customers'):
    print('ID\tCustomer Name')
    for row in c.execute("SELECT id, CompanyName FROM 'Customer'"):
        print(str(row[0]) + ' \t ' + row[1])
elif (command == 'employees'):
    print('ID\tEmployee Name')
    for row in c.execute("SELECT id, FirstName, LastName FROM 'Employee'"):
        print(str(row[0]) + ' \t ' + row[1] + ' ' + row[2])
elif (command == 'orders'):
    ord_params = sys.argv[2].split("=")
    if (ord_params[0] == 'cust'):
        print('Order dates')
        for row in c.execute("SELECT OrderDate FROM 'Order' WHERE CustomerId=?", (ord_params[1],)):
            print(row[0])
    elif(ord_params[0] == 'emp'):
        print('Order dates')
        for row in c.execute("SELECT OrderDate FROM 'Order' INNER JOIN 'Employee' on 'Employee'.id = EmployeeId WHERE 'Employee'.LastName =?", (ord_params[1],)):
            print(row[0])
    