import sqlite3

def connect():
    conn = sqlite3.connect('new_database.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS daily_activities (Id INTEGER PRIMARY KEY, activity_date TEXT, income INTEGER, exercise_status TEXT, '
                'diet_status TEXT, study_status TEXT, python_practice_status TEXT)')
    conn.commit()
    conn.close()

def insert(activity_date, income, exercise_status, diet_status, study_status, python_practice_status):
    conn = sqlite3.connect('new_database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO daily_activities VALUES (NULL, ?,?,?,?,?,?)",
                (activity_date, income, exercise_status, diet_status, study_status, python_practice_status))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('new_database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM daily_activities")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('new_database.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM daily_activities WHERE id=?", (id,))
    conn.commit()
    conn.close()

def search(activity_date='', income='', exercise_status='', diet_status='', study_status='', python_practice_status=''):
    conn = sqlite3.connect('new_database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM daily_activities WHERE activity_date=? OR income=? OR exercise_status=? OR diet_status=? OR study_status=? OR python_practice_status=?",
                (activity_date, income, exercise_status, diet_status, study_status, python_practice_status))
    rows = cur.fetchall()
    conn.close()
    return rows

# Example usage:
# connect()
# insert('2023-01-20', 3000, 'no', 'yes', 'no', 'yes')
# print(view())
# delete(1)
