from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json # Mendapatkan data JSON dari permintaan POST
    print("Recieve webhook data", data)

    # Lakukan sesuatu dengan data yang diterima
    # Misalnya, kirim respons sederhana
    response = {"status": "success", "message": "Webhook data received"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)