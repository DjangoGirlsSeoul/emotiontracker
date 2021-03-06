from flask import Flask, request, render_template, send_from_directory
from werkzeug.contrib.cache import SimpleCache
from game import Game

# songs = [{"speed" : 1, "notes" : ['a','b','c','g'] }, {"speed" : 1, "notes" : ['b','c','c','g'] }]
WEBCAM_SPEED = 1

app = Flask(__name__)
cache = SimpleCache()
cache.set('webcam_speed', 1)

@app.route('/')
def main():
    g = Game()
    g.run()
    return render_template('index.htm')

##{'[{"emotion":"angry","value":0.03350348808431149},{"emotion":"sad","value":0.31215305776434915},{"emotion":"surprised","value":0.16222857011091235},{"emotion":"happy","value":0.04008017326503987}]': u''}
@app.route('/emotions', methods=['POST'])
def get_emotions():
    emotions = request.get_json()
    happy_point = request.json[3]['value']
    if happy_point < 0.3:
        cache.set('webcam_speed', 2)
    return 'Hello World!'


@app.route('/index_files/<path:path>')
def send_js(path):
    return send_from_directory('templates/index_files', path)


if __name__ == '__main__':
    app.run()
