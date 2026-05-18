# Criando uma interface gráfica no Debian

O presente trabalho tem como objetivo a criação de uma interface gráfica em uma máquina virtual com sistema operacional Debian "só texto" (versão 6.12.74). Tenha em mente que o código em si não é nada complexo; utilizo somente alguns componentes básicos da biblioteca Custom Tkinter, do Python, a fim de criar um programa simples para teste da interface gráfica.
## Preparando a máquina virtual

### 1. Instale o Python em sua máquina virtual

* Inicialmente, verifique se há atualizações: execute [ apt update ].
* Caso exista alguma atualização a ser realizada: execute [ apt upgrade ]; provavelmente o sistema buscará sua validação do projeto, caso peça, digite 's' e clique ENTER.
* Agora, para baixar efetivamente o Python: execute [ apt install python3 ].
* Verifique a instalação: execute [ python3 --version ].
* Instale o gerenciador de pacotes do Python: execute [ apt install python3-pip ].

### 2. Instale a biblioteca Custom Tkinter em sua máquina virtual

* Baixe o CutomTkinter: execute [ apt install python3-tk ].
* Baixe o CustomTkinter globalmente no sistema: execute [ pip3 install customtkinter --break-system-packages ].
* Baixe também a biblioteca Pillow (para carregamento de imagens): execute [ apt install python3-pil ].

### 3. Instale o servidor gráfico que irá 'abrir a janela'

* Baixe o servidor: execute [ apt install xong openbox -y ].

### 4. Configure o mecanismo de "disparo" da interface gráfica

* Na pasta (/root): execute [ nano ~/.xinitrc ].
* Dentro do arquivo .xinitrc, escreva o seguinte comando: [ openbox-session & python3 /local-do-arquivo-python-do-seu-programa/arquivo.py ].
* Salve as alterações do arquivo e volte ao terminal.

### 5. Execute o programa

* No terminal: execute [ startx ].

O servidor gráfico tomará para si a gestão dos pixels da tela e executará a interface gráfica gerada pala biblioteca CustomTkinter.
