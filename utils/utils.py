import requests, json
from datetime import datetime


def load_operations():
    '''
    загружает список вопросов из джейсон файла
    '''
    with open('operations.json', 'r', encoding= 'utf-8') as file:
        operations = json.load(file)
        return operations

def ex_operations(x):
    '''
    Выбирает из списка пройденные операции и формирует новый список
    :return:
    '''
    work_list = []
    for i in x:
            if 'state' in i and i['state'] == 'EXECUTED' and "from" in i:
                work_list.append(i)
    return work_list

def last_values(data, how_much=None):
    '''
    Фуц-ия для сортировки списка по дате и получения последих how_much значений

    '''
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    data = data[:how_much]
    return data

def edited_data(x):
    '''
    Изменяем вх данные под необходимый формат и заполяем форму на выход

    '''
    finished_data = []

    for i in x:
        ed_date = datetime.strptime(i["date"], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        ed_description = i["description"]
        from_data = i["from"].split()
        ed_accont_number = from_data.pop(-1)
        if len(ed_accont_number) == 16:
            ed_accont_number = f'{ed_accont_number[:4]} {ed_accont_number[4:6]}** **** {ed_accont_number[-4:]}'
        else:
            ed_accont_number = f'**{ed_accont_number[-4:]}'

        ed_from_name = ' '.join(from_data)

        to_data = i["to"].split()
        ed_to_number = to_data.pop(-1)
        if len(ed_to_number) == 16:
            ed_to_number = f'{ed_to_number[:4]} {ed_to_number[4:6]}** **** {ed_to_number[-4:]}'
        else:
            ed_to_number = f'**{ed_to_number[-4:]}'

        ed_to_name = ' '.join(to_data)


        ed_amount_money = f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}'

        finished_data.append(f'''{ed_date} {ed_description}
{ed_from_name} {ed_accont_number} -> {ed_to_name} {ed_to_number}
{ed_amount_money}''')

    return finished_data

