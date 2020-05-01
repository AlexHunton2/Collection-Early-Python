import pygame

class Robot(pygame.sprite.Sprite):
     
    def __init__(self, filename, colorkey):
        super().__init__() 
 
        self.original_image = pygame.image.load(filename).convert()
        self.image = self.original_image

        self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect()
         
        self.angle = 0
        self.angle_change = 0
         
    def update(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.angle = self.angle_change
        self.angle = self.angle % 360
    
    def getAngle(self):
        return self.angle