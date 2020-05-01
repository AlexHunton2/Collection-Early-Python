import pygame, time
from levels import *

pygame.init()
win = pygame.display.set_mode((750,700))
myfont = pygame.font.SysFont("monospace", 15)
pygame.display.set_caption("Thin Ice")

BLACK = (0, 0, 0)
WHITE = (181, 235, 245)
GREEN = (51, 102, 153)
RED = (255, 0, 0)
BLUE = (0, 0 , 255)
YELLOW = (204,204,204) 
PURPLE = (148, 0, 211)

grid_Size = 25

boundID = 1
iceID = 2
waterID = 3
winID = 4
rewardID = 5

levels = ["testlevel","level1","level2","level3","level4"]
count = 1

grid = 0
winx = 0
winy = 0
spawnx = 0
spawny = 0
player = 0
rewardx = 0
rewardy = 0

score = 0
permscore = 0

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
    
    def render(self):
        pygame.draw.circle(win, RED, (self.x, self.y), 12, 12)


def loadlevel():
    currentlevel = levels[count]
    if currentlevel == "testlevel":
        package = testlevel()
        return package
    elif currentlevel == "level1":
        package = firstlevel()
        return package
    elif currentlevel == "level2":
        package = secondlevel()
        return package
    elif currentlevel == "level3":
        package = thirdlevel()
        return package

def unpackpackage():
    loadedvalues = loadlevel()
    global grid
    grid = loadedvalues[0]
    global winx
    winx = loadedvalues[1]
    global winy
    winy = loadedvalues[2]
    global spawnx
    spawnx = loadedvalues[3]
    global spawny
    spawny = loadedvalues[4]
    try:
        global rewardx
        rewardx = loadedvalues[5]
        global rewardy
        rewardy = loadedvalues[6]
    except IndexError:
        pass

def renderlevel():
    unpackpackage()
    global player
    player = Player(spawnx, spawny)
    player.render()
    for row in range(20):
            for column in range(30):
                color = WHITE
                if grid[row][column] == boundID:
                    color = GREEN
                if grid[row][column] == iceID:
                    color = WHITE
                if grid[row][column] == waterID:
                    color = BLUE
                if grid[row][column] == winID:
                    color = RED
                if grid[row][column] == rewardID:
                    color = PURPLE

                pygame.draw.rect(win, color, ((25 * column), (25 * row), 25, 25))
                pygame.display.update()

def updatescore():
    label = myfont.render(("Score: " + str(score)), 1, (0,0,0))
    pygame.draw.rect(win, YELLOW, (30,600, 500, 20))
    win.blit(label,(30,600))

def shortcutrender():
    renderlevel()
    player.render()
    pygame.display.update()

def move(m):
    global score
    global permscore
    global rewardx
    global rewardy
    cx = int(player.x / grid_Size)
    cy = int(player.y / grid_Size)
    left = grid[cy][cx-1]
    right = grid[cy][cx+1]
    up = grid[cy-1][cx]
    down = grid[cy+1][cx]
    #boundries
    if m == "left":
        if not (left == boundID or left == waterID):
            player.x-=grid_Size
            score += 50
            updatescore()
    elif m == "right":
        if not (right == boundID or right == waterID):
            player.x+=grid_Size
            score += 50
            updatescore()
    elif m == "up":
        if not (up == boundID or up == waterID):
            player.y-=grid_Size
            score += 50
            updatescore()
    elif m == "down":
        if not (down == boundID or down == waterID):
            player.y+=grid_Size
            score += 50
            updatescore()
    #updated variables due to movenment
    if not (cx == int(player.x / grid_Size) and cy == int(player.y / grid_Size)):
        grid[cy][cx] = waterID
    #update variables
    cx = int(player.x / grid_Size)
    cy = int(player.y / grid_Size)
    left = grid[cy][cx-1]
    right = grid[cy][cx+1]
    up = grid[cy-1][cx]
    down = grid[cy+1][cx]
    #check win
    if (cx == rewardx and cy == rewardy):
        score += 500
        updatescore()
        grid[cx][cy] == iceID
        rewardx = 50
        rewardy = 50
    try:
        if (cx == winx and cy == winy):
            global count
            count += 1
            shortcutrender()
            permscore = score
            updatescore()
            return
    except TypeError:
        print("End of Levels")
        count -= 1
        shortcutrender()
        permscore = score
        updatescore()
    #check lose
    if ((left == boundID) or (left == waterID)) and ((right == boundID) or (right == waterID)) and ((up == boundID) or (up == waterID)) and ((down == boundID) or (down == waterID)):
        shortcutrender()
        score = permscore
        updatescore()

    #rendering
    for row in range(20):
            for column in range(30):
                if grid[row][column] == waterID:
                    color = BLUE
                    pygame.draw.rect(win, color, ((25 * column), (25 * row), 26, 26))
                if grid[row][column] == iceID:
                    color = WHITE
                    pygame.draw.rect(win, color, ((25 * column), (25 * row), 26, 26))
                            
    player.render()
    pygame.display.update()
    
def Main():
    run = True
    win.fill((YELLOW))
    label = myfont.render(("Score: " + str(score)), 1, (0,0,0))
    win.blit(label,(30,600))
    shortcutrender()
    while run:
        global count
        pygame.time.delay(90)
        for event in pygame.event.get():
            ev = pygame.event.get()
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            move("right")
        if keys[pygame.K_LEFT]:
            move("left")
        if keys[pygame.K_UP]:
            move("up")
        if keys[pygame.K_DOWN]:
            move("down")
        if keys[pygame.K_1]:
            count = 0
            shortcutrender()
        if keys[pygame.K_2]:
            count = 1
            shortcutrender()
        if keys[pygame.K_3]:
            count = 2
            shortcutrender()
        if keys[pygame.K_4]:
            count = 3
            shortcutrender()
Main()
pygame.quit()