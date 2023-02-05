import requests, json



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
    w = []
    for i in x:
            if 'state'in i and i['state'] == 'EXECUTED' and "from" in i:
                w.append(i)
    return w

