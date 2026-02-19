from flask import Flask, render_template, request, jsonify
import fraud  

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main web interface."""
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    """Handle the phishing detection request from the web form."""
    try:
        
        client_id = request.form['client_id']
        client_secret = request.form['client_secret']
        date_time = request.form['date_time']
        sender = request.form['sender']
        receiver = request.form['receiver']
        locale = request.form['locale']

        
        if 'file_path' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        file = request.files['file_path']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        if not file.filename.endswith('.wav'):
            return jsonify({"error": "Only WAV files are supported"}), 400

        
        token = fraud.get_bearer_token(client_id, client_secret)

        
        result = fraud.detect_phishing(file, date_time, sender, receiver, locale, token)

        
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)