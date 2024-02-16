import pandas as pd
from sqlalchemy import create_engine, text
import os
engine = create_engine('postgresql://postgres:1234@localhost:8009/postgres', echo=False)

class etl_data:
   
   def __init__(self,dept) -> None:
    self.dept=dept
    print('dept value',self.dept)

   def get_details(self,id):

    emp_df = pd.read_sql_query('select empno,ename,sal,deptno from emp',engine)
    filter_emp_dict = emp_df.loc[emp_df.index == int(id)]
    print(emp_df.loc[emp_df.index == id])
    result=filter_emp_dict.to_dict(orient='index')
    return result
   
   def post_data(self,file,table,delete_data):

    if delete_data == "True":
      conn = engine.connect()
      conn.execute(text("TRUNCATE TABLE emp"))
      conn.commit()
      conn.close()

    path = os.getcwd() + '/source/' + file
    df = pd.read_csv(path, index_col=0, sep=',')
    write_df = df.to_sql(table, engine, if_exists='append')
    if write_df == 1:
      return df.to_dict(orient='index')

etl_data_obj=etl_data('00')