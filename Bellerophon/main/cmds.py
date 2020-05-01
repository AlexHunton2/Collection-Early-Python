from run import KEON

class Commands:

    def __init__(self, command)
        self.command = KEON
    
    def repeatcommand():
        try:
            if self.command == "repeat after me":
                talkToMe("I will repeat after you")
                repeated = listen()
                talkToMe(repeated)
            else:
                talkToMe("I'm sorry, but that is not a valid command")
        except sr.UnknownValueError:
            talkToMe("Oops Didn't Catch That!")