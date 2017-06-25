from flask import Flask, render_template, request
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as CImage
import getPics

app = Flask(__name__)
CLARIFAI_APP_ID = 'H2EWeFlad0JQkoyO7KpKKrJRvw_4x_hCIVfb8tgk'

def getData(model, venues):
    venueColorDict = {}
    for x in range(len(venues)):
        image = CImage(url=venues[x][1])
        imageData = model.predict([image])
        colors = imageData['outputs'][0]['data']['colors'] #current color palette
        colorPalette =[]
        for y in range(len(colors)):
            colorPalette.append(colors[y]['raw_hex'])
        venueColorDict[venues[x][0]] = colorPalette
    return venueColorDict

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/submitCity', methods=['GET', 'POST'])
def getCity():
    cityName = request.form['city']

    CLARIFAI_APP_SECRET = 'ROFbJfmbRVd6SsH7Xv1MfloxjqM4yZSod-Ul-ITG'
    appy = ClarifaiApp(CLARIFAI_APP_ID, CLARIFAI_APP_SECRET)
    appy.auth.get_token()
    model = appy.models.get('eeed0b6733a644cea07cf4c60f87ebb7')
    venues = getPics.getVenues(cityName)

    return render_template("index.html", colorDict=getData(model, venues))

if __name__ == "__main__":
    app.run('127.0.0.1', 5007, debug=True)
