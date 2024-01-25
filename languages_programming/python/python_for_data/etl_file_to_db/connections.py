import psycopg2
from common import config

parameters = config()['target']

class database:
    """ Connections destination """

    def __init__(self) -> None:
        self.host = parameters['host']
        self.database = parameters['database']
        self.user = parameters['user']
        self.password = parameters['password']
        self.port = parameters['port']
        self.autocommit = parameters['autocommit']

    def __source__conect__(self):
        self.conn=psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            port=self.port)
        self.cur_des = self.conn.cursor()
        self.conn.autocommit=self.autocommit

    def __disconnect_destination__(self):
        self.conn.close()

    def __execute__(self,sql):
        self.__source__conect__()
        self.cur_des.execute(sql)
        self.cur_des.close()
        self.__disconnect_destination__()
    
    def __copy_ex__(self,sql,file):
        self.__source__conect__()
        self.cur_des.copy_expert(sql,file)
        self.cur_des.close()
        self.__disconnect_destination__()

