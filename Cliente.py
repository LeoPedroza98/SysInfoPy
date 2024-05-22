import socket
import pickle
import time
import os
import datetime


def cliente_conexao():
    try:
        host = socket.gethostname()
        port = 7777
        socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_tcp.connect((host, port))
    except Exception:
        raise Exception

    return socket_tcp


def menu():
    while True:
        print()
        print('As informações estão sendo capturadas pelo (servidor):', socket.gethostname(), '(',
              socket.gethostbyname(socket.gethostname()), ')')
        print("AT-LEONARDO PEDROZA DE FARIA")
        print('{:>45}'.format('MENU PRINCIPAL'))
        print()
        print('1. Uso de memória')
        print('2. Informações de CPU')
        print('3. Uso de disco')
        print('4. Informações sobre diretórios')
        print('5. Informações de processos')
        print('6. Informações de redes')
        print('0. Sair')

        sair = False

        while True:
            try:
                opcao = int(input('Insira a opção desejada: '))
                print()
            except:
                print('Insira um número válido.')
                continue

            if (opcao == 1):
                informacoes_memoria()
                input('\nEnter para voltar ao menu anterior ')
                os.system("cls")
                break
            elif (opcao == 2):
                os.system("cls")
                menu_sys_cpu()
                break
            elif (opcao == 3):
                pdisco = get_data_servidor('disco')
                if pdisco == None:
                    break
                print_uso_disco(pdisco)
                input('\nEnter para voltar ao menu anterior ')
                os.system("cls")
                break
            elif (opcao == 4):
                caminhos_diretorios()
                break
            elif (opcao == 5):
                processos = get_data_servidor('processos')
                if processos == None:
                    break
                print_processos(processos)
                input('\nEnter para voltar ao menu anterior ')
                os.system("cls")
                break
            elif (opcao == 6):
                os.system("cls")
                menu_sys_rede()
                break

            elif (opcao == 0):
                print('Fechando a aplicação...')
                sair = True
                break
            else:
                print('Opção inválida!')

        if sair: break

#region Ports


def print_host(info_host):
    qtd_host = len(info_host)
    subrede_split = (info_host[0]).split('.')
    subrede = ".".join(subrede_split[0:3]) + '.x'
    print('Foram encontrados {} Hosts na sub-rede: {}'.format(qtd_host, subrede), end='\n\n')
    for i in range(0, qtd_host):
        print(i + 1, '-', info_host[i])
#endregion
#region Memoria
def print_uso_memoria(porcentagem):
    print("Porcentagem de uso de memória em tempo real: {}%".format(porcentagem), end='\r')
    print()


def informacoes_memoria():
    while True:
        porcentagem = get_data_servidor('memoria')
        if porcentagem == None:
            return
        for i in range(5):
            print_uso_memoria(porcentagem)
            time.sleep(0.5)
        print()
        break

def tamanho_memoria(tamanho):
    tam = ''
    tamanho = int(round(tamanho / 1024))
    tam = str(tamanho) + 'KB'
    return tam
#endregion
#region Disco
def print_uso_disco(pdisco):
    print("Porcentagem de uso de disco: {}%".format(pdisco))


def print_diretorio(data):
    print('{:<30}'.format('Nome'), end='')
    print('{:<9}'.format('Tipo'), end='')
    print('{:<13}'.format('Tamanho'), end='')
    print('{:<23}'.format('Criacao'), end='')
    print('{:<23}'.format('Modificação'), end='')
    print('{:<35}'.format('Caminho Absoluto'), end='')
    print()
    for arq in data:
        print('{:<30}'.format(arq['nome']), end='')
        print('{:<9}'.format('Pasta' if arq['tamanho'] == 0 else 'Arquivo'), end='')
        print('{:<13}'.format('' if arq['tamanho'] == 0 else tamanho_memoria(arq['tamanho'])), end='')
        print('{:<23}'.format(datetime.datetime.fromtimestamp(arq['Criação']).strftime('%Y-%m-%d %H:%M:%S')), end='')
        print('{:<23}'.format(datetime.datetime.fromtimestamp(arq['Modificação']).strftime('%Y-%m-%d %H:%M:%S')), end='')
        print('{:<35}'.format(arq['abspath']), end='')
        print()
def caminhos_diretorios():
    input(
        'Abaixo será mostrada informações sobre diretorio em que o "servidor" está sendo executado.\nEnter para continuar...\n')
    info_diretorio = get_data_servidor('diretorio ')
    if info_diretorio == None:
        print('Não foi possível listar o diretório, tente novamente.')
        return
    print_diretorio(info_diretorio)
    input('\nEnter para voltar ao menu anterior ')
    os.system("cls")

#endregion
#region Processos
def print_processos(processos):
    print('{:<6}'.format('PID'), end='')
    print('{:<30}'.format('Nome'), end='')
    print('{:<30}'.format('Usuário'), end='')
    print('{:<25}'.format('Uso de memória'), end='')
    print('{:<25}'.format('Uso de Processamento'), end='')
    print()
    for p in processos:
        pid = p['pid']
        nome = p['name']
        usuario = '--' if p['username'] == None else p['username']
        memory_percent = p['memory_percent']
        cpu_percent = p['cpu_percent']
        print('{:<6}'.format(pid), end='')
        print('{:<30}'.format(nome), end='')
        print('{:<30}'.format(usuario), end='')
        print('{:<25}'.format(round(memory_percent, 2)), end='')
        print('{:<25}'.format(cpu_percent), end='')
        print()
