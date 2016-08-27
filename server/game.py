import signal
import subprocess
import curses
import curses.ascii
import time
import threading

stdscr = curses.initscr()
curses.cbreak()
# curses.noecho()
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
            # send(note)
            # threading.Thread(target=play_audio, kwargs={'audio_file_location': 'audio_files/ox.wav'}).start()
            subprocess.call("afplay /Users/jinpark/Documents/code/emotiontracker/server/audio_files/{}1.wav".format(note), shell=True )
            # input_note = self.nonBlockingRawInput("note: ", song["speed"] * WEBCAM_SPEED)

            # try:
            #     while True:
            input_base_chr = stdscr.getch()
            # print(input_base_chr)
            input_note = chr(input_base_chr)
            curses.nocbreak(); stdscr.keypad(0); curses.echo()
            curses.endwin()

            # print(input_note)
                    # if input_note != -1:
                    #     stdscr.addstr("%s was pressed\n" % input_note)
                    # stdscr.addstr("time() == %s\n" % time.time())
            # finally:
            #     curses.endwin()
            # input_note = stdscr.getch()
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


    # g = Game()
    # g.start([{"speed" : 1, "notes" : ['d','d','e','e'] }, {"speed" : 1, "notes" : ['b','c','c','g'] }])
