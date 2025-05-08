def arqExiste(nome):
    try:
        a=open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(nome):
    try:
        a=open(nome, 'wt+')
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo ({nome}) criado com sucesso.')


def lerArq(nome):
    try:
        a=open(nome, 'rt')
    except:
        print('Houve um erro ao ler o arquivo!')
    else:
        for linha in a:
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n', '')
            print(f'{dado[0]:.<25}{dado[1]:>3} anos')
        a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a=open(arquivo, 'at')
    except:
        'ERRO'
    else:
        a.write(f'{nome};{idade}\n')
        print('Usuário adicionado com sucesso!')
        a.close()