#endregion
# region CPU
def menu_sys_cpu():
    while True:
        print('{:>45}'.format('Informações da CPU'))
        print()
        print('1. Nome e modelo')
        print('2. Arquitetura')
        print('3. Palavra do processador')
        print('4. Frequência')
        print('5. Núcleos')
        print('6. Uso de CPU')
        print('0. Voltar')
        print()

        voltar = False

        while True:
            try:
                opcao = int(input('Insira a opção desejada: '))
                print()
            except:
                print('Insira uma opção válida.\n')
                continue

            if (opcao == 1):
                info_cpu = get_data_servidor('cpu')
                if info_cpu == None:
                    break
                print_modelo_cpu(info_cpu['modelo'])
                input('\nEnter para voltar ao menu anterior ')
                os.system("cls")
                break
            elif (opcao == 2):
                info_cpu = get_data_servidor('cpu')
                if info_cpu == None:
                    break
                print_arquitetura_cpu(info_cpu['arquitetura'])
                input('\nEnter para voltar ao menu anterior ')
                os.system("cls")
                break
            elif (opcao == 3):
                info_cpu = get_data_servidor('cpu')
                if info_cpu == None:
                    break
                print_palavra_cpu(info_cpu['palavra'])
                input('\nEnter para voltar ao menu anterior ')
                os.system("cls")
                break
            elif (opcao == 4):
                info_cpu = get_data_servidor('cpu')
                if info_cpu == None:
                    break
                print_frequencia_cpu(info_cpu['frequencia'])
                input('\nEnter para voltar ao menu anterior ')
                os.system("cls")
                break
            elif (opcao == 5):
                info_cpu = get_data_servidor('cpu')
                if info_cpu == None:
                    break
                print_nucleos_cpu(info_cpu['nucleos'], info_cpu['nucleos_fisicos'])
                input('\nEnter para voltar ao menu anterior ')
                os.system("cls")
                break
            elif (opcao == 6):
                info_cpu = get_data_servidor('cpu')
                if info_cpu == None:
                    break
                print_uso_cpu(info_cpu['cpu'])
                input('\nEnter para voltar ao menu anterior ')
                os.system("cls")
                break
            elif (opcao == 0):
                voltar = True
                os.system("cls")
                break
            else:
                print('Opção inválida!\n')

        if voltar: break

def print_modelo_cpu(modelo):
    print('Modelo:', modelo)


def print_arquitetura_cpu(arquitetura):
    print('Arquitetura:', arquitetura)


def print_palavra_cpu(palavra):
    print('Palavra:', str(palavra) + ' bits')


def print_frequencia_cpu(frequencia):
    print('Frequência:', str(frequencia) + 'Hz')


def print_nucleos_cpu(nucleos, nucleos_fisicos):
    print('Nucleos (físicos):', str(nucleos) + '(' + str(nucleos_fisicos) + ')')


def print_uso_cpu(cpu):
    for n in range(1, len(cpu) + 1):
        print('Porcentagem de uso do núcleo {}:'.format(n), cpu[n - 1], '%')


# endregion
# region Redes
def menu_sys_rede():
    while True:
        print('{:>45}'.format('INFORMAÇÕES DE REDE'))
        print()
        print('1. Interfaces Disponíveis')
        print('2. Hosts disponíveis na sub-rede')
        print('0. Voltar')
        print()

        voltar = False

        while True:
            try:
                opcao = int(input('Insira a opção desejada: '))
                print()
            except:
                print('Insira uma opção válida.\n')
                continue

            if (opcao == 1):
                info_redes = get_data_servidor('rede')
                if info_redes == None:
                    break
                informacoes_redes(info_redes)
                input('\nEnter para voltar ao menu anterior ')
                os.system("cls")
                break
            elif (opcao == 2):
                print('Mapeando favor aguardar...')
                info_host = get_data_servidor('hosts')
                if info_host == None:
                    break
                print_host(info_host)
                input('\nEnter para voltar ao menu anterior ')
                os.system("cls")
                break
            elif (opcao == 0):
                voltar = True
                os.system("cls")
                break
            else:
                print('Opção inválida!\n')

        if voltar: break

def informacoes_redes(data):
    for interface in data:
        print('Lista de endereços da interface', interface)
        print('{:<10}'.format('Família'), end='')
        print('{:<15}'.format('Máscara'), end='')
        print('{:<25}'.format('Endereço'), end='')
        print()
        for endereco in data[interface]:
            print('{:<10}'.format(endereco['Familia']), end='')
            print('{:<15}'.format('--' if endereco['Mascara'] == None else endereco['Mascara']), end='')
            print('{:<25}'.format(endereco['Endereço']), end='')
            print()
        print()
# endregion
def get_data_servidor(mensagem):
    data = None
    try:
        s = cliente_conexao()
        s.send(mensagem.encode('ascii'))
        b = s.recv(16000)

        data = pickle.loads(b)
    except:
        print('Não foi possível abrir uma conexão com o servidor remoto.')
    return data


if __name__ == '__main__':
    menu()