import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='0000', db='easy_go', charset='utf8')

cursor = db.cursor()

def findMaxId():
    sql = "SELECT MAX(Id) FROM member;"
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback
    if(isinstance(data[0], int)):
        return data[0]
    else:
        return 0

def sameEmail(email):
    sql = "SELECT AccountNumber FROM member;"
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        db.commit()
    except:
        print("fail")
        db.rollback
    for i in range(findMaxId()):
        if email == data[i][0]:
            return True
    return False

    

def submit(username, email, password):
    id = findMaxId() + 1
    if sameEmail(email):
        return False
    sql = "INSERT INTO member( Id, Name, AccountNumber, Password ) \
        VALUES ({}, \'{}\', \'{}\', \'{}\')".format(id, username, email, password)
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except:
        db.rollback
        return False

