from utils.utils import load_operations, ex_operations, last_values, edited_data



def main():
    '''
    Основная фукция

    '''

    x = edited_data(last_values(ex_operations(load_operations()), 5))

    for i in x:
        print(i)
        print()

main()

