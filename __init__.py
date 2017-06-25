from flask import Flask, render_template
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as CImage

import getPics

app = Flask(__name__)
CLARIFAI_APP_ID = 'H2EWeFlad0JQkoyO7KpKKrJRvw_4x_hCIVfb8tgk'
CLARIFAI_APP_SECRET = 'ROFbJfmbRVd6SsH7Xv1MfloxjqM4yZSod-Ul-ITG'
appy = ClarifaiApp(CLARIFAI_APP_ID, CLARIFAI_APP_SECRET)
appy.auth.get_token()
model = appy.models.get('eeed0b6733a644cea07cf4c60f87ebb7')

venues = getPics.getVenues("New York")


def getData():
    images =[]
    jsondata =[]
    for x in range(len(venues)):
        image = CImage(url=venues[x][1])
        jsondata.append(model.predict([image]))
    return jsondata

def getColors(data):
    colors=[]
    names=[]
    for x in range(len(data)):
        current = data[x]
        currentColorPalette = current['outputs'][0]['data']['colors']
        currentNameList = current['outputs'][0]['data']['colors']
        for y in range(len(currentColorPalette)):
            colors.append(currentColorPalette[y]['raw_hex'])
            names.append(currentNameList[y]['w3c']['name'])
    return colors, names

@app.route("/")
def hello():
    data = getData()
    return render_template("index.html", colorObjects=getColors(data))

def render():
    hello()


if __name__ == "__main__":
    app.run('127.0.0.1', 5007, debug=True)
