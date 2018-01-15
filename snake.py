import pygame, sys, random, time    #Libraries imported

check_errors=pygame.init()  #(6,0)
if check_errors[1]>0:
    print(" Had {0} initializing errors exiting....".format(check_errors[1]))
    sys.exit(-1)
else:
    print("Pygame successfully initialized")

#Creating play surface
playSurface=pygame.display.set_mode((720,480))
pygame.display.set_caption('Snake')

                                #time.sleep(5)
#colors
red = pygame.Color(255,0,0) #Game over
green = pygame.Color(0,255,0)#Snake
black = pygame.Color(0,0,0)#score
white = pygame.Color(255,255,255)#background
brown = pygame.Color(165,42,42)#food

#fps Controller
fpsController=pygame.time.Clock()

#Sanke Position and Body
snakePosi=[100,200]
snakeBody=[[100,50],[90,50],[90,50]]

#Food
foodPosi=[random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn=True

#Direction 
direction='right'
changeto=direction

#Game over function
def gameOver():
    myFont = pygame.font.SysFont('arial',70)
    GOsurface = myFont.render('Game Over',True, red)
    GOrect= GOsurface.get_rect()
    GOrect.midtop=(360, 20)
    playSurface.blit(GOsurface,GOrect)
    pygame.display.flip()
    
gameOver()
time.sleep(5)
