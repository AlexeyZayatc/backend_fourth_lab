import pandas as pd

def get_reader(conn):
    return pd.read_sql_query("select * from reader",conn)

def get_book_reader(conn, reader_id):
    return pd.read_sql_query("select * from book_reader where reader_id="+str(reader_id),conn)