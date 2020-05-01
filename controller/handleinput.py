from receiveinput import GamePad
from inputs import get_key
import pygame

gamepad = GamePad()

def main():
    while gamepad.gamePadRun:
        inputs = gamepad.getInputs()
        print(inputs[2])
        if int(inputs[0][0]) == -1:
            print("LEFT")
        if int(inputs[0][0] + .1) == 1:
            print("RIGHT")
        if inputs[2]['START'] == 1:
            print("ENDED")
            gamepad.endInputs()
    gamepad.endInputs()
    
if __name__ == "__main__":
    main()