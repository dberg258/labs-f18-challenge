from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/pokemon/<data>', methods=['GET'])
def main(data):
    try:
        request = requests.get('https://pokeapi.co/api/v2/pokemon/' + data)
    
        if data.isdigit():
            data = "The Pokemon with id " + data + " is " + request['name'].capitalize() + "."
        else:
            data = data.capitalize() + " has id " + str(request['id']) + "."
    
    except requests.exceptions.Timeout as e:
        data = "Cannot find your Pokemon at this time. :("
        print(e)
    except requests.exceptions.TooManyRedirects as e:
        data = "Cannot find your Pokemon at this time. :("
        print(e)
    except json.decoder.JSONDecodeError:
        if data.isdigit():
            data = "Id does not match any Pokemon :("
        else:
            data = "Pokemon does not exist. Make sure spelling is correct (no capital letters) :("

    return render_template('index.html', name=data)


if __name__ == '__main__':
    app.run()
