import cx_Oracle
import time

def ora_conn():
   conn_str = 'scott/power@orcl'

   conn = cx_Oracle.connect(conn_str)

   curr = conn.cursor()

   curr.execute('select * from emp')
   for i in curr:
      print(i)

#conn.close()

if __name__ == "__main__":
   ora_conn()