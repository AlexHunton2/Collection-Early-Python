import pygame

def testlevel():
    grid = []
    winy = 19
    winx = 1 
    offset = 4
    spawnx = 64
    spawny = 64
    for row in range(20):
        grid.append([])
        for column in range(30):
            grid[row].append(0)
    for x in range(20):
        grid[0][x] = 1
        grid[19][x] = 1
        grid[x][0] = 1
        grid[x][19] = 1
        grid[6][16] = 1
    grid[1][19] = 4
    return grid, winy, winx, spawnx, spawny

def firstlevel():
    grid = []
    winx = 5
    winy = 17
    offset = 4
    spawnx = 64
    spawny = 138
    for row in range(20):
        grid.append([])
        for column in range(30):
            grid[row].append(0)
    for x in range(16):
        grid[offset][x+2] = 1
        grid[offset+2][x+2] = 1
    for x in range(3):
        grid[x+4][1] = 1
        grid[x+4][18] = 1
    grid[winx][winy] = 4
    return grid, winy, winx, spawnx, spawny

def secondlevel():
    grid = []
    winy = 19
    winx = 1 
    offset = 4
    spawnx = 64
    spawny = 138
    for row in range(20):
        grid.append([])
        for column in range(30):
            grid[row].append(0)
    for x in range(7):
        grid[offset][x+1] = 1
        grid[offset+6][x+1] = 1
    for x in range(6):
        grid[x+offset][1] = 1
    for x in range(2):
        grid[x+(offset-1)][8] = 1
        grid[x+(offset+6)][8] = 1
        grid[x+(offset-3)][17] = 1
    for x in range(9):
        grid[offset-2][x+8] = 1
    for x in range(12):
        grid[offset+8][x+8] = 1
        grid[x+1][offset+16] = 1
    for x in range(4):
        grid[offset-4][x+17] = 1
    grid[winx][winy] = 4
    return grid, winy, winx, spawnx, spawny

def thirdlevel():
    grid = []
    winy = 15
    winx = 3 
    offset = 4
    spawnx = 64
    spawny = 164
    rewardx = 7
    rewardy = 7
    for row in range(20):
        grid.append([])
        for column in range(30):
            grid[row].append(0)
    for x in range(3):
        grid[x+5][1] = 1
        grid[5][x+1] = 1
        grid[2][x+14] = 1
        grid[x+2][16] = 1
        grid[4][x+16] = 1
    for x in range(4):
        grid[7][x+1] = 1
        grid[4][x+3] = 1
        grid[4][x+10] = 1
    for x in range(15):
        grid[8][x+4] = 1
    for x in range(5):
        grid[3][x+6] = 1
        grid[x+2][14] = 1
        grid[x+4][18] = 1
    grid[winx][winy] = 4
    grid[rewardx][rewardy] = 5
    return grid, winy, winx, spawnx, spawny, rewardx, rewardy
