import os


# input recursivo dos caminhos dos arquivos
def input_caminhos():
    caminhos = []
    while True:
        caminho = input('Digite o caminho do arquivo: ')
        if caminho == '':
            break
        caminhos.append(caminho)
    return caminhos


# verifica se o arquivo existe
def verifica_arquivo(caminhos):
    for i in caminhos:
        if os.path.exists(i):
            return True
        else:
            return False

# verifica se os caminhos dos arquivos são vazios
def verifica_vazio(path):
    for i in path:
        if os.path.exists(i):
            with open(i, 'r') as arquivo:
                if arquivo.read() == '':
                    return True
                else:
                    return False
        else:
            return False


def ler_arquivo(path):
    for i in path:
        with open(path, 'r') as arquivo:
            return arquivo.read()


# copiar cada linha de cada arquivo para uma lista
# tirar todos os caracteres '\n'
# ordenar a lista
# escrever a lista em um arquivo novo com o nome 'juncao.txt' com um item em cada linha
def ler_arquivo_lista(caminhos):
    lista = []
    for i in caminhos:
        with open(i, 'r') as arquivo:
            for linha in arquivo:
                lista.append(linha.strip())
    sorted(lista)
    return lista


def juncao_arquivos(caminhos):
    lista = sorted(ler_arquivo_lista(caminhos))
    with open('final.txt', 'w') as arquivo:
        for i in lista:
            arquivo.write(i + '\n')
    print('Arquivo final.txt criado com sucesso!')


#desativei os input para conseguir testar o programa
caminhos = []


def juncao(caminhos):
    if verifica_arquivo(caminhos) == True and verifica_vazio(caminhos) == False:
        juncao_arquivos(caminhos)
    else:
        print('Impossível criar arquivo final.txt')
        return 'Impossível criar arquivo final.txt'


juncao(caminhos)
