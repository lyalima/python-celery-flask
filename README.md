# Distribuição de tarefas de cotação de criptomoedas com Python, Celery e RabbitMQ e Flask.

O projeto usa a API do site DefiLlama para pegar as cotações de criptomoedas, através do nome da cripto(chain) e do endereço de contrato(address), que podem ser obtidos no site da Coingecko e da EtherScan, e salva essas cotações no banco de dados.

Para distribuição e enfileiramento das tarefas são usados o Celery e o RabbitMQ. 

As tarefas podem ser executadas através da API feita em Flask.

Para instalar as dependências necessárias para usar o projeto, execute: pip install -r./requirements.txt.

Para executar o projeto use: python app.py

Para executar o RabbitMQ use: docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management.

Para executar o Celery use: celery -A core worker -l INFO.
