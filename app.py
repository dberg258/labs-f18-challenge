from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/pokemon/<data>', methods=['GET'])
def main():
    request = requests.get('https://pokeapi.co/api/v2/pokemon/' + data)
    return render_template('index.html', name=request)


if __name__ == '__main__':
    app.run()
