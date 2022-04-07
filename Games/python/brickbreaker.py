import pygame
import sys

class ball():
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = 10
        self.yvel = 5

    def draw(self, surface):
        radius = 5
        center = (self.xpos, self.ypos)
        pygame.draw.circle(surface, (0,255,0), center, radius)
    
    def move(self):
        self.ypos += 5

class brick():
    def __init__(self, xpos, ypos, color):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.xpos, self.ypos, 30, 15))



class paddle():

    xpos = 230

    def __init__(self, color):
        self.color = color
        self.width = 50
        self.height = 10

    def move(self, screen_width):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            mouse_move = pygame.mouse.get_rel()
            x_change = mouse_move[0]

            new_x = self.xpos + x_change
            if((new_x <= (screen_width - self.width)) and (new_x >= 0)):
                self.xpos = new_x
                   
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.xpos, 390, self.width, self.height))


def redrawWindow(surface):
    global pad, nBall, bricks
    surface.fill((0,0,0))
    pad.draw(surface)
    nBall.draw(surface)
    for i, lis in enumerate(bricks):
        for b in range(len(lis)):
            lis[b].draw(surface)

    pygame.display.update()


def main():
    pygame.init()
    global pad, nBall, bricks
    width = 900
    height = 400

    win = pygame.display.set_mode((width, height))
    pygame.mouse.set_pos(255, 395)
    pad = paddle((255,255,255))
    nBall = ball(245, 195)
    bricks = []
    for i in range(0, 255, 16):
        bricklist = []
        for j in range(255-i, 255+i, 32):
            nBrick = brick(j, i, (0,0,255))
            bricklist.append(nBrick)
        bricks.append(bricklist)

    clock = pygame.time.Clock()

    flag = True
    while flag:
        pad.move(width)
        nBall.move()
        redrawWindow(win)
        pygame.time.delay(30)
        clock.tick(30)
        string = "Python"

    print(string[1:5])

main()