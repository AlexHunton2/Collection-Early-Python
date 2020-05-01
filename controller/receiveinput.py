import pygame

class GamePad:
    axisA = [0, 0]
    axisB = [0, 0]
    buttons = {"A":0, "B":0, "X":0, "Y":0, "LBUMP":0, "RBUMP":0, "BACK":0, "START":0}
    gamePadRun = True
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
    def endInputs(self):
        self.gamePadRun = False
        return pygame.quit()
    def setAxisA(self, x, y):
        self.axisA = [x, y]
    def setAxisB(self, x, y):
        self.axisB = [x, y]
    def updateButton(self, button, value):
        possibleButtons = list(self.buttons.keys())
        for i in possibleButtons:
            if i == possibleButtons[button]:
                self.buttons.update({possibleButtons[button]:value})
    def getInputs(self):
        #Pygame events
            for event in pygame.event.get(): # User did something.
                if event.type == pygame.QUIT: # If user clicked close.
                    self.endInputs # Flag that we are done so we exit this loop.
            #Get a list of all joysticks connected
            joystick_count = pygame.joystick.get_count()

            for i in range(joystick_count):
                joystick = pygame.joystick.Joystick(i) 
                joystick.init()
                name = joystick.get_name()
                axes = joystick.get_numaxes()
                buttons = joystick.get_numbuttons()
                #only get correct controller 
                if i == 0:
                    for j in range(axes):
                        axis = joystick.get_axis(j)
                        #print("Joystick: {} Axis: {} Value: {}".format(i, j, axis))
                        if j == 0:
                            self.setAxisA(axis, self.axisA[1])
                        if j == 1:
                            self.setAxisA(self.axisA[0], -axis)
                        if j == 3:
                            self.setAxisB(self.axisB[0], -axis)
                        if j == 4:
                            self.setAxisB(axis, self.axisB[1])
                    for l in range(8):
                        button = joystick.get_button(l)
                        self.updateButton(l, button)
                        
            return self.axisA, self.axisB, self.buttons

        
