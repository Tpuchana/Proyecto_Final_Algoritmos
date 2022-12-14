import pygame
from random import random


pygame.init()
win_w = 1280
win_h = 720
win = pygame.display.set_mode((win_w, win_h))
clock = pygame.time.Clock()

class Bird:
    def __init__(self):
        self.x = win_w * 0.2
        self.y = win_h * 0.5
        self.vel = 0
        self.salvel = win_h*0.0075
        self.grv = win_h*0.00038
        self.body = pygame.Rect(self.x, self.y, win_h*0.05, win_h*0.05)
    
    def jump(self):
        self.vel = -self.salvel

    def move(self):
        self.y = self.y + self.vel
        self.vel = self.vel + self.grv
        self.body.y = self.y
    
    def checkfordeath(self, obstacles):
        for obstacle in obstacles:
            if bird.body.colliderect(obstacle) or pygame.Rect(
            obstacle.x,
            obstacle.y-win_h*1.25,
            obstacle.width,
            obstacle.height
            ):
                pygame.quit()
    
class ObstaclesManager:
    def __init__(self):
        self.obstacles_list = []

    def generateobstacles(self):
        can_gen = True
        for obstacle in self.obstacles_list:
            if obstacle.x > win_w*0.8:
                can_gen = False
        
        if can_gen:
            self.obstacles_list.append(
                pygame.rect(
                    win_w,
                    random.random.randint(win_h*0.25, win_h*0.8),
                    win_w*0.01,
                    win_h
                )
            )

    
    def scrollscene(self):
        for obstacle in self.obstacles_list:
            obstacle.x = obstacle.x-(win_w*0.0025)
            if obstacle.x < 0 - obstacle.width:
                self.obstacles_list.remove(obstacle)

manager = ObstaclesManager()
bird = Bird()

game_resumed = False

while True:
    clock.tick(60)
    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()
                game_resumed = True
    
    
    manager.generateobstacles()
    manager.scrollscene()
    bird.move()
    bird.checkfordeath(obstacles=manager.obstacles_list)

    pygame.draw.rect(win, (255, 255, 255), bird.body)
    for obstacle in manager.obstacles_list:
        pygame.draw.rect(win, (255, 0, 0), obstacle)
        pygame.draw.rect(win, (255, 0, 0), pygame.Rect(
            obstacle.x,
            obstacle.y-win_h*1.25,
            obstacle.width,
            obstacle.height


        ))
            
        
    pygame.display.update()




        
