import mysql.connector
import random

# Connect to MySQL
mydb = mysql.connector.connect(host='localhost', user='root', password='3109')
mycursor = mydb.cursor()

# Create DATABASE and TABLE
mycursor.execute("CREATE DATABASE IF NOT EXISTS LIBRARY")
mycursor.execute("USE LIBRARY")

rec = "CREATE TABLE IF NOT EXISTS Book (bno INTEGER PRIMARY KEY, bname VARCHAR(50) NOT NULL, bauth VARCHAR(50) NOT NULL, bprice INTEGER NOT NULL, bqty INTEGER NOT NULL)"
mycursor.execute(rec)


# Connect with DATABASE
mycon = mysql.connector.connect(host='localhost', user='root', password='3109', database='LIBRARY')
mycur = mycon.cursor()

# Function to insert book record
def insertbook():
    bno = int(input("Enter Book Code: "))
    bname = input("Enter Book Name: ")
    bauth = input("Enter Book Author: ")
    bprice = int(input("Enter Book Price: "))
    bqty = int(input("Enter Book Quantity: "))
    qry = "INSERT INTO Book VALUES (%s, %s, %s, %s, %s)"
    data = (bno, bname, bauth, bprice, bqty)
    mycur.execute(qry, data)
    mycon.commit()
    print("\t\tRecord ADDED successfully...")
    

# Function to display book record
def displaybook():
    qry = "SELECT * FROM Book"
    mycur.execute(qry)
    data = mycur.fetchall()
    count = mycur.rowcount
    print("\t\tTotal Book Records.........:", count, "\n")
    for (bno, bname, bauth, bprice, bqty) in data:
        print("Book Code:\t", bno)
        print("Book Name:\t", bname)
        print("Book Author:\t", bauth)
        print("Book Price:\t", bprice)
        print("Book Quantity:\t", bqty)
        print(".................................")

# Function to search book record
def searchbook():
    bno = int(input("Enter book number to be searched...: "))
    qry = "SELECT * FROM Book WHERE bno=%s"
    rec = (bno,)
    mycur.execute(qry, rec)
    data = mycur.fetchall()
    count = mycur.rowcount
    if count != 0:
        print("\t\tBook Records found.........:\n")
        for (bno, bname, bauth, bprice, bqty) in data:
            print("Book Code:\t", bno)
            print("Book Name:\t", bname)
            print("Book Author:\t", bauth)
            print("Book Price:\t", bprice)
            print("Book Quantity:\t", bqty)
            print(".................................")
    else:
        print("\t\tRecord NOT found..!!!")
        

# Function to delete book record
def deletebook():
    bno = int(input("Enter book number to be deleted...: "))
    qry = "SELECT * FROM Book WHERE bno=%s"
    rec = (bno,)
    mycur.execute(qry, rec)
    data = mycur.fetchall()
    count = mycur.rowcount
    if count != 0:
        print("\t\tBook Records found.........:\n")
        for (bno, bname, bauth, bprice, bqty) in data:
            print("Book Code:\t", bno)
            print("Book Name:\t", bname)
            print("Book Author:\t", bauth)
            print("Book Price:\t", bprice)
            print("Book Quantity:\t", bqty)
            print(".................................")
        opt = input("Are you SURE to DELETE the above record (Y/N)...: ")
        if opt == "Y" or opt == "y":
            qry = "DELETE FROM Book WHERE bno=%s"
            rec = (bno,)
            mycur.execute(qry, rec)
            print("\n\t\tRecord deleted Successfully...... ")
            mycon.commit()
        else:
            print("\t\tRecord NOT deleted..!!!")
    else:
        print("\t\tRecord NOT found..!!!")


# Function to update book record
def updatebook():
    bno = int(input("Enter book number to be updated...: "))
    qry = "SELECT * FROM Book WHERE bno=%s"
    rec = (bno,)
    mycur.execute(qry, rec)
    data = mycur.fetchall()
    count = mycur.rowcount
    if count != 0:
        print("\t\tBook Records found.........:\n")
        for (bno, bname, bauth, bprice, bqty) in data:
            print("Book Code:\t", bno)
            print("Book Name:\t", bname)
            print("Book Author:\t", bauth)
            print("Book Price:\t", bprice)
            print("Book Quantity:\t", bqty)
            print(".................................")
        opt = input("Are you SURE to UPDATE the above record (Y/N)...: ")
        if opt == "Y" or opt == "y":
            print("\n\t\tEnter new Data....")
            bname = input("Enter New Book Name: ")
            bauth = input("Enter New Book Author: ")
            bprice = int(input("Enter New Book Price: "))
            bqty = int(input("Enter New Book Quantity: "))
            qry = "UPDATE Book SET bname=%s, bauth=%s, bprice=%s, bqty=%s WHERE bno=%s"
            rec = (bname, bauth, bprice, bqty, bno)
            mycur.execute(qry, rec)
            print("\n\t\tRecord Updated Successfully...... ")
            mycon.commit()
        else:
            print("\t\tRecord NOT updated..!!!")
    else:
        print("\t\tRecord NOT found..!!!")


# Menu

while True:
    print("\n\t\tLIBRARY BOOK RECORD MANAGEMENT\n")
    print("==================================")
    print("\t\t1. Add New Book record")
    print("\t\t2. Display Book record")
    print("\t\t3. Search Book record")
    print("\t\t4. Delete Book record")
    print("\t\t5. Update Book record")
    print("\t\t6. EXIT")
    print("==================================")
    choice = int(input("Enter choice 1-6: "))
    if choice == 1:
        insertbook()
    elif choice == 2:
        displaybook()
    elif choice == 3:
        searchbook()
    elif choice == 4:
        deletebook()
    elif choice == 5:
        updatebook()
    elif choice == 6:
        mycon.close()
        print("\nThanks, have a nice day.........")
        break
    else:
        print("\t!!! Wrong choice... please enter choice 1-6:")
