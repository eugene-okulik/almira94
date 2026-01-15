import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO students (name, second_name, group_id) values ('Almira 1', 'Mazhitova 1', NULL)")
student_id = cursor.lastrowid
print(f"student_id={student_id}")

cursor.execute(f"INSERT INTO books (title, taken_by_student_id) values ('Два капитана 1', {student_id})")

cursor.execute(f"INSERT INTO books (title, taken_by_student_id) values ('Дневник Бриджит Джонс 1', {student_id})")

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) values ('January1_2026', 'Jan 2026', 'Feb 2026')")
group_id = cursor.lastrowid
print(f"group_id={group_id}")

cursor.execute(F"UPDATE students s SET group_id = {group_id} where id = {student_id}")

cursor.execute("INSERT INTO subjects (title) values ('db_subject222_1')")
subj1_id = cursor.lastrowid

cursor.execute("INSERT INTO subjects (title) values ('db_subject333_1')")
subj2_id = cursor.lastrowid
print(f"subj2_id={subj2_id}")

cursor.execute(f"INSERT INTO lessons (title, subject_id) values ('db_subject222_1_introduction_1', {subj1_id})")
lesson1_id = cursor.lastrowid
print(f"lesson1_id={lesson1_id}")

cursor.execute(f"INSERT INTO lessons (title, subject_id) values ('db_subject222_1_basis_1', {subj1_id})")
lesson2_id = cursor.lastrowid
print(f"lesson2_id={lesson2_id}")

cursor.execute(f"INSERT INTO lessons (title, subject_id) values ('db_subject333_1_introduction_1', {subj2_id})")
lesson3_id = cursor.lastrowid
print(f"lesson3_id={lesson3_id}")

cursor.execute(f"INSERT INTO lessons (title, subject_id) values ('db_subject333_1_basis_1', {subj2_id})")
lesson4_id = cursor.lastrowid
print(f"lesson4_id={lesson4_id}")

cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) values ('3', {lesson1_id}, {student_id})")

cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) values ('2', {lesson2_id}, {student_id})")

cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) values ('4', {lesson3_id}, {student_id})")

cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) values ('5', {lesson4_id}, {student_id})")

db.commit()

marks = cursor.execute(f"SELECT m.value FROM marks m WHERE m.student_id = {student_id}")
print(cursor.fetchall())

cursor.execute(f"SELECT b.title FROM books b WHERE b.taken_by_student_id = {student_id}")
print(cursor.fetchall())

big_query = f"""SELECT * FROM students s
JOIN `groups` g ON g.id = s.group_id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjects s2 ON s2.id = l.subject_id
WHERE s.id = {student_id}"""

cursor.execute(big_query)
print(cursor.fetchall())

db.close()
