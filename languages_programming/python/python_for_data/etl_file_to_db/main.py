import os
import time
from datetime import datetime

import funtions as fun
import connections as conne
from io import StringIO
from common import config

if __name__=='__main__':

    sql = config()['query']['provisionig_table']
    insert = config()['query']['insert_table']
    file_name = config()['source']['path']

    current_path = os.getcwd()
    sub_folder_file = current_path + file_name
    
    start_time = time.time()

    try:

        destination_db = conne.database()
        destination_db.__execute__(sql)

        for df in fun.read_csv(sub_folder_file):

            sio = StringIO()
            df = df.applymap(fun.truncar_fields)
            df['execution_date'] = datetime.now()
            df.to_csv(sio, index=None, header=None)
            sio.seek(0)
            destination_db.__copy_ex__(insert,sio)

    except:
        print(f"Error en la BD")
    
    end_time = time.time() 
    total_time = end_time - start_time 
    print(f"Insert time: {total_time} seconds")
                
    
    