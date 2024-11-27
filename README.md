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


                                   




