from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    # Pythonプログラム「CPI.py」を実行
    result = subprocess.run(['python', 'CPI.py'], capture_output=True, text=True)
    # 実行結果をHTMLで表示
    return render_template('index.html', result=result.stdout)

if __name__ == '__main__':
    app.run(debug=True)
