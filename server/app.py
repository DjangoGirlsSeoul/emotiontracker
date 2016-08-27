from flask import Flask, request, render_template, send_from_directory, redirect, url_for, abort
from werkzeug.contrib.cache import SimpleCache

songs = [{"speed" : 1, "notes" : ['a','b','c','g'] }, {"speed" : 1, "notes" : ['b','c','c','g'] }]
WEBCAM_SPEED = 1

app = Flask(__name__)
cache = SimpleCache()
cache.set('webcam_speed', 1)

@app.route('/')
def main():
    return render_template('index.htm', level=0)

@app.route('/piano')
def piano():
    return render_template('piano.html', level=0)


@app.route('/level/<int:level>')
def play_level(level):
    if level < 5:
        return render_template('index.htm', level=level)
    else:
        return render_template('win.html')

##{'[{"emotion":"angry","value":0.03350348808431149},{"emotion":"sad","value":0.31215305776434915},{"emotion":"surprised","value":0.16222857011091235},{"emotion":"happy","value":0.04008017326503987}]': u''}
# @app.route('/emotions', methods=['POST'])
def get_emotions():
    emotions = request.get_json()
    happy_point = request.json[3]['value']
    if happy_point < 0.3:
        cache.set('webcam_speed', 2)
    return 'Hello World!'

@app.route('/answers', methods=['POST'])
def check_answers():
    # {level: 1, answers: ['a', 'b', 'c', 'g']}
    
    answers_level = request.get_json()
    print(answers_level);
    current_level = answers_level['level']
    answers = answers_level['answers']
    if songs[current_level]['notes'] == answers:
        print('pass!')
        return redirect(url_for('play_level', level=current_level + 1))
    else:
        abort(404)
        print('FIAIL')
        return render_template('fail.html')



@app.route('/index_files/<path:path>')
def send_js(path):
    return send_from_directory('templates/index_files', path)


if __name__ == '__main__':
    app.run()
