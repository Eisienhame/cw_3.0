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
    for i in x:
        for o in i:
            if o['state'] == 'EXECUTED' and i[2]['from'] is True:
                print(i)

kol = load_operations()
ex_operations(kol)