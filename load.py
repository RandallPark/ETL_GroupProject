from sqlalchemy import create_engine

connection_string = "root:root@127.0.0.1/top50_db"
engine = create_engine(f'mysql://{connection_string}')

def df_to_sql(df, table_name):
    df.to_sql(name = table_name, con = engine, if_exists = 'append', index = True)