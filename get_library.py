# импортируем необходимые модули
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
import sqlite3
from library_model import get_db

conn = sqlite3.connect("library.sqlite")
cursor = conn.cursor()
sql_query = """SELECT name FROM sqlite_master 
    WHERE type='table';"""
cursor.execute(sql_query)
temp = cursor.fetchall()
my_tables = [item[0] for item in temp]
my_relations = []
for table_name in my_tables:
    my_relations.append(get_db(conn,table_name))
conn.close()



env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('library_templ.html')


# генерируем результат на основе шаблона
result_html = template.render(
 tables = my_tables,
 relations = my_relations,
 len=len,
 enumerate=enumerate
 )


#создаем файл для HTML-страницы
f = open('library.html', 'w', encoding ='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()


