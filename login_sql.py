import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='0000', db='easy_go', charset='utf8')

cursor = db.cursor()

#data = '--------------'


def login(email, password):
    sql = "SELECT Password FROM `member` WHERE AccountNumber = \'{}\';".format(email)
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        print(data[0])
        db.commit()
    except:
        db.rollback
    
    if data[0] == password:
        return True
    else:
        return False
