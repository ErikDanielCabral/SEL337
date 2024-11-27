**Funcionamento do projeto - Resumo:** O intuito é utilizar uma unidade de serviço personalizada (blink_9703.service) para iniciar automaticamente um programa simples em python (blink.py) capaz de piscar um LED, conforme a inicialização (boot) do sistema operacional instalado em uma RaspberryPi.  

**"Boot" da RaspberryPi:** Resumido nas quatros etapas abaixo, o processo todo demora poucos segundos.

  1.Bootloader:
    A Raspberry Pi inicia carregando um bootloader primário armazenado na memória ROM. Este bootloader localiza e carrega o segundo estágio do boot a partir do cartão SD.

  2.Carregamento de Firmware:
    Os arquivos de firmware necessários (como bootcode.bin e start.elf) são carregados no processador para inicializar os componentes básicos, incluindo a GPU e a CPU.
  
  3.Kernel Linux:
  O kernel do sistema operacional é carregado e inicializado, incluindo os módulos necessários para dispositivos e periféricos.

  4.Init System: 
  Após o kernel ser carregado, o sistema inicia o processo init, responsável por configurar e gerenciar os serviços e processos necessários para o funcionamento do sistema operacional.

**Init System e systemd:** Existem vários sistemas de init disponíveis, mas o mais comum nas distribuições Linux modernas, incluindo as utilizadas pela Raspberry Pi, é o systemd.  Este, que por sua vez, é um sistema de inicialização moderno e eficiente, usado para gerenciar serviços no Linux. Suas principais características seguem listadas.

  1.Gerenciamento de Serviços: Usa arquivos .service para definir como e quando um programa ou serviço deve ser iniciado.

  2.Execução Paralela: Permite inicializar vários serviços simultaneamente, acelerando o processo de boot.

  3.Controle de Dependências: Garante que os serviços sejam iniciados na ordem correta, conforme suas dependências.

  4.Facilidade de Configuração: Arquivos .service são simples de criar e configurar.

**Video demonstrativo:** https://drive.google.com/file/d/1o-oIDu36a_8VTKZhXwdbr--EnUdmUie5/view?usp=sharing

**Códigos comentados - blink.py**

*from gpiozero import LED*  # Importa a classe LED da biblioteca gpiozero, que facilita o controle de GPIOs na Raspberry Pi.
*from time import sleep*    # Importa a função sleep, usada para criar pausas entre as ações.

*PinLed = LED(25)*          # Cria um objeto LED associado ao pino GPIO 25 da Raspberry Pi. Este pino deve estar conectado ao LED.

*while True:*              # Inicia um loop infinito que será executado continuamente.

  *PinLed.on()*           # Liga o LED, enviando um sinal HIGH (3,3V) ao pino GPIO 25.
  
  *print("LED aceso")*    # Imprime no terminal que o LED está aceso.
  
  *sleep(1)*              # Aguarda por 1 segundo antes de continuar.

  *PinLed.off()*         # Desliga o LED, enviando um sinal LOW (0V) ao pino GPIO 25.
  
  *print("LED apagado")*  # Imprime no terminal que o LED está apagado.
  
  *sleep(1)*              # Aguarda por 1 segundo antes de reiniciar o loop.

**Códigos comentados - blink_9703.service**

*[Unit]*

*Description=LED Blink Service*          # Uma descrição para o serviço, que aparecerá ao listar os serviços.
*After=multi-user.target*                # Define que o serviço será iniciado apenas depois que o sistema alcançar o estado "multi-user",

*[Service]*

*Type=simple*                            # Define que o serviço será considerado ativo enquanto o comando especificado no ExecStart *estiver em execução.*
*User=sel*                               # Define o usuário que executará o serviço. Neste caso, o usuário é "sel".
*ExecStart=/usr/bin/python /home/sel/pi/blink.py* #Utiliza o python para rodar o scrpit com esse nome neste diretório
  
*#ExecStop=/usr/bin/python /home/sel/pi/cleanup.py* # Encerra o serviço.

*Restart=on-failure*                     # Configura o serviço para reiniciar automaticamente se ele falhar.
*WorkingDirectory=/home/sel/pi*          # Define o diretório de trabalho para o serviço.

*[Install]*

*WantedBy=multi-user.target*             # Indica que este serviço será iniciado no nível de execução "multi-user",
                                    




