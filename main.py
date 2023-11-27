from flask import Flask, jsonify, request
import requests
import json
from datetime import datetime
import redis

app = Flask(__name__)

# OpenWeatherMap ID
API_KEY = 'SUA_API_KEY'

# Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

@app.route('/weather', methods=['GET'])
def get_weather():
    # Nome da cidade através da query string 'city'
    city = request.args.get('city')

    if not city:
        return jsonify({'error': 'Informe a cidade para realizar a consulta.'}), 400
  
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}  # 'units' para temperatura em Celsius

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return jsonify({'error': 'Erro ao realizar consulta no servidor, tente novamente.'})

    
    data = response.json()

    # Gravação do histórico das consultas no Redis
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    history = 'history:' + timestamp + ' / ' + city
    redis_client.set(history, json.dumps({'timestamp': timestamp, 'city': city}))

    # Retorno da previsão
    return jsonify(data)

@app.route('/history', methods=['GET'])
def get_history():
    # Get do histórico no redis
    history_key = redis_client.history_key('history:*')

    history_entries = [json.loads(redis_client.get(hk)) for hk in history_key]

    return jsonify(history_entries) # Retorno do histórico (json)

if __name__ == '__main__':
    app.run(debug=True)
