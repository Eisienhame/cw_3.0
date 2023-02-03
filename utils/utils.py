import requests, json



def load_operations():
    '''
    загружает список вопросов из джейсон файла
    '''
    with open('operations.json', 'r', encoding= 'utf-8') as file:
        operations = json.load(file)
        return operations
