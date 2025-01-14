def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Houve um erro na criação do arquivo.")
    else:
        print(f"arquivo '{nome}' criado com sucesso.")


def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler arquivo.")
    else:
        from utilidadescev.menu import cabecalho

        cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"\033[36m{dado[0]:<30}\033[35m{dado[1]:>3} anos.\033[m")
    finally:
        a.close()

def cadastrar(arq, nome="<DESCONHECIDO>", idade=0):
    try:
        a = open(arq, "at")
    except:
        print("Houve um erro na abertura do arquivo.")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um erro na hora de ESCREVER os dados.")
        else:
            print(f"Novo registro de {nome} adicionado")
            a.close()