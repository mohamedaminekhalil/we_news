import sqlite3


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS articles (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        category TEXT,
                        date DATE,
                        title TEXT,
                        content TEXT,
                        url TEXT,
                        img TEXT,
                        author TEXT,
                        saved BOOLEAN DEFAULT 0,
                        later BOOLEAN DEFAULT 0
                    )''')
    conn.commit()


def insert_data(data):
    """
    Add new article to the data
    """
    conn = sqlite3.connect('database.db')
    create_table(conn)
    urls = select_all_urls(conn)  # To avoid duplicate articles with different titles
    cursor = conn.cursor()
    for article in data:
        if article[4] not in urls:
            cursor.execute('''INSERT INTO articles (category, date, title, content, url, img, author, saved, later)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', article)
    conn.commit()
    conn.close()


def select_all_urls(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT url FROM articles')
    rows = cursor.fetchall()
    url_list = [row[0] for row in rows]
    return url_list


def retrieve_data_by_later():
    """
        Retrieve all articles with statu later is True
    """
    conn = sqlite3.connect('database.db')
    create_table(conn)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM articles WHERE later = 1')
    rows = cursor.fetchall()
    conn.close()
    return rows


def retrieve_data_by_saved():
    """
    Retrieve all articles with statu saved is True
    """
    conn = sqlite3.connect('database.db')
    create_table(conn)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM articles WHERE saved = 1')
    rows = cursor.fetchall()
    conn.close()
    return rows


def retrieve_data_by_date(target_date):
    """
    Retrieve all articles in database from the target_date given
    """
    conn = sqlite3.connect('database.db')
    create_table(conn)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM articles WHERE date = ?', (target_date,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def toggle_later_status(id_):
    """
    Update later statu for the article with id_
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT later FROM articles WHERE id = ?', (id_,))
    current_saved = cursor.fetchone()

    new_saved = 1 if current_saved[0] == 0 else 0

    cursor.execute('UPDATE articles SET later = ? WHERE id = ?', (new_saved, id_))
    conn.commit()

    conn.close()


def toggle_saved_status(id_):
    """
    Update saved statu for the article with id_
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT saved FROM articles WHERE id = ?', (id_,))
    current_saved = cursor.fetchone()

    new_saved = 1 if current_saved[0] == 0 else 0

    cursor.execute('UPDATE articles SET saved = ? WHERE id = ?', (new_saved, id_))
    conn.commit()

    conn.close()


def get_unique_values():
    conn = sqlite3.connect('database.db')
    create_table(conn)
    cursor = conn.cursor()

    cursor.execute('SELECT DISTINCT date FROM articles')

    unique_values = [item[0] for item in cursor.fetchall()]

    conn.close()

    return unique_values
