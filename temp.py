import cx_Oracle

class Ora(object):
    def __init__(self,uname,pwd,sid):
        self.uname = uname
        self.pwd = pwd
        self.sid = sid


    def Ora_connect(self):
        try:
            Connect = cx_Oracle.connect(self.uname, self.pwd, self.sid)
            print("Connection Established!")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 1017:
                print("logon denied due to invalid Username/Password")
                exit(1)
            elif error.code == 12154:
                print("Check the SID you passed!")
                exit(1)
            else:
                print("Please check the Conenction prameters!")
                exit(1)
            raise


if __name__ == "__main__":
    a = Ora('scott', 'power', 'orcl')
    a.Ora_connect()
