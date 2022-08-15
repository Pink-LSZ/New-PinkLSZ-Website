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

    def checkexists(self, username):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM users WHERE username='{username}'")
                result = cursor.fetchall()
                if result:
                    return True
                else:
                    return False
            connection.commit()

    def GetAccount(self, username):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f'SELECT username, email, discriminator, hfcode, hfaccesstoken, hf_uid, discordId, avatar, isdev, isadmin FROM users WHERE username="{username}"')
                result = cursor.fetchone()
                return result
            connection.commit()

    def UpdateHF(self, username, code, access_token, uid):
        connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(f'UPDATE users SET hfcode = "{code}", hfaccesstoken = "{access_token}", hf_uid = "{uid}"WHERE username="{username}"')
            connection.commit()