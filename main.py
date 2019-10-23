from flask import Flask
from flask import send_from_directory
import pygame

app = Flask('app')

@app.route('/')
def hello_world():
  html = '''<!DOCTYPE html>
<html>
  <body>
    <h3>
      ░▓▓▓▓▓░▓▓▓▓▓▓░
      <br>
      ▓▓▓▓░░░░░▓▓░░░░░
      <br>
      ░░▓▓▓▓░░░▓▓░░░░░░
      <br>
      ▓▓▓▓▓░░░░▓▓░░░░
    </h3>
    <audio controls>
      <source src="music.mp3" type="audio/mpeg"></source>
    </audio>
    <ol>
      <li>Coffee</li>
      <li>Tea</li>
      <li>Milk</li>
    </ol>  
  </body>
</html>'''
  return html


@app.route('/music/<path:filename>')
def download_file(filename):
    return send_from_directory('/home/name/Music/', filename)



app.run(host='0.0.0.0', port=8080)
