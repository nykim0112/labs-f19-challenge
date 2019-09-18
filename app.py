from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<query>')
def pokemon_info(query):
    request_url="https://pokeapi.co/api/v2/pokemon/"+str(query)+"/"
    response = requests.get(request_url)

    # for debugging purposes
    # print(response.status_code)

    decoded_response = json.loads(response.text)

    if ( query.isdigit() ):
        return "The pokemon with id " + str(query) + " is " + decoded_response['name']

    elif ( type(query) == str ):
        return str(query) + " has id " + str(decoded_response['id'])

    else:
        return "404: Pokemon not found. Please check if you have typed in the correct information."

if __name__ == '__main__':
    app.run()
