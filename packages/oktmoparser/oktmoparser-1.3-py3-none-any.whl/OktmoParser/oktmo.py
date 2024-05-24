import csv
import json
import re
import requests


class OktmoParser():

    def __init__(self):
        self.url = 'https://rosstat.gov.ru/opendata/7708234640-oktmo'
        self.file_name = 'data.csv'

    def parse_oktmo(self, start_keyword, end_keyword):

        response = requests.get(self.url)

        if response.status_code == 200:

            match = re.search(r'<a href="(https://rosstat\.gov\.ru/opendata/7708234640-oktmo/data-[^\"]+)"', response.text)

            if match:
                download_url = match.group(1)
                print(f'Найдена ссылка для скачивания: {download_url}')

                file_response = requests.get(download_url)

                if file_response.status_code == 200:

                    with open(self.file_name, 'wb') as f:
                        f.write(file_response.content)
                    print('Файл успешно загружен, формирую результат в формате JSON')

                    encoding = 'windows-1251'
                    data_found = False
                    result_data = {}
                    try:
                        with open('data.csv', newline='', encoding=encoding) as csvfile:
                            csvreader = csv.reader(csvfile, delimiter=';')
                            for row in csvreader:
                                if data_found and row[6] != end_keyword:
                                    oktmo_code = row[0] + ' ' + row[1] + ' ' + row[2]
                                    if row[3] != '000':
                                        oktmo_code += ' ' + row[3]
                                    settlement_name = row[6]
                                    result_data[settlement_name] = {
                                        'ОКТМО': oktmo_code,
                                        'КЧ': row[4]
                                    }
                                if row[6] == start_keyword:
                                    data_found = True
                                elif row[6] == end_keyword:
                                    data_found = False
                                    break
                    except UnicodeDecodeError:
                        print(f'Не удалось прочитать файл с кодировкой {encoding}')

                    with open('result.json', 'w') as json_file:
                        json.dump(result_data, json_file, ensure_ascii=False, indent=4)
                        print('Готово')
                else:
                    print('Не удалось загрузить файл')
            else:
                print('Ссылка на файл не найдена')
        else:
            print('Не удалось получить доступ к странице')
