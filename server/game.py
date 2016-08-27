import signal
from audio import play_audio
import threading

WEBCAM_SPEED = 1

class AlarmException(Exception):
    pass

class Game:
    def alarmHandler(self, signum, frame):
        raise AlarmException

    def nonBlockingRawInput(self, prompt='', timeout=5):
        signal.signal(signal.SIGALRM, self.alarmHandler)
        signal.alarm(timeout)
        try:
            text = raw_input(prompt)
            signal.alarm(0)
            return text
        except AlarmException:
            print '\nPrompt timeout. Continuing...'
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''

    def play_level(self, song):
        score = 0
        success_score = len(song["notes"]) * 0.8
        for note in song["notes"]:
            # send(note)
            threading.Thread(target=play_audio, kwargs={'audio_file_location': 'audio_files/ox.wav'}).start()
            print('asdasdasasda')
            print(note)
            input_note = self.nonBlockingRawInput("note: ", song["speed"] * WEBCAM_SPEED)

            if input_note == note :
                score += 1

        if score >= success_score :
            print("score: {}".format(score))
            print("success")
            return True
        else :
            print("score: {}".format(score))
            print("fail")
            return False

    def start(self, songs):
        for idx,song in enumerate(songs):
            print("level : {}".format(idx+1))
            passing = self.play_level(song)
            if not passing:
                print("You failed!!!!!!!!!!!!")
                exit()

g = Game()
g.start(
    [
    {"speed" : 1, "notes" : ['a','b','c','g'] }, 
    {"speed" : 1, "notes" : ['b','c','c','g'] }
    ]
    )
