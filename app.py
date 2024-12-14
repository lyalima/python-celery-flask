from flask import Flask, request, jsonify
from tasks import get_price_crypto


app = Flask(__name__)

@app.route('/crypto_price', methods=['POST'])
def crypto_price():
    data = request.get_json()
    crypto_chain = data.get('crypto_chain')
    crypto_address = data.get('crypto_address')

    if not crypto_chain:
        return jsonify({'error': 'Nome da criptomoeda é necessário'}), 400
    
    get_price_crypto.delay(crypto_chain, crypto_address)

    return jsonify({'message': 'Requisição processada com sucesso!'}), 200


if __name__ == '__main__':
    app.run(debug=True)
