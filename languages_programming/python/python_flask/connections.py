from sqlalchemy import create_engine,text,MetaData,Table

class database:

    def __init__(self) -> None:

        self.host = 'localhost'
        self.user = 'postgres'
        self.database = 'postgres'
        self.password = '1234'
        self.port = '8009'
        self.engine = self.create_engine()

    def create_engine(self):
        """ Get consult for id """

        return create_engine('{engine}://{user}:{password}@{host}:{port}/{database}'.format(
            engine='postgresql',
            user = self.user,
            password = self.password,
            host = self.host,
            port = int(self.port),
            database = self.database
        ))
      
    def execute(self,sql):
        """ Post load information from csv file to table """

        cur = self.create_engine().connect()
        cur.execute(text(sql))
        cur.commit()
        cur.close()

    def metadata(self,table_name):

        table_reflection = Table(table_name,
                                 MetaData(),
                                 autoload_with = self.create_engine().connect())
        return table_reflection.columns.keys()