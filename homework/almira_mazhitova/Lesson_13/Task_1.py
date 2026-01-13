import os
import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
task_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def split_string(file_string):
    line_num = file_string.split('. ', 1)[0]
    datetime_str = (file_string.split('. ', 1)[1]).split(' - ', 1)[0]
    return line_num, datetime_str


def from_str_to_datetime(datetime_str):
    datetime_var = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S.%f')
    return datetime_var


def from_datetime_to_str(datetime_var):
    datetime_str = datetime_var.strftime('%Y-%m-%d %H:%M:%S.%f')
    return datetime_str


def read_file():
    with open(task_file_path, 'r') as homework_file:
        for line in homework_file.readlines():
            yield line


for data_line in read_file():
    if data_line.startswith('1.'):
        task_datetime_str = split_string(data_line)[1]
        task_datetime = from_str_to_datetime(task_datetime_str)
        task_date_plus_week = task_datetime + datetime.timedelta(weeks=1)
        task_date_plus_week_str = from_datetime_to_str(task_date_plus_week)
        print(task_date_plus_week_str)

    if data_line.startswith('2.'):
        task_datetime_str = split_string(data_line)[1]
        task_datetime = from_str_to_datetime(task_datetime_str)
        print(task_datetime.strftime('%A'))
    if data_line.startswith('3.'):
        task_datetime_str = split_string(data_line)[1]
        task_datetime = from_str_to_datetime(task_datetime_str)
        now = datetime.datetime.now()
        diff = now - task_datetime
        print(diff.days)
