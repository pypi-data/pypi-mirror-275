# snippet_manager/database.py
import sqlite3

def setup_database():
    conn = sqlite3.connect('snippets.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS snippets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            tags TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_snippet(title, content, tags):
    conn = sqlite3.connect('snippets.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO snippets (title, content, tags)
        VALUES (?, ?, ?)
    ''', (title, content, tags))
    conn.commit()
    conn.close()
    print(f'Snippet "{title}" added successfully!')

def search_snippets(query):
    conn = sqlite3.connect('snippets.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, title, content, tags
        FROM snippets
        WHERE title LIKE ? OR tags LIKE ?
    ''', (f'%{query}%', f'%{query}%'))
    results = cursor.fetchall()
    conn.close()
    return results

def view_snippet(snippet_id):
    conn = sqlite3.connect('snippets.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, title, content, tags
        FROM snippets
        WHERE id = ?
    ''', (snippet_id,))
    snippet = cursor.fetchone()
    conn.close()
    return snippet

def delete_snippet(snippet_id):
    conn = sqlite3.connect('snippets.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM snippets
        WHERE id = ?
    ''', (snippet_id,))
    conn.commit()
    conn.close()
    print(f'Snippet with ID {snippet_id} deleted successfully!')
