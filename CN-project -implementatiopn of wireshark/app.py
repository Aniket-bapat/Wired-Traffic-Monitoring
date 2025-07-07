from flask import Flask, render_template, request, redirect, url_for
import subprocess
import sys 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_capture', methods=['POST'])
def start_capture():
    subprocess.Popen([sys.executable, 'scripts/traffic_sniffer.py']) 
    return redirect(url_for('index'))

@app.route('/analyze', methods=['POST'])
def analyze():
    subprocess.run([sys.executable, 'scripts/analyze_capture.py'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
