# Aplicativo de Rastreamento de Preços de Criptomoedas

## Descrição do Projeto

Este projeto é um aplicativo de rastreamento de preços de criptomoedas em Python. Ele utiliza a API do CoinGecko para obter informações em tempo real sobre os preços de várias criptomoedas. Os usuários podem definir alertas de preço e ser notificados quando uma criptomoeda específica atingir o valor desejado.

## Estrutura do Projeto

- O projeto é dividido em quatro componentes principais:

crypto_api.py: Responsável por fazer requisições à API do CoinGecko para obter preços de criptomoedas.
alert_system.py: Gerencia os alertas de preço com base nos valores fornecidos pelo usuário.
user_interface.py: Interface do usuário para interagir com o aplicativo, permitindo definir a criptomoeda de interesse e o preço-alvo para o alerta.
main.py: Arquivo principal que integra todos os módulos e executa o aplicativo.

##Pré-requisitos
Python 3.x
Acesso à Internet

##Como Instalar
Clone o repositório ou faça o download dos arquivos crypto_api.py, alert_system.py, user_interface.py e main.py.
Certifique-se de que o Python está instalado em sua máquina.

##Como Executar
Abra um terminal ou prompt de comando.
Navegue até o diretório onde os arquivos do projeto estão salvos.
Execute o aplicativo com o comando python main.py ou python3 main.py.
Siga as instruções na tela para definir a criptomoeda e o preço-alvo para o alerta.

##Funcionalidades
Consulta em tempo real os preços de diversas criptomoedas usando a API do CoinGecko.
Permite ao usuário definir um preço-alvo para uma criptomoeda específica.
Notifica o usuário quando o preço da criptomoeda atinge o valor definido no alerta.

##Licença
Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes (se aplicável).
