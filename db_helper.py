import mysql.connector
from mysql.connector import Error
import db_connection


newconnection = db_connection.connection
add = "INSERT INTO persons (personname, personphone) VALUES (%s, %s);"
deletenameorphone = "DELETE FROM persons WHERE personname = %s or personphone= %s"

#username = 'saahilll'
#phoneno = 12323123

def addcontact(username, phoneno):
    try:
        newcursor = newconnection.cursor(prepared=True)
        newcursor.execute(add, (username, phoneno))
        newconnection.commit()

    except Error as e:
        newconnection.rollback()
        print("Error while Inserting to MySQL", e)

    finally:
        if newconnection.is_connected():
            newcursor.close()
            newconnection.close()
            print("MySQL connection is closed")

def deletecontact_name(namee):
    try:
        newcursor = newconnection.cursor()
        newcursor.execute(deletenameorphone, (namee, '0'))
        newconnection.commit()

    except Error as e:
        newconnection.rollback()
        print("Error while deleting in MySQL", e)

    finally:
        if newconnection.is_connected():
            newcursor.close()
            newconnection.close()
            print("MySQL connection is closed")


def deletecontact_phone(phonee):
    try:
        newcursor = newconnection.cursor()
        newcursor.execute(deletenameorphone, ('0', phonee))
        newconnection.commit()

    except Error as e:
        newconnection.rollback()
        print("Error while deleting in MySQL", e)

    finally:
        if newconnection.is_connected():
            newcursor.close()
            newconnection.close()
            print("MySQL connection is closed")


def show():
    try:
        newcursor = newconnection.cursor()
        newcursor.execute("select personname from persons")
        result = newcursor.fetchall()
        for x in result:
            print(x)

    except Error as e:

        print("Error while fetching data from MySQL", e)

    finally:
        if newconnection.is_connected():
            newcursor.close()
            newconnection.close()
            print("MySQL connection is closed")
