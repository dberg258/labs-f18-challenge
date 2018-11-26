from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/pokemon/<data>', methods=['GET'])
def main(data):
    request = requests.get('https://pokeapi.co/api/v2/pokemon/' + data)
    
    if data.isdigit():
        data = "The Pokemon with id " + data + " is " + request['name'].capitalize() + "."
    else:
        data = data.capitalize() + " has id " + str(request['id']) + "."

    return render_template('index.html', name=data)


if __name__ == '__main__':
    app.run()
