import sqlite3 

# Connect to database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    grade INTEGER,
    address TEXT
)
""")
conn.commit()

# Insert multiple rows (note the comma between values)
cursor.executemany("""
INSERT INTO student (name, grade, address)
VALUES (?, ?, ?)
""", [
    ('Rabin', 12, 'Samakhushi'),
    ('Karma', 10, 'Boudha'),
    ('Hari', 9, 'Sukedhara')
])
conn.commit()

# Display all records
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
print("All Records:")
for item in rows:
    print(item)

# Update Karma's address
cursor.execute("""
UPDATE student
SET address = 'Lalitpur'
WHERE name = 'Karma'
""")
conn.commit()

# Delete Rabin
cursor.execute("""
DELETE FROM studentgit 
WHERE name = 'Rabin'
""")
conn.commit()

# Show final data after update and deletegit remote add origin url
print("\nAfter Update and Delete:")
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
for item in rows:
    print(item)

conn.close()