import mysql.connector


con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="testing"
)

cursor = con.cursor()

def user_login(tup):
    try:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM `admin` WHERE `email`=%s AND `password`=%s",tup)
        return (cursor.fetchone())
    except:
        return False

def addtraindata(source,destination,cost,refid):
    
    mysql_insert_query="""INSERT INTO record(source,destination,cost,refid) VALUES(%s,%s,%s,%s)"""
    recordTuple=(source,destination,cost,refid)
    cursor.execute(mysql_insert_query,recordTuple)
    con.commit()    
    
