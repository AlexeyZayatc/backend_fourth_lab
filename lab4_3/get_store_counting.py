from jinja2 import Template
import sqlite3
from store_counting_model import get_amount, get_author, get_genre

# устанавливаем соединение с базой данных
conn =sqlite3.connect("store.sqlite")

author_id = 3
genre_id = 2

df_store_counting = get_amount(conn, author_id, genre_id)

df_author = get_author(conn)
df_genres = get_genre(conn)

# закрываем соединение с базой
conn.close()
f_template = open("store_counting_template.html",encoding='utf-8-sig')
html = f_template.read()
f_template.close()
# создаем объект-шаблон
template = Template(html)
# генерируем результат на основе шаблона
result_html = template.render(
 author_id = author_id,
 genre_id = genre_id,
 first_combo_box = df_author,
 second_combo_box = df_genres,
 store_counting = df_store_counting,
 len = len
 )
#создаем файл для HTML-страницы
f = open('store_counting.html', 'w', encoding ='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()
