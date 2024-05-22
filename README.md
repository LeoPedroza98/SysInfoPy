# SysInfo: Uma Ferramenta Completa para Monitorar e Gerenciar Seus Sistemas

SysInfo é um script Python que fornece uma interface amigável para coletar e visualizar informações detalhadas sobre o seu sistema. Ele é perfeito para administradores de sistema, entusiastas de computadores e qualquer pessoa que queira ter um controle mais preciso do desempenho e da saúde do seu computador.

## Funcionalidades

- **Informações de Memória**: Monitora o uso de memória em tempo real, incluindo porcentagem de uso, memória disponível e total.
- **Informações da CPU**: Exibe detalhes sobre o modelo, arquitetura, palavra, frequência, núcleos e uso da CPU.
- **Informações do Disco**: Mostra o uso do disco em porcentagem, espaço livre e total.
- **Informações de Diretórios**: Lista os arquivos e pastas em um diretório específico, incluindo nome, tipo, tamanho, data de criação e modificação.
- **Informações de Processos**: Exibe uma lista de processos em execução, incluindo PID, nome, usuário, uso de memória e uso da CPU.
- **Informações de Rede**: Mostra detalhes sobre as interfaces de rede disponíveis, incluindo endereços IP, máscaras de sub-rede e gateways.
- **Verificação de Portas Abertas**: Permite verificar se há portas abertas em um host específico.
- **Detecção de Hosts na Rede**: Encontra hosts ativos na sua rede local.
- **Interface de Menu Intuitiva**: Navegue facilmente pelas opções e visualize as informações de forma organizada.

## Pacotes Utilizados

- `socket`: Cria sockets para comunicação com o servidor.
- `pickle`: Serializa e desserializa dados para envio e recebimento.
- `psutil`: Acessa informações sobre o sistema, como uso de memória, CPU e disco.
- `cpuinfo`: Obtém informações detalhadas sobre a CPU.
- `subprocess`: Executa comandos do sistema operacional.
- `platform`: Identifica a plataforma do sistema operacional.
- `nmap`: Realiza mapeamento de portas em hosts remotos.
- `os`: Fornece funções para trabalhar com o sistema operacional, como listar diretórios e arquivos.
- `datetime`: Converte datas e horários para formatos legíveis.

## Como Usar
1. Clone o repositório:
    ```
    git clone https://github.com/intel/CommsPowerManagement/blob/master/power.md
    ```
2. Instale os pacotes necessários:
   ```
   pip install -r requirements.txt
   ```
3. Execute os script:
  ```
  python Cliente.py
  ```
  ```
  python Servidor.py
  ```
