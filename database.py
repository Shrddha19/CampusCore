import mysql.connector as ms
def logins():
    conn1=ms.connect(host="localhost",user="root",password="your password",database="shr")
    return conn1
def student():    
    conn2=ms.connect(host="localhost",user="root",password="your password",database="shr")
    return conn2
