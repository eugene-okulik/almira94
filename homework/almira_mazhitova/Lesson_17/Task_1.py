import argparse
import os
import re

from datetime import datetime
from pathlib import Path


def is_date_time_format(datetime_str):
    # Заданный формат в логах
    date_format = '%Y-%m-%d %H:%M:%S.%f'
    try:
        # Пытаемся распарсить строку
        datetime.strptime(datetime_str, date_format)
        return True
    except ValueError:
        # Если строка не соответствует формату или содержит невалидные данные
        return False


def log_parse(user_path, user_error_text):
    path_logsdir_or_logsfile_path = Path(f'{user_path}')
    error_text = user_error_text
    error_text_words = re.findall(r'\w+', error_text)
    files_dict = {}
    if not path_logsdir_or_logsfile_path.exists():
        print(f"Переданный путь ({path_logsdir_or_logsfile_path}) не существует")
    if path_logsdir_or_logsfile_path.is_dir():
        with os.scandir(path_logsdir_or_logsfile_path) as entries:
            for entry in entries:
                if entry.is_file():
                    files_dict[entry.name] = entry.path
    if path_logsdir_or_logsfile_path.is_file():
        files_dict[path_logsdir_or_logsfile_path.name] = path_logsdir_or_logsfile_path

    errors_dict = {}
    for file_name, file_path in files_dict.items():
        errors_dict[file_name] = []
        data_dict = {}
        with open(files_dict[file_name], 'r', encoding='utf-8') as f:
            string_num = 0
            for string in f:
                string_num += 1
                datetime_string = string[:22]
                if is_date_time_format(datetime_string):
                    data_dict[datetime_string] = []
                    data_dict[datetime_string].append((string[22:].strip(), string_num))
                    before_datetime_string = datetime_string
                else:
                    data_dict[before_datetime_string].append((string.strip(), string_num))

            for log_time, string_list in data_dict.items():
                for string_info in string_list:
                    string = string_info[0]
                    string_num = string_info[1]
                    if error_text in string:
                        words_in_string = re.findall(r'\w+', string)
                        n = len(words_in_string)
                        m = len(error_text_words)
                        for i in range(n - m + 1):
                            if words_in_string[i: i + m] == error_text_words:
                                # Берем 5 слов до и после, несмотря на старые границы строк
                                start = max(0, i - 5)
                                end = i + m + 5

                                before = words_in_string[start: i]
                                after = words_in_string[i + m: end]

                                error_text_have_five_words_before = before
                                error_text_before = ' '.join(error_text_have_five_words_before)
                                # error_text_before_new = string[start:i]
                                error_text_have_five_words_after = after
                                error_text_after = ' '.join(error_text_have_five_words_after)
                                # error_text_after_new = string[i + m: end]
                                error_info = (f"строка {string_num}: "
                                              f"{error_text_before} {error_text} {error_text_after}")
                                errors_dict[file_name].append(error_info)

    for file_name, path_to_file in files_dict.items():
        if errors_dict[file_name]:
            print(f"\nИСКОМЫЙ ТЕКСТ ({error_text}) БЫЛ НАЙДЕН "
                  f"В ФАЙЛЕ {file_name}: \n" + '\n'.join(errors_dict[file_name]))
        else:
            print(f"По указанному пути отсутствуют ошибки с текстом {error_text}")


def main():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('logsdir_or_logsfile_path', type=str,
                            help='Путь до папки с логами (будут обработаны все файлы в папке) или '
                                 'путь ло конкретного файла с логами (будет обработна только он)')

    arg_parser.add_argument('--text', type=str, help='Текст, который необходимо найти в логах')

    parsed_args = arg_parser.parse_args()

    log_parse(parsed_args.logsdir_or_logsfile_path, parsed_args.text)


if __name__ == "__main__":
    main()
