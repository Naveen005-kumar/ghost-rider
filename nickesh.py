import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='12345')
cur=conn.cursor()
if conn.is_connected:
    cur.execute("CREATE DATABASE hospital")
    print("Database created successfully")

import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='12345',database='hospital')
if conn.is_connected():
    print('succesfully connected')

c=conn.cursor()
c.execute('CREATE TABLE patient_record(Patient_Name varchar(50),Age int(3),Reason varchar(50),Phone_Numner int(15))')
print('TABLE CREATED')

c.execute('CREATE TABLE doctor_record(Doctor_Name varchar(50),Qualification varchar(25),Department varchar(25))')
print('TABLE CREATED')

c.execute('CREATE TABLE employee_record(Employee_Name varchar(50),Proession varchar(20),Salary_Amount varchar(9),Phone_Number(15))')
print('TABLE CREATED')

import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='12345',database='hospital')
cur=conn.cursor()
print("              HOSPITAL MANAGEMENT SYSTEM              ")
print("1.Login")
print("2.Exit")
print()
option=int(input("enter your choice:"))
if option==1:
    user_name=input('Enter your user name :')
    password=input('Enter your password:')
    while user_name=='sary' and password=='123':
        print('connected succesfully')

        print("1.Add Patients records")
        print("2.Add Doctor records")
        print("3.Add Employee records")
        print("4.View one Patient Detail")
        print("5.Delete one patient detail")
        print("6.View one Doctor Detail")
        print("7.Delete one doctor Detail")
        print("8.View one employee detail")
        print("9.Delete one employee detail")
        print("10.Exit")


        print()
        choice=int(input('enter your choice:'))


        if choice==1:
            print()
            print("Patient Details:")
            print()
            name=input('Name:')
            name=name.upper()
            age=int(input('Age:'))
            doc=input('Reason:')
            doc=doc.upper()
            phone_no=int(input('Phone Number:'))
            cur.execute("insert into patient_record values('"+ name +"',"+ str(age) +",'"+ doc +"',"+ str(phone_no +")")
            conn.commit()
            print('Record added')


        elif choice==2:
            print()
            print("Doctor Details:")
            print()
            name=input('Name:')
            name=name.upper()
            qual=input("enter the qualification:")
            qual=qual.upper()
            dept=input("enter the department:")
            dept=dept.upper()
            cur.execute("insert into doctor_record values('"+ name + "','" + qual + "','" + dept + "')")
            conn.commit()
            print('Record added')

        elif choice==3:
            print()
            print("Employee Details :")
            print()
            emp_name=input('Employee Name:')
            emp_name=emp_name.upper()
            profession=input('Profession :')
            profession=profession.upper()
            salary=int(input('Salary amount:'))
            phone_no=input('phone_no:')
            cur.execute("insert into employee_record values('" + emp_name + "','" + profession + "'," + str(salary) + "," + str(phone_no) + ")")
            conn.commit()
            print('Record added')

        elif choice==4:
            print()
            name=input('Name of the patient:')
            name=name.upper()
            cur.execute("select*from patient_record where patient_name like'"+ str(name) +"'")
            data=cur.fetchall()
            if data!=0:
                for row in data:
                    print()
                    print("Patient Details:")
                    print()
                    print('Name:',row[0])
                    print('Age:',row[1])
                    print('Reason:',row[2])
                    print('Phone Number:',row[3])
                    input()
                else:
                    print()
                    print("Patient Record Does not Exist")

        elif choice==5:
            print()
            name=input('Name of the patient:')
            name=name.upper()
            cur.execute("delete from patient_record where Patient_Name like'" + name + "'")
            print('Record Deleted Successfully')

        elif choice==6:
            print()
            name=input('Name of the Doctor:')
            name=name.upper()
            cur.execute("select*from doctor_record where Doctor_name like'" + str(name) +"'")
            data=cur.fetchall()
            if data!=0:
                for row in data:
                    print()
                    print("Doctor Details:")
                    print()
                    print('Name:',row[0])
                    print('Qualification:',row[1])
                    print('Department:',row[2])
                    input()
            else:
                print()
                print("Doctor Record Does not Exist")

        elif choice==7:
            print()
            name=input('Name of the Doctor:')
            name=name.upper()
            cur.execute("delete from doctor_record where doctor_Name like '" + name + "'")
            print('Record Deleted Successfully')

        elif choice==8:
            print()
            name=input('Name of the employee:')
            name=name.upper()
            cur.execute("select*from employee_record where Employee_name like'" + str(name) + "'")
            data=cur.fetchall()
            if data!=0:
                for row in data:
                    print()
                    print("Employee Details:")
                    print()
                    print('Name:',row[0])
                    print('Profession:',row[1])
                    print('Salary amount:',row[2])
                    print('Phone Number:',row[3])
                    input()

        elif choice==9:
            print()
            name=input('Name of the Employee:')
            name=name.upper()
            cur.execute("delete from employee_record where Employee_Name like'" + name + "'")
            print('Record Deleted Successfully')

        elif choice==10:
            exit()

    else:
        print("Wrong Passward,Try again")

else:
    exit()
conn.commit()
input()


        
            


