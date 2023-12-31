#Funçao que irá ler o input int do usuario
def leiaInt(msg):
    color1="\033[1;32m"
    color0="\033[m"

    while True:
        try:
            n=int(input(msg))
        except (ValueError,TypeError):
            print(f"{color1}Por favor, digite somente numeros!{color0}")
            continue
        except KeyboardInterrupt:
            print(f"{color1}\nUsuario preferiu não digitar esse numero!{color0}")
            return 0
        else:
            return n

#Função cosmetica que irá inserir linhas
def linha(tam=42):
    return "-" * tam

#Função cosmetica que irá formatar textos
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

#Função que irá reproduzir de forma formatada um menu
def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c=1
    for item in lista:
        print(f"{c} - {item}")
        c+=1
    print(linha())
    opc = leiaInt("Sua opção: ")
    return opc
