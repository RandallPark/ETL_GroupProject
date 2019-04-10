from sqlalchemy import create_engine
from config import connection_string

engine = create_engine(f'mysql://{connection_string}')

def df_to_sql(df, table_name):
    df.to_sql(name = table_name, con = engine, if_exists = 'append', index = True)