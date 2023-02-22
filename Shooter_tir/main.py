import pygame
pygame.init()
import os

os.environ["SDL_VIDEO_CENTERED"] = "1"

WIN_WIDTH = 900
WIN_HEIGHT = 600
FPS = 60
WHITE = (255,255,255)

def file_path(file_name):
    folder = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder, file_name)
    return path

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

pygame.mixer.music.load(file_path(r"sounds\sound_fon.mp3"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

music_shot = pygame.mixer.Sound(file_path(r"sounds\shot.ogg"))
music_shot_out = pygame.mixer.Sound(file_path(r"sounds\shot_out.ogg"))

fon = pygame.image.load(file_path(r"images\Stall\bg_green.png"))
fon = pygame.transform.scale(fon, (WIN_WIDTH, WIN_HEIGHT)).convert()

class Scope():
    def __init__(self):
        self.rect = pygame.Rect(0,0,40,40)
        self.image = pygame.image.load(file_path(r"images\HUD\crosshair_outline_large.png"))
        self.image = pygame.transform.scale(self.image,(40, 40)).convert_alpha()

play = True
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    if play:
        window.blit(fon,(0,0))



    






    clock.tick(FPS)
    pygame.display.update() 