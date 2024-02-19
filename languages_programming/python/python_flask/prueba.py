import connections as conne
import pandas as pd

conn = conne.database()

pd.read_sql_query('select empno,ename,sal,deptno from emp',conn.create_engine())

conn.execute('TRUNCATE TABLE emp')

columns = conn.metadata('jobs')