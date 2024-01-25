import pandas as pd

def read_csv(file_name):
    for chuck in pd.read_csv(file_name, chunksize=10000):
        yield chuck

def truncar_fields(valor):
    if isinstance(valor, str):
        return valor[:5000]
    return valor        