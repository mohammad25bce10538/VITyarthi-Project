import mysql.connector
print("""
__________________________

CHAD Shoes: For the cold!
(Shoe manufacturing unit)
__________________________
""")
mydb=mysql.connector.connect(host="localhost", user="root", passwd="ILoveMyMom@123L")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS shoe_manu")
mycursor.execute("USE shoe_manu")
mycursor.execute("CREATE TABLE IF NOT EXISTS Raw_Material(M_Id CHAR(4) NOT NULL,\
                 M_Name VARCHAR(35) NOT NULL,\
                 M_Qty_kgs INT NOT NULL,\
                 Sup_Code CHAR(4) NOT NULL)")
mycursor.execute("CREATE TABLE IF NOT EXISTS Human_Resource(E_Id CHAR(4) NOT NULL,\
                 E_Name VARCHAR(35) NOT NULL,\
                 M_Name VARCHAR(35) NOT NULL,\
                 salary INT NOT NULL)")
mycursor.execute("""CREATE TABLE IF NOT EXISTS Produced_Material(P_Id CHAR(4) NOT NULL,\
                 P_Name VARCHAR(35) NOT NULL,\
                 M_Name VARCHAR(35) NOT NULL,\
                 Price INT NOT NULL,\
                 P_Qty_pair INT NOT NULL)""")
mycursor.execute("CREATE TABLE IF NOT EXISTS Rejected_Material(P_Id CHAR(4) NOT NULL,\
                 P_Name VARCHAR(35) NOT NULL,\
                 Rej_P_Qty_pair INT NOT NULL,\
                 Reason VARCHAR(40) NOT NULL)")
mycursor.execute("CREATE TABLE IF NOT EXISTS Dispatch(P_Id CHAR(4) NOT NULL,\
                 D_Qty_pair INT NOT NULL,\
                 D_Code CHAR(4) NOT NULL,\
                 D_Location VARCHAR(18) NOT NULL)")
mydb.commit()
while True:
    print("1: Raw_Material")
    print("2: Human_Resource")
    print("3: Produced_Material")
    print("4: Rejected_Material")
    print("5: Dispatch")
    print("6: Exit")
    ch1=int(input("Enter any number from 1 to 6:"))
    if ch1==1:
        print("A: Add Record")
        print("U: Update Record")
        print("S: Search Record")
        print("D: Display Table")
        print("X: Delete Record")
        ch2 = input("Select any option:")
        if ch2=="A":
            M_Id=input("Enter material Id:")
            M_Name=input("Enter material name: ")
            M_Qty_kgs=int(input("Enter its quantity in kg:"))
            Sup_Code=input("Enter supplier code:")
            mycursor.execute("INSERT INTO Raw_Material VALUES\
                             (%s,%s,%s,%s)",(M_Id,M_Name,M_Qty_kgs,Sup_Code))
            mydb.commit()
            print("Data added successfully!")
        elif ch2=="U":
            M_Id=input("Enter material Id to update:")
            M_Name=input("Enter new material name:")
            M_Qty_kgs=int(input("Enter new quantity in kg:"))
            Sup_Code=input("Enter new supplier code:")
            mycursor.execute("UPDATE Raw_Material SET M_Name=%s,\
                             M_Qty_kgs=%s,Sup_Code=%s\
                             WHERE M_Id=%s",(M_Name,M_Qty_kgs,Sup_Code,M_Id))
            mydb.commit()
            print("Data updated successfully!") 
        elif ch2=="S":
            try:
                M_Id=input("Enter material ID: ")
                mycursor.execute("SELECT * FROM Raw_Material\
                                 WHERE M_Id=%s",(M_Id,))
                results=mycursor.fetchall()
                for i in results:
                    print(i)
            except Exception as e:
                print("Unable to fetch data:",e)
        elif ch2=="D":
            mycursor.execute("SELECT * FROM Raw_Material")
            for a in mycursor:
                print(a)
        elif ch2=="X":
            try:
                print("Proceed with caution...")
                M_Id=input("Enter material Id: ")
                mycursor.execute("DELETE FROM Raw_Material\
                                 WHERE M_Id=%s",(M_Id,))
                mydb.commit()
                print("Record deleted successfully!")
            except Exception as e:
                print("Unable to delete data:",e) 
        else:
            print("Invalid option chosen")
    elif ch1==2:
        print("A: Add Record")
        print("U: Update Record")
        print("S: Search Record")
        print("D: Display Table")
        print("X: Delete Record")
        ch3 = input("Select any option:")
        if ch3=="A":
            E_Id=input("Enter employee Id:")
            E_Name=input("Enter employee name:")
            M_Name=input("Enter material name:")
            Salary=int(input("Enter salary:"))
            mycursor.execute("INSERT INTO Human_Resource VALUES\
                             (%s, %s, %s, %s)",(E_Id,E_Name,M_Name,Salary))
            mydb.commit()
            print("Data added successfully!")
        elif ch3=="U":
            E_Id=input("Enter employee Id to update:")
            E_Name=input("Enter new employee name:")
            M_Name=input("Enter new material name:")
            Salary=int(input("Enter new salary:"))
            mycursor.execute("UPDATE Human_Resource SET E_Name=%s,\
                             M_Name=%s,Salary=%s\
                             WHERE E_Id=%s",(E_Name,M_Name,Salary,E_Id))
            mydb.commit()
            print("Data updated successfully!") 
        elif ch3=="S":
            try:
                E_Id=input("Enter employee ID:")
                mycursor.execute("SELECT * FROM Human_Resource\
                                 WHERE E_Id=%s",(E_Id,))
                results=mycursor.fetchall()
                for j in results:
                    print(j)
            except Exception as e:
                print("Unable to fetch data:",e)
        elif ch3=="D":
            mycursor.execute("SELECT * FROM Human_Resource")
            for b in mycursor:
                print(b)
        elif ch3=="X":
            try:
                print("Proceed with caution...")
                E_Id=input("Enter employee Id: ")
                mycursor.execute("DELETE FROM Human_Resource\
                                 WHERE E_Id = %s",(E_Id,))
                mydb.commit()
                print("Record deleted successfully!")
            except Exception as e:
                print("Unable to delete data:",e)
        else:
            print("Invalid option chosen")
    elif ch1==3:
        print("A: Add Record")
        print("U: Update Record")
        print("S: Search Record")
        print("D: Display Table")
        print("X: Delete Record")
        ch4 = input("Select any option: ")
        if ch4=="A":
            P_Id=input("Enter product Id:")
            P_Name=input("Enter product name:")
            M_Name=input("Enter material name: ")
            Price=int(input("Enter price:"))
            P_Qty_pair=int(input("Enter no. of pairs produced:"))
            mycursor.execute("INSERT INTO Produced_Material VALUES\
                             (%s, %s, %s, %s, %s)",(P_Id,P_Name,M_Name,Price,P_Qty_pair))
            mydb.commit()
            print("Data added successfully!")
        elif ch4=="U":
            P_Id=input("Enter product Id to update:")
            P_Name=input("Enter new product name:")
            M_Name=input("Enter new material name:")
            Price=int(input("Enter new price:"))
            P_Qty_pair=int(input("Enter new no. of pairs produced:"))
            mycursor.execute("UPDATE Produced_Material SET P_Name=%s,\
                             M_NAme=%s,Price=%s,P_Qty_pair=%s\
                             WHERE P_Id=%s",(P_Name,M_Name,Price,P_Qty_pair,P_Id))
            mydb.commit()
            print("Data updated successfully!")
        elif ch4=="S":
            try:
                P_Id=input("Enter product ID:")
                mycursor.execute("SELECT * FROM Produced_Material\
                                 WHERE P_Id = %s",(P_Id,))
                results=mycursor.fetchall()
                for k in results:
                    print(k)
            except Exception as e:
                print("Unable to fetch data:",e)
        elif ch4=="D":
            mycursor.execute("SELECT * FROM Produced_Material")
            for c in mycursor:
                print(c)
        elif ch4=="X":
            try:
                print("Proceed with caution...")
                P_Id = input("Enter product Id: ")
                mycursor.execute("DELETE FROM Produced_Material\
                                 WHERE P_Id=%s",(P_Id,))
                mydb.commit()
                print("Record deleted successfully!")
            except Exception as e:
                print("Unable to delete data:",e)
        else:
            print("Invalid option chosen")
    elif ch1==4:
        print("A: Add Record")
        print("U: Update Record")
        print("S: Search Record")
        print("D: Display Table")
        print("X: Delete Record")
        ch5 = input("Select any option:")        
        if ch5=="A":
            P_Id=input("Enter product Id:")
            P_Name=input("Enter product name:")
            Rej_P_Qty_pair=int(input("Enter no.of pairs rejected:"))
            Reason=input("Enter reason of rejection:")
            mycursor.execute("INSERT INTO Rejected_Material VALUES\
                             (%s,%s,%s,%s)",(P_Id,P_Name,Rej_P_Qty_pair,Reason))
            mydb.commit()
            print("Data added successfully!")
        elif ch5=="U":
            P_Id=input("Enter product Id to update:")
            P_Name=input("Enter new product name:")
            Rej_P_Qty_pair=int(input("Enter new no. of pairs rejected:"))
            Reason=input("Enter new reason of rejection:")
            mycursor.execute("UPDATE Rejected_Material SET P_Name=%s,\
                             Rej_P_Qty_pair=%s,Reason=%s\
                             WHERE P_Id=%s",(P_Name,Rej_P_Qty_pair,Reason,P_Id))
            mydb.commit()
            print("Data updated successfully!")
        elif ch5=="S":
            try:
                P_Id=input("Enter product ID:")
                mycursor.execute("SELECT * FROM Rejected_Material\
                                 WHERE P_Id=%s",(P_Id,))
                results=mycursor.fetchall()
                for l in results:
                    print(l)
            except Exception as e:
                print("Unable to fetch data:",e)
        elif ch5=="D":
            mycursor.execute("SELECT * FROM Rejected_Material")
            for d in mycursor:
                print(d)
        elif ch5=="X":
            try:
                print("Proceed with caution...")
                P_Id=input("Enter product Id:")
                mycursor.execute("DELETE FROM Rejected_Material\
                                 WHERE P_Id=%s",(P_Id,))
                mydb.commit()
                print("Record deleted successfully!")
            except Exception as e:
                print("Unable to delete data:",e)
        else:
            print("Invalid option chosen")
    elif ch1==5:
        print("A: Add Record")
        print("U: Update Record")
        print("S: Search Record")
        print("D: Display Table")
        print("X: Delete Record")
        ch6=input("Select any option: ")
        if ch6=="A":
            P_Id = input("Enter product Id:")
            D_Qty_pair = int(input("Enter no. of pairs dispatched: "))
            D_Code = input("Enter dispatch code:")
            D_Location = input("Enter dispatch location: ")
            mycursor.execute("INSERT INTO Dispatch VALUES\
                             (%s,%s,%s,%s)",(P_Id,D_Qty_pair,D_Code,D_Location))
            mydb.commit()
            print("Data added successfully!")
        elif ch6=="U":
            D_Code=input("Enter dispatch code to update:")
            D_Qty_pair=int(input("Enter new no. of pairs dispatched:"))
            P_Id=input("Enter new product id:")
            D_Location=input("Enter new dispatch location:")
            mycursor.execute("UPDATE Dispatch SET D_Qty_pair=%s,\
                             P_Id=%s,D_Location=%s\
                             WHERE D_Code=%s",(D_Qty_pair,P_Id,D_Location,D_Code))
            mydb.commit()
            print("Data updated successfully!")
        elif ch6=="S":
            try:
                D_Code=input("Enter dispatch code: ")
                mycursor.execute("SELECT * FROM Dispatch\
                                 WHERE D_Code=%s",(D_Code,))
                results=mycursor.fetchall()
                for m in results:
                    print(m)
            except Exception as e:
                print("Unable to fetch data:",e)
        elif ch6=="D":
            mycursor.execute("SELECT * FROM Dispatch")
            for e in mycursor:
                print(e)
        elif ch6=="X":
            try:
                print("Proceed with caution...")
                D_Code = input("Enter dispatch code: ")
                mycursor.execute("DELETE FROM Dispatch\
                                 WHERE D_Code=%s",(D_Code,))
                mydb.commit()
                print("Record deleted successfully!")
            except Exception as e:
                print("Unable to delete data:",e)
        else:
            print("Invalid option chosen")
    elif ch1==6:
        print("Exiting...")
        break
    else:
        print("Invalid option chosen")


        
