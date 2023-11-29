import pandas as pd

def get_amount(conn, author, genre):
    return pd.read_sql_query('''
                select 
                title as "Название", 
                name_author as "Автор",
                amount as "Количество",
                name_genre as "Жанр",
                IIF(book.amount<3,'мало',
                    IIF(book.amount>10,'много','достаточно')) as "Наличие"
                from book
                join author using (author_id)
                join genre using (genre_id)
                where author_id=''' + str(author) + ''' and genre_id = '''+ str(genre) + " order by 2",conn)

def get_genre(conn):
    return pd.read_sql_query('''
                             select * from genre                             
                             ''',conn)

def get_author(conn):
    return pd.read_sql_query('''
                             select * from author                             
                             ''',conn)