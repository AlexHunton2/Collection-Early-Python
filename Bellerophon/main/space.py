def Main():
    ulti.talkToMe("I am listening")
    command = ulti.listen()
    print(command)
    if command == "repeat after me":
        ulti.talkToMe("I will repeat after you")
        repeated = ulti.listen()
        ulti.talkToMe(repeated)
    else:
        print("Error")
    return command