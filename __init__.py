from flask import Flask, render_template
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as CImage

app = Flask(__name__)
CLARIFAI_APP_ID = 'H2EWeFlad0JQkoyO7KpKKrJRvw_4x_hCIVfb8tgk'
CLARIFAI_APP_SECRET = 'ROFbJfmbRVd6SsH7Xv1MfloxjqM4yZSod-Ul-ITG'
appy = ClarifaiApp(CLARIFAI_APP_ID, CLARIFAI_APP_SECRET)
appy.auth.get_token()
def getColors():
    model = appy.models.get('eeed0b6733a644cea07cf4c60f87ebb7')
    image = CImage(url='https://samples.clarifai.com/metro-north.jpg')
    data = model.predict([image])
    outputs = data['outputs']#['data']#['colors'][0]['raw_hex']
    data = outputs[0]
    data = data['data']['colors']
    color = data[0]
    color = color['raw_hex']
    return color

@app.route("/")
def hello():
    return render_template("index.html", color=getColors())

def main():
    hello()


if __name__ == "__main__":
    app.run('127.0.0.1', 5007, debug=True)
