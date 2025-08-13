from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dictionary():
    return render_template('dictionary.html')

@app.route('/health')
def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
