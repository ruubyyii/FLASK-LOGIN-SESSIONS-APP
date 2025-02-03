class ModelUser():

    def login(self, db, user):

        try:
            cur = db.connection.cursor()
            sql = 'SELECT * FROM user WHERE username = %s'

            cur.execute(sql, (user.username,))
            row = cur.fetchone()
        except Exception as e:

            raise Exception(e)