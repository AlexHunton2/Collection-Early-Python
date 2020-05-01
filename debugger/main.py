import pygame
from robot import *
import math

pygame.init()

width = 800
height = 500

field = pygame.image.load("debugger/img/field.png")
screen = pygame.display.set_mode((width, height))
screen.fill((225, 225, 225))

running = True
curveMode = True
lastx, lasty = 0, 0
storex, storey = 0, 0
robox, roboy = 0, 0
angle = 0
speed = 1
distBetween = 20
red = (255, 0, 0)
WHITE = (255, 255, 255)
blackdraw = []
reddraw = []
points = []
first = True
follow = False

all_sprites_list = pygame.sprite.Group()
robot = Robot("debugger/img/robot.png", WHITE)
robot.angle_change = 0
all_sprites_list.add(robot)

#Definitions
def xy(event):
    global lastx, lasty
    lastx, lasty = event[0], event[1]

def quadConvo(num):
    num = (((num * 12)/500) - 6)
    return num
    
def addLine(event):
    global lastx, lasty, storex, storey, first, points
    #blackdraw.append((event[0], event[1]))
    lastx, lasty = event[0], event[1]
    diffx, diffy = event[0] - storex, event[1] - storey
    if first:
        storex, storey = event[0], event[1]
        first = False
    if (diffx > distBetween) or (diffx < -distBetween) or (diffy > distBetween) or (diffy < -distBetween):
        storex, storey = event[0], event[1]
        reddraw.append((event[0], event[1]))
        points.append((quadConvo(event[0]), -quadConvo(event[1])))

def redraw(x, y):
    screen.blit(field, (0, 0))
    pygame.draw.line(screen, (0, 0, 0), (0, 250), (500, 250), 3)
    pygame.draw.line(screen, (0, 0, 0), (250, 0), (250, 500), 3)
    font = pygame.font.SysFont("monospace", 24)
    if curveMode:
        mode = font.render("Mode: Curve Mode", 18, (0,0,0))
    else:
        mode = font.render("Mode: Point Mode", 18, (0,0,0))
    xlabel = font.render("Robot X:" + str(round(quadConvo(x), 3)), 18, (0,0,0))
    ylabel = font.render("Robot Y:" + str(round(quadConvo(y), 3)), 18, (0,0,0))
    screen.blit(mode, (500, 20))
    screen.blit(xlabel, (500, 50))
    screen.blit(ylabel, (500, 100))

    #for i in blackdraw:
        #if ((blackdraw.index(i) % 1) == 0):
            #pygame.draw.ellipse(screen, (0, 0, 0), (i[0], i[1], 5, 5))
    for i in reddraw:
        try:
            pygame.draw.line(screen, (0, 0, 0), i, reddraw[reddraw.index(i)+1], 3)
        except IndexError:
            pass
        pygame.draw.ellipse(screen, red, (i[0]-5, i[1]-5, 10, 10))
    
clock = pygame.time.Clock()

while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            xy((pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            if mousex < 500 and not curveMode:
                addLine((mousex, mousey))
        if (event.type == pygame.MOUSEMOTION):
            if pygame.mouse.get_pressed()[0] == True:
                mousex, mousey = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                if mousex < 500 and curveMode:
                    addLine((mousex, mousey))
        if (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_SPACE:
                if follow:
                    follow = False
                else:
                    follow = True
            if event.key == pygame.K_b: 
                reddraw.pop(0)
            if event.key == pygame.K_v:
                if curveMode:
                    curveMode = False
                    point = []
                    reddraw = []
                else:
                    curveMode = True
                    point = []
                    reddraw = []
    if follow:
        try:
            xdiff = quadConvo(reddraw[0][0]) - quadConvo(robox)
            ydiff = quadConvo(reddraw[0][1]) - quadConvo(roboy)
            angle = (math.degrees(math.atan2(ydiff, xdiff)) - 90)
            robot.angle_change = angle
            #print(quadConvo(reddraw[1][0]))
            #print(quadConvo(robox))  
            #print(xdiff)
            print(angle)
        except:
            pass
        if len(reddraw) != 0:
            if robox < reddraw[0][0]:
                robox += speed
            if robox > reddraw[0][0]:
                robox -= speed
            if roboy > reddraw[0][1]:
                roboy -= speed
            if roboy < reddraw[0][1]:
                roboy += speed
    redraw(robox, roboy)
    robot.rect.x = robox - 25
    robot.rect.y = roboy - 25
    robot.update()
    all_sprites_list.draw(screen)

    clock.tick(60)

    pygame.display.update()