import signal
import subprocess
import curses
import curses.ascii
import time
import threading

stdscr = curses.initscr()
curses.cbreak()
curses.halfdelay(10) # 10/10 = 1[s] inteval

# songs = [{"speed" : 1, "notes" : ['a','b','c','g'] }, {"speed" : 1, "notes" : ['b','c','c','g'] }]
WEBCAM_SPEED = 3
class AlarmException(Exception):
    pass

class Game:
    def __init__(self):
        self.songs = ''

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
            raw_inp = None
            print '\nPrompt timeout. Continuing...'
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''

    def play_level(self, song):
        score = 0
        success_score = len(song["notes"]) * 0.8
        for note in song["notes"]:
            subprocess.call("afplay /Users/jinpark/Documents/code/emotiontracker/server/audio_files/{}1.wav".format(note), shell=True )
            input_base_chr = stdscr.getch()
            input_note = chr(input_base_chr)
            curses.nocbreak(); stdscr.keypad(0); curses.echo()
            curses.endwin()

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

    def start(self):
        self.songs = [{"speed" : 1, "notes" : ['a','b','c','g'] }, {"speed" : 1, "notes" : ['b','c','c','g'] }]
        for idx,song in enumerate(self.songs):
            print("level : {}".format(idx+1))
            passing = self.play_level(song)
            if not passing:
                print("You failed!!!!!!!!!!!!")
                exit()

    def run(self):
        t = threading.Thread(target=self.start)
        t.start()
