import pickle
import os
import socket
import psutil
import cpuinfo
import subprocess
import platform
import nmap
import time


def conexao(s):
    (cliente, addrs) = s.accept()
    req = cliente.recv(128).decode('ascii')
    retorno_cliente(cliente, req)

def servidor():
    host = socket.gethostname()
    port = 7777
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sckt.bind((host, port))
    sckt.listen()

    while True:
        conexao(sckt)

    sckt.close()

def retorno_cliente(cliente, msg):
    info = None
    if msg == 'memoria':
        info = informacao_memoria()
    elif msg == 'cpu':
        info = informacao_cpu()
    elif msg == 'disco':
        info = informacao_disco()
    elif 'diretorio' in msg:
        dir = msg.replace('diretorio ', '')
        info = informacao_diretorio(dir)
    elif msg == 'processos':
        info = informacoes_processos()
    elif msg == 'rede':
        info = informacao_rede()
    elif msg == 'hosts':
        info = informacoes_hosts()
    elif 'ports' in msg:
        host = msg.replace('ports', '')
        info = informacao_port(host)

    b = pickle.dumps(info)
    cliente.send(b)


def informacoes_hosts():
    host_ip = socket.gethostbyname(socket.gethostname()).split('.')
    base_ip = ".".join(host_ip[0:3]) + '.'
    host_validos = []
    return_codes = dict()
    for i in range(1, 255):
        return_codes[base_ip + str(i)] = informacao_pings(base_ip + str(i))
        if i % 20 == 0:
            print(".", end="")
        if return_codes[base_ip + str(i)] == 0:
            host_validos.append(base_ip + str(i))
    print("\nMapeamento completo. . . . .")

    return host_validos

def informacao_pings(hostname):
    plataforma = platform.system()
    args = []
    if plataforma == "Windows":
        args = ["ping", "-n", "1", "-l", "1", "-w", "100", hostname]

    else:
        args = ['ping', '-c', '1', '-W', '1', hostname]

    ping = subprocess.call(args, stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
    return ping

def informacao_rede():
    interfaces = psutil.net_if_addrs()
    rede = {}
    for interface in interfaces:
        rede[interface] = []
        for endereco in interfaces[interface]:
            rede[interface].append(
                {'Familia': endereco.family.name, 'Endereço': endereco.address, 'Mascara': endereco.netmask})

    print('Enviando todas as Informações sobre interfaces de rede. . . . . \n')
    return rede
def informacoes_processos():
    processos = []
    for p in psutil.process_iter():
        processos.append(p.as_dict(attrs=['pid', 'name', 'username', 'memory_percent', 'cpu_percent']))

    print('Enviando todas as informações sobre PIDS. . . . .\n')
    return processos


def informacao_diretorio(caminho):
    info_dir = []
    try:
        abspath = os.path.abspath(caminho)
        for item in os.listdir(abspath):
            arq = os.path.join(abspath, item)
            info = os.stat(arq)
            tamanho = info.st_size
            criacao = info.st_ctime
            modificacao = info.st_mtime
            if os.path.isdir(arq):
                tamanho = 0
            info_dir.append(
                {'nome': item, 'tamanho': tamanho, 'Criação': criacao, 'Modificação': modificacao, 'abspath': abspath})
    except:
        info_dir = None
        print('Informações sobre o diretório enviadas...\n')

    return info_dir
def informacao_cpu():
    info = cpuinfo.get_cpu_info()
    print(info)  # Print the info dictionary to see its structure
    cpu = psutil.cpu_percent(interval=0.10, percpu=True)
    modelo = info.get('brand', 'Unknown')  # Access the 'brand' key if present, otherwise return 'Unknown'
    palavra = info['bits']
    arquitetura = info['arch']
    frequencia = psutil.cpu_freq().max
    nucleos = psutil.cpu_count()
    nucleos_fisicos = psutil.cpu_count(logical=False)

    info_cpu = {'modelo': modelo, 'palavra': palavra, 'arquitetura': arquitetura, 'frequencia': frequencia,
                'nucleos': nucleos, 'nucleos_fisicos': nucleos_fisicos, 'cpu': cpu}

    print('Informações sobre o CPU enviadas...\n')

    return info_cpu


def informacao_disco():
    disco = psutil.disk_usage('.').percent
    print('Enviando todas as informações sobre o disco...\n')
    return disco

def informacao_memoria():
    memory = psutil.virtual_memory().percent
    print('Enviando todas as informações sobre memorias . . . . . .\n')
    return memory

def informacao_port(host):
    print('\nEnviando todas as informações do HOST:', host)
    mapPort = nmap.PortScanner()
    mapPort.scan(host)
    list_port = []
    for i in mapPort[host].all_protocols():
        protocolo = i
    openport = mapPort[host][protocolo].keys()
    for port in openport:
        list_port.append(port)
    print('Dados sobre o HOST: {} enviados'.format(host))

    return host, protocolo, list_port

if __name__ == '__main__':
    servidor()