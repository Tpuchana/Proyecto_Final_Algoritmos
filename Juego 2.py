import pygame
import random

pygame.init()
ven_a = 1280
ven_h = 720
ventana = pygame.display.set_mode((ven_a, ven_h))
reloj = pygame.time.Clock()

class Pajarito:
    def __init__(self):     
        self.x = ven_a * 0.2
        self.y = ven_h * 0.5
        self.vel = 0
        self.salvel = ven_h*0.015
        self.grv = ven_h*0.00069
        self.jugador = pygame.Rect(self.x, self.y, ven_h*0.04, ven_h*0.04)


    def checkfordeath(self, obstacles):
        for obstacle in obstacles:
            if pajaro.jugador.colliderect(obstacle) or pajaro.jugador.colliderect(pygame.Rect(
                obstacle.x,
                obstacle.y-ven_h*1.25,
                obstacle.width,
                obstacle.height
            )):
                pygame.quit()
        
    def move(self):
        self.vel = self.vel+self.grv
        self.y = self.y+self.vel
        self.jugador.y = self.y

    
    def jump(self):
        self.vel = -self.salvel
        
 
                
        
class Obstaculos:
    def __init__(self):
        self.obstacles_list = []
        
    def generateobstacles(self):
        can_gen = True
        for obstacle in self.obstacles_list:
            if obstacle.x > ven_a*0.75:
                can_gen = False
        
        if can_gen:
            self.obstacles_list.append(
                pygame.Rect(
                    ven_a,
                    random.randint(ven_h*0.50, ven_h*0.8),
                    ven_a*0.075,
                    ven_h
                )
            )
                 
    def scrollscene(self):
        for obstacle in self.obstacles_list:
            obstacle.x -= ven_a*0.0025
            if obstacle.x < 0 - obstacle.width:
                self.obstacles_list.remove(obstacle)
        
manager = Obstaculos()
pajaro = Pajarito()

game_resumed = False

while True:
    reloj.tick(60)
    ventana.fill((31, 176, 202))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or pygame.K_w:
                pajaro.jump()
                game_resumed = True
    
    if game_resumed:
        manager.generateobstacles()
        manager.scrollscene()
        pajaro.move()
        pajaro.checkfordeath(obstacles=manager.obstacles_list)
    
    pygame.draw.rect(ventana, (228, 255, 0), pajaro.jugador)
    for obstacle in manager.obstacles_list:
        pygame.draw.rect(ventana, (0, 255, 31), obstacle)
        pygame.draw.rect(ventana, (0, 255, 0), pygame.Rect(
            obstacle.x,
            obstacle.y-ven_h*1.25,
            obstacle.width,
            obstacle.height
        ))

    pygame.display.update()
    