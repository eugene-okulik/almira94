import mysql.connector as mysql
import os
import dotenv
import csv


dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

my_dir_path = os.path.dirname(os.path.dirname(__file__))
homework_path = os.path.dirname(my_dir_path)
csv_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')


def check_row_in_db(row_item):
    query1 = f"""
select count(*) as cocount
from students s
join `groups` g on g.id = s.group_id
join books b on b.taken_by_student_id = s.id
join marks m on m.student_id = s.id
join lessons l on l.id = m.lesson_id
join subjects s2 on s2.id = l.subject_id
where s.name = %s and s.second_name = %s
and g.title = %s and b.title = %s  
and s2.title = %s and l.title = %s
and m.value = %s
    """
    cursor = db.cursor(dictionary=True)
    cursor.execute(query1, (row_item['name'], row_item['second_name'], row_item['group_title'],
                   row_item['book_title'], row_item['subject_title'], row_item['lesson_title'], row_item['mark_value']))
    count_of_strings = cursor.fetchone()['cocount']
    if count_of_strings >= 1:
        return True
    else:
        return False


with open(csv_file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    for row in file_data:
        if check_row_in_db(row):
            continue
        else:
            print(row)
