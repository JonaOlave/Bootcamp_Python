def banner():
    '''
    Pueden modificar el nombre del sistema a gusto :) !!!
    '''
    banner1='Bienvenidos a nuestro sistema'
    banner2='Awake-ERP'
    punteada = ('-'*35)
    espacio = (' '*35)
    espacio_banner1 = (' '*3)
    espacio_banner2 = (' '*13)

    print("+"+ punteada +"+")
    print("|"+ espacio +"|")
    print("|"+(espacio_banner1 + banner1 + espacio_banner1)+"|")
    print("|"+(espacio_banner2 + banner2 + espacio_banner2)+"|")
    print("+"+ punteada +"+")

if __name__ == "__main__":
    banner()