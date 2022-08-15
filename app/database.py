import pymysql.cursors

class MySQL:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database

    def query(self, query, querytype='select', fetchall=True):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                if querytype == 'select':
                    if fetchall == True:
                        result = cursor.fetchall()
                    else:
                        result = cursor.fetchone()
                    return result
            connection.commit()