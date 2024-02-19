import pandas as pd
import os
from io import StringIO
import connections as conne

local_path = os.getcwd()
path_file = local_path + '/source/'
provisioning_db = local_path + '/source/source_sql/'
conn = conne.database()
engine = conn.create_engine()

def read_csv(file_name):
  for chuck in pd.read_csv(file_name, chunksize=10000, sep = ',',header = None):
    yield chuck

class etl_data:
   
  def __init__(self,dept) -> None:
    self.dept = dept

  def get_details(self,id,table):
    """ Get consult for id """

    columns_table = conn.metadata(table)
    columns_consult = ','.join(columns_table)
    query = 'SELECT ' + columns_consult + ' FROM ' + table
    emp_df = pd.read_sql_query(query,engine)
    filter_emp_dict = emp_df.loc[emp_df.index == int(id)]
    result = filter_emp_dict.to_dict(orient='index')
    return result
   
  def post_data(self,file,table,delete_data):
    """ Post load information from csv file to table """

    file_sql = provisioning_db + table + '.sql'
    if os.path.exists(file_sql):
      with open(file_sql,'r',encoding = 'UTF-8') as sql_file:
        lines = sql_file.read()
        conn.execute(lines)
    if delete_data == "True":
      conn.execute(f'TRUNCATE TABLE {table}')

    for df in read_csv(path_file + file):
      sio = StringIO()
      df.to_csv(sio, index=None, header=None)
      columns_table = conn.metadata(table)
      df.columns = columns_table
      sio.seek(0)
      write_df = df.to_sql(table, engine, if_exists = 'append',index=False)
      if write_df != 0:
        return df.to_dict(orient='index')
      
etl_data_obj=etl_data('00')