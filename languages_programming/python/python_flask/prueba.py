import pandas as pd
from sqlalchemy import create_engine
import os
from etl import etl_data_obj
import pandas as pd

# Supongamos que tenemos un DataFrame df
data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C': [11, 12, 13, 14, 15]}

df = pd.DataFrame(data)
print(df)

# Filtrar el DataFrame donde el valor de la primera columna ('A') sea igual a 3
df_result = pd.DataFrame(df.iloc[2])

print(df.loc[df.index == 2])
#print(df_result.pivot_table())