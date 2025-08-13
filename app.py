from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def dictionary():
    return render_template('dictionary.html')

@app.route('/ads.txt')
def ads_txt():
    return send_from_directory('.', 'ads.txt')

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory('.', 'robots.txt')

@app.route('/robots_google.txt')
def robots_google_txt():
    return send_from_directory('.', 'robots_google.txt')


@app.route('/health')
def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
