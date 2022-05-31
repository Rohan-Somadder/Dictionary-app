'''
Dictionary App
API used - Free Dictionary API
Link - https://dictionaryapi.dev/

#TODO : None
'''


from word import Word


LINK = 'https://api.dictionaryapi.dev/api/v2/entries/en/'


def menu():
    '''
    Displays the menu
    '''
    print('\n', ''.center(80, '='), sep='\n')
    print('DICTIONARY APP'.center(80, '-'))
    print(''.center(80, '='))
    print('\n', 'MENU'.center(80, '-'), sep='\n')
    print('1. WORD MEANING')
    print('2. EXAMPLES')
    print('ELSE : EXIT')


def main():
    '''
    Main function
    '''
    menu()
    try:
        choice = int(input("ENTER CHOICE : "))
    except ValueError:
        choice = -1
    input_w = input("Enter the word : ")
    word = Word(input_w, LINK)
    if choice == 1:
        word.word_meanings()
    elif choice == 2:
        pass


if __name__ == "__main__":
    main()
