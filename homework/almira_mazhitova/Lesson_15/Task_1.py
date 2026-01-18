import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# cursor.execute("INSERT INTO students (name, second_name, group_id) values ('Almira 1', 'Mazhitova 1', NULL)")
# student_id = cursor.lastrowid


def insert_into_students(cursor_item, name, second_name):
    query = "INSERT INTO students (name, second_name) values (%s, %s)"
    cursor_item.execute(query, (name, second_name))
    result_id = cursor_item.lastrowid
    return result_id


student_id = insert_into_students(cursor, 'Almira 1111', 'Mazhitova 1111')

# cursor.execute(f"INSERT INTO books (title, taken_by_student_id) values ('Два капитана 1', {student_id})")
#
# cursor.execute(f"INSERT INTO books (title, taken_by_student_id) values ('Дневник Бриджит Джонс 1', {student_id})")

insert_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('Два капитана 1111', student_id),
        ('Дневник Бриджит Джонс 1111', student_id)
    ]
)

# cursor.execute("INSERT INTO `groups` (title, start_date, end_date) values ('January1_2026', 'Jan 2026', 'Feb 2026')")


def insert_into_groups(cursor_item, title, start_date, end_date):
    query = "INSERT INTO `groups` (title, start_date, end_date) values (%s, %s, %s)"
    cursor_item.execute(query, (title, start_date, end_date))
    result_id = cursor_item.lastrowid
    return result_id


group_id = insert_into_groups(cursor, 'January1111_2026', 'Jan 2026', 'Feb 2026')

# update_students_query = "UPDATE students s SET group_id = %s where id = %s"
# cursor.execute(update_students_query, (group_id, student_id))


def update_students_group(cursor_item, group_id_item, student_id_item):
    query = "UPDATE students s SET group_id = %s where id = %s"
    cursor_item.execute(query, (group_id_item, student_id_item))


update_students_group(cursor, group_id, student_id)

# cursor.execute("INSERT INTO subjects (title) values ('db_subject222_1')")
# subj1_id = cursor.lastrowid
#
# cursor.execute("INSERT INTO subjects (title) values ('db_subject333_1')")
# subj2_id = cursor.lastrowid


def insert_into_sujects(cursor_item, title):
    query = "INSERT INTO subjects (title) values (%s)"
    cursor_item.execute(query, (title, ))
    result_id = cursor_item.lastrowid
    return result_id


subj1_id = insert_into_sujects(cursor, 'subj121')
subj2_id = insert_into_sujects(cursor, 'subj212')

# cursor.execute(f"INSERT INTO lessons (title, subject_id) values ('db_subject222_1_introduction_1', {subj1_id})")
# lesson1_id = cursor.lastrowid
#
# cursor.execute(f"INSERT INTO lessons (title, subject_id) values ('db_subject222_1_basis_1', {subj1_id})")
# lesson2_id = cursor.lastrowid
#
# cursor.execute(f"INSERT INTO lessons (title, subject_id) values ('db_subject333_1_introduction_1', {subj2_id})")
# lesson3_id = cursor.lastrowid
#
# cursor.execute(f"INSERT INTO lessons (title, subject_id) values ('db_subject333_1_basis_1', {subj2_id})")
# lesson4_id = cursor.lastrowid


def insert_into_lessons(cursor_item, title, subject_id):
    query = "INSERT INTO lessons (title, subject_id) values (%s, %s)"
    cursor_item.execute(query, (title, subject_id))
    result_id = cursor_item.lastrowid
    return result_id


lesson1_id = insert_into_lessons(cursor, 'db_subject1111_1_introduction_1', subj1_id)
lesson2_id = insert_into_lessons(cursor, 'db_subject1111_1_basis_1', subj1_id)
lesson3_id = insert_into_lessons(cursor, 'db_subject2222_1_introduction_1', subj1_id)
lesson4_id = insert_into_lessons(cursor, 'db_subject2222_1_basis_1', subj1_id)


# cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) values ('3', {lesson1_id}, {student_id})")
#
# cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) values ('2', {lesson2_id}, {student_id})")
#
# cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) values ('4', {lesson3_id}, {student_id})")
#
# cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) values ('5', {lesson4_id}, {student_id})")


def insert_into_marks(cursor_item, value, lesson_id, student_id_item):
    query = "INSERT INTO marks (value, lesson_id, student_id) values (%s, %s, %s)"
    cursor_item.execute(query, (value, lesson_id, student_id_item))
    result_id = cursor_item.lastrowid
    return result_id


mark1_id = insert_into_marks(cursor, '3', lesson1_id, student_id)
mark2_id = insert_into_marks(cursor, '3', lesson2_id, student_id)
mark3_id = insert_into_marks(cursor, '3', lesson3_id, student_id)
mark4_id = insert_into_marks(cursor, '3', lesson4_id, student_id)


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

db.commit()
db.close()
