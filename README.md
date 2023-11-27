# Aplicação de Previsão do Tempo
Este repositório contém uma aplicação de backend em Python que realiza consultas de previsão do tempo utilizando a API do OpenWeatherMap, com gravação do histórico de chamadas em banco de dados Redis.

1. Clone este repositório:
```
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

2. Instale as dependências:
```
pip install flask
pip install redis
```

3. Configure a Chave de API do OpenWeatherMap:

    - Crie uma conta em https://openweathermap.org/ e obtenha sua chave de API gratuita.
    - Substitua 'SUA_API_KEY' pela sua chave de API no arquivo main.py.

4. Instale e inicie o servidor Redis:

    - Certifique-se de ter o Redis instalado. [Instruções de instalação do Redis](https://redis.io/download/)
    - Inicie o servidor Redis.

5. Execute a aplicação:
```
python app.py
```
A aplicação estará acessível em http://127.0.0.1:5000/.

## Uso da API
### Obter Previsão do Tempo
Endpoint: /weather

Parâmetros:

- 'city' (obrigatório): Nome da cidade para a qual você deseja obter a previsão do tempo.
Exemplo de requisição:

```
http://127.0.0.1:5000/weather?city=New%20York
```
### Consultar Histórico de Chamadas
Endpoint: /history

Exemplo de requisição:

```
http://127.0.0.1:5000/history
```
### Contribuição
Sinta-se à vontade para contribuir com críticas, melhorias, correções de bugs ou novos recursos.
