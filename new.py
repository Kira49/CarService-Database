import pymysql as ps
import pymysql.cursors
import subprocess as sp
import datetime

def addCustomer():
    try:
        new= {}
        print("Enter details: ")
        new[0]=input("Customer Name: ")
        new[1]=int(input("Contact number: "))
        new[2]=input("Membership ID: ")
        new[3]=input("Location: ")
        query="INSERT INTO Customers VALUES ('%s','%d','%s','%s');" % (new[0],new[1],new[2],new[3])
        db.cursor().execute(query)
        db.commit()
    except Exception as exp:
        db.rollback()
        print("failed to add customer")
        print(">>>>", exp)
    return

def calculate_age(born):
    today = date.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError: # raised when birth date is February 29 and the current year is not a leap year
        birthday = born.replace(year=today.year, month=born.month+1, day=1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year

def addSpare():
    try:
        new= {}
        print("Enter deatils: ")
        new[0]=input("Type ID: ")
        new[1]=input("Name: ")
        new[2]=float(input("Cost per piece: "))
        query="INSERT INTO Spares VALUES ('%s','%s','%f');" % (new[0],new[1],new[2])
        db.cursor().execute(query)
        db.commit()
    except Exception as exp:
        db.rollback()
        print("failed to add spare")
        print(">>>>", exp)
    return

def addEmployee():
    try:
        new= {}
        print("Enter details: ")
        new[0]=int(input("SSN: "))
        new[1]=input("Full Name: ")
        new[2]=int(input("Contact number: "))
        new[3]=input("Join date: ")
        new[4]=input("Birth Date: ")
        # new[5]= calculate_age(new[4])
        new[5]=int(input("Age: "))
        new[6]=int(input("Warehouse number: "))
        # new[7]=input("Assigned car: ")
        # new[8]=input("Type ID: ")
        query="INSERT INTO Employee VALUES ('%d','%s','%d','%s','%s','%d','%d');" %(new[0],new[1],new[2],new[3],new[4],new[5],new[6])
        db.cursor().execute(query)
        db.commit()
    except Exception as exp:
        db.rollback()
        print("failed to add employee")
        print(">>>>", exp)
    return

def addWarehouse():
    try:
        new= {}
        print("Enter details: ")
        new[0]=input("Type: ")
        new[1]=int(input("Warehouse number: "))
        new[2]=int(input("Number of employees"))
        query="INSERT INTO Warehouse VALUES ('%s','%d','%d');" % (new[0],new[1],new[2])
        db.cursor().execute(query)
        db.commit()
    except Exception as exp:
        db.rollback()
        print("failed to add warehouse")
        print(">>>>", exp)
    return

def addGarage():
    try:
        new= {}
        print("Enter details: ")
        new[0]=int(input("Number: "))
        new[1]=float(input("Maintenance Cost: "))
        query="INSERT INTO Garage VALUES ('%d','%f');" % (new[0],new[1])
        db.cursor().execute(query)
        db.commit()
    except Exception as exp:
        db.rollback()
        print("failed to add garage")
        print(">>>>", exp)
    return

def addCars():
    try:
        new= {}
        print("Enter details: ")
        new[0]=input("Registeration ID: ")
        new[1]=input("Due Date: ")
        new[2]=int(input("Garage number: "))
        new[3]=input("Task: ")
        new[4]=float(input("Total cost: "))
        new[5]=input("Customer ID: ")
        query="INSERT INTO Cars VALUES ('%s','%s','%d','%s','%f','%s');" % (new[0],new[1],new[2],new[3],new[4],new[5])
        db.cursor().execute(query)
        db.commit()
    except Exception as exp:
        db.rollback()
        print("failed to add car")
        print(">>>>", exp)
    return

def addServiceHistory():
    try:
        new= {}
        print("Enter details: ")
        new[0]=input("Registeration Number: ")
        new[1]=input("Task ID: ")
        new[2]=float(input("Cost: "))
        query="INSERT INTO Service_History VALUES ('%s','%s','%f');" % (new[0],new[1],new[2])
    except Exception as exp:
        db.rollback()
        print("failed to add service history")
        print(">>>>", exp)
    return

def updtserhis():
    try:
            new={}
            new[0]=input("Give the registration_no of the service you want to update the details about: ")
            new[1]=input("Give the updated cost: ")
            query="UPDATE Service_History SET cost = '%s' WHERE registeration_no='%s'; " % (new[1],new[0])
            db.cursor().execute(query)
            db.commit()
    except Exception as exp:
            db.rollback()
            print("Failed")
            print(">>>>>>>",exp)

def updtcust():
    try:
            new={}
            new[0]=input("Give the membership_id of the Customer you want to update the details about: ")
            new[1]=input("Give the updated name: ")
            new[2]=int(input("Give the updated contact: "))
            new[3]=input("Give the updated location: ")
            query="UPDATE Customers SET name = '%s',contact='%d',location='%s' WHERE membership_id='%s'; " % (new[1],new[2],new[3],new[0])
            db.cursor().execute(query)
            db.commit()
    except Exception as exp:
            db.rollback()
            print("Failed")
            print(">>>>>>>",exp)

def updtemp():
    try:
            new={}
            new[0]=input("Give the Ssn of the Employee you want to update the details about: ")
            new[1]=input("Give the updated full_name: ")
            new[2]=int(input("Give the updated contact: "))
            new[3]=input("Give the updated join_date: ")
            new[4]=input("Give the updated birth_date: ")
            new[5]=int(input("Give the updated age: "))
            new[6]=int(input("Give the updated warehouse_no: "))
            query="UPDATE Employee SET full_name = '%s',contact='%d',join_date='%s',birth_date='%s',age='%d',warehouse_no='%d' WHERE ssn='%s'; " % (new[1],new[2],new[3],new[4],new[5],new[6],new[0])
            db.cursor().execute(query)
            db.commit()
    except Exception as exp:
            db.rollback()
            print("Failed")
            print(">>>>>>>",exp)

def updtspare():
    try:
            new={}
            new[0]=input("Give the typeid of the Spare part you want to update the details about: ")
            new[1]=input("Give the updated name: ")
            new[2]=int(input("Give the updated cost_per_piece: "))
            query="UPDATE Spares SET name = '%s',cost_per_piece='%s' WHERE typeid='%s'; " % (new[1],new[2],new[0])
            db.cursor().execute(query)
            db.commit()
    except Exception as exp:
            db.rollback()
            print("Failed")
            print(">>>>>>>",exp)

def updttaskstat():
    try:
            new={}
            new[0]=input("Give the registeration_no of the service you want to update the details about: ")
            new[1]=input("Give the updated service status: ")
            query="UPDATE Service_History SET task_status = '%s' WHERE registeration_no='%s'; " % (new[1],new[0])
            db.cursor().execute(query)
            db.commit()
    except Exception as exp:
            db.rollback()
            print("Failed")
            print(">>>>>>>",exp)

def delcar():
	try:
			new1={}
			new1[0]=input("Give reg_id of car to remove: ")
			query1="DELETE from Cars where reg_id='%s';" % (new1[0])
			# query2="DELETE from Employee where assigned_car='%s';" % (new1[0])
			db.cursor().execute(query1)
			# db.cursor().execute(query2)
			db.commit()
	except Exception as exp:
			db.rollback()
			print("Failed")
			print(">>>>>>",exp)

def delemp():
	try:
			new1={}
			new1[0]=int(input("Give SSN of employee to remove: "))
			query1="DELETE from Employee where Ssn='%d';" % (new1[0])
			db.cursor().execute(query1)
			db.commit()
	except Exception as exp:
			db.rollback()
			print("Failed")
			print(">>>>>>",exp)

def delspare():
	try:
			new1={}
			new1[0]=input("Give typeid of spare to remove: ")
			query1="DELETE from Spares where typeid='%s';" % (new1[0])
			db.cursor().execute(query1)
			db.commit()
	except Exception as exp:
			db.rollback()
			print("Failed")
			print(">>>>>>>",exp)

def searchspares():
	try:
			query = " SELECT name from Spares;"
			curr.execute(query)
			rows = curr.fetchall()
			for row in rows:
				print(row)
	except Exception as exp:
			db.rollback()
			print("Failed")
			print(">>>>>>",exp)

def searchcar():
	try:
			query1 = " SELECT task, reg_id from Cars;"
			curr.execute(query1)
			rows1 = curr.fetchall()
			for row1 in rows1 :
				print(row1)
	except Exception as exp:
			db.rollback()
			print("Failed")
			print(">>>>>>",exp)

def selection():
    try:
            new={}
            new[0] = input("Table name: ")
            new[1] = input("Input WHERE clause: ")
            query = "SELECT * FROM %s WHERE %s;" % (new[0], new[1])
            db.cursor().execute(query)
            # print(db.cursor.fetchone())
            op = db.cursor().fetchall()
            for row in op:
                print(row)
            db.commit()
    except Exception as exp:
            # db.rollback()
            # print("Failed")
            # print(">>>>>>>", exp)
            db.cursor().execute(query)
            db.commit()

def projection():
    try:
            ner={}
            new[0] = input("Enter Table name: ")
            new[1] = input("Enter Column names: ")
            query = "SELECT %s FROM %s;" % (new[1], new[0])
            db.cursor().execute(query)
            op = db.cursor().fetchall()
            for row in op:
                print(row)
            db.commit()
    except Exception as exp:
            db.cursor().execute(query)
            db.commit()

def dispatch(ch):
    if(ch == 1):
        addCustomer()
    elif(ch == 2):
        addSpare()
    elif(ch == 3):
        addEmployee()
    elif(ch == 4):
        addWarehouse()
    elif(ch == 5):
        addGarage()
    elif(ch == 6):
        addCars()
    elif(ch == 7):
        addServiceHistory()
    elif(ch == 8):
        delcar()
    elif(ch == 9):
        delemp()
    elif(ch == 10):
        delspare()
    elif(ch == 11):
        selection()
    elif(ch == 12):
        searchspares()
    elif(ch == 13):
        searchcar()
    elif(ch == 14):
        updtserhis()
    elif(ch == 15):
        updtcust()
    elif(ch == 16):
        updtemp()
    elif(ch == 17):
        updtspare()
    elif(ch == 18):
        updttaskstat()
    elif(ch == 19):
        projection()

while(1) :

    user = input("Username: ")
    password = input("Password: ")
    try:
        db = ps.connect(host="127.0.0.1",
                         user=user,
                         port=5005,
                         password=password,
                         db="COMPANY",
                         cursorclass=pymysql.cursors.DictCursor)
        
        tmp = sp.call('clear', shell=True)
        
        if (db.open) :
            print("connected")
        else :
            print("Failed to connect")
        
        tmp = input("Press any key to continue> ")
        with db.cursor() as cur:
            while (1):
                tmp = sp.call('clear', shell=True)
                print("1. Add Customer")
                print("2. Add Spare")
                print("3. Add Employee")
                print("4. Add Warehouse")
                print("5. Add Garage")
                print("6. Add Cars")
                print("7. Add Service History")
                print("8. Delete Car")
                print("9. Delete Employee")
                print("10. Delete Spare")
                print("11. Selection Query")
                print("12. Search Spare parts")
                print("13. Search Car")
                print("14. Update Service history")
                print("15. Update Customer details")
                print("16. Update Employee details")
                print("17. Update Spare part details")
                print("18. Update service status")
                print("19. Projection Query")
                print("0. Quit")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 0:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")
    except :
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
