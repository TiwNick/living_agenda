import os

def exibir_opcoes():
    print('1. Create new activity')
    print('2. List activities')
    print('3. Leave\n')

def back_menu():
    input('\nPress any key for back to the menu...')
    main()

def invalid_option():
    print('Please insert a valid option!\n')
    back_menu()

def list_activities():
    pass

def main():
    os.system('cls')
    #exibir_nome_programa()
    exibir_opcoes()
    #escolher_opcao()

if __name__ == '__main__':
    main()