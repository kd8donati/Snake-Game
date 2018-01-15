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
direction='RIGHT'
changeto=direction

#Game over function
def gameOver():
    myFont = pygame.font.SysFont('arial',70)
    GOsurface = myFont.render('Game Over',True, red)
    GOrect= GOsurface.get_rect()
    GOrect.midtop=(360, 20)
    playSurface.blit(GOsurface,GOrect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()#for game
    sys.exit()#for console

#main logic for Events of the game

while True:      #or can use "while 1:"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()#for game
            sys.exit()#for console
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto='RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto='LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto='UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto='DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
                
    #validation of direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction='RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction='RIGHT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction='UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction='DOWN'
    
    if direction == 'RIGHT':
        snakePosi[0]+=10
    if direction == 'LEFT':
        snakePosi[0]-=10
    if direction == 'UP':
        snakePosi[1]-=10
    if direction == 'DOWN':
        snakePosi[1]+=10
    
    
    #SNAKE BOFY MECHANISM
    snakeBody.insert(0, list(snakePosi))
    if snakePosi[0]==foodPosi and snakePosi[1]==foodPosi[1]:
        foodSpawn=False
    else:
        snakeBody.pop()
    if foodSpawn == False:
        foodPosi=[random.randrange(1,72)*10,random.randrange(1,46)*10]
        #foodSpawn=True
        










    

