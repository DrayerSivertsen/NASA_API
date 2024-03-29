#!/usr/bin/env python3 # called a shabang line used to show how to execute, when user runs give file to python
import urllib.request
import json
import webbrowser
import urllib
from flask import Flask, render_template
from PIL import Image
import base64
import io



app = Flask(__name__)

# Define APOD
apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=ZuohWEJ9pX59O6nuwvw0EvkYgN2EOdkkSZagtn7x'

# Call the webservice
apodurlobj = urllib.request.urlopen(apodurl + mykey + "&date=2015-01-26")

# read the file-like object
apodread = apodurlobj.read()

# decode json to python data structure
decodeapod = json.loads(apodread.decode('utf-8'))

# display our pythonic data
print("\n\nConverted python data")
print(decodeapod)

# use web browser to open the HTTPS URL
#input('\nPress Enter to open NASA Picture of the Day in Google')
#webbrowser.open(decodeapod['url'])


image_url = str(decodeapod['url'])
name = decodeapod['explanation']
title = str(decodeapod['title'])

@app.route('/')
def image():
    return render_template("index.html", image_url=image_url)

@app.route('/description')
def des():
    return render_template("description.html", explanation=name, title=title)



if __name__ == '__main__':
    app.run()