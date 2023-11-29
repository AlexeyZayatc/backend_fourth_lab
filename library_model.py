import pandas as pd
def get_db(conn, db_name):
 return pd.read_sql("SELECT * FROM "+ db_name, conn)
