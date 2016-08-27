import signal

class AlarmException(Exception):
    pass

def alarmHandler(signum, frame):
    raise AlarmException

def nonBlockingRawInput(prompt='', timeout=5):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = raw_input(prompt)
        signal.alarm(0)
        return text
    except AlarmException:
        print '\nPrompt timeout. Continuing...'
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

songs = [{"speed" : 1, "notes" : ['a','b','c','g'] }, {"speed" : 1, "notes" : ['b','c','c','g'] }]

success_score = 4

WEBCAM_SPEED = 1

def play_level(song):
    score = 0
    success_score = len(song["notes"]) * 0.8
    for note in song["notes"]:
        # send(note)
        input_note = nonBlockingRawInput("note: ", note["speed"] * WEBCAM_SPEED)

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

for idx,song in enumerate(songs):
    print("level : {}".format(idx+1))
    passing = play_level(song)
    if not passing:
        print("You failed!!!!!!!!!!!!")
        exit()
