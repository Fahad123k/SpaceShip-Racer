import pygame
import time
import random
 
pygame.init()

############ 

#############
# golbal variables
display_width = 800  
display_height = 600

space_width = 103
space_height = 107

thing_width = 99
thing_height = 107

#Friction is in space is less
friction=5
##############
#Some colors
black = (100,100,100)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

#Stage Colors
snow_color=(20,50,255)
grey_color=(60,60,60)
desert_color=(255,100,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
 
score_color = (5,250,255)
 



# Blast image
blast=pygame.image.load('blast.png')

background=pygame.image.load("bk.jpg")
#stages background
sky=pygame.image.load('sky.jpg')
water=pygame.image.load('water1.jpg')
space=pygame.image.load('space.jpg')

# by Defauly Stage is space
stage=space
#images of Enemy and SpaceCrafy

spacecraft = pygame.image.load('spacecraft.png')
thing = pygame.image.load('enemy.png')
gameIcon = pygame.image.load('spacecraft.png')
#default value

 # Set Display height and Width
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Space Racer')
clock = pygame.time.Clock()
pygame.display.set_icon(gameIcon)


pause = False
#crash = True

#Score Fuction
def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged: "+str(count), True,score_color)
    gameDisplay.blit(text,(0,0))
#Enemy Function
def things(thingx, thingy):
    gameDisplay.blit(thing,(thingx, thingy))

#Space Ship Function
def spaceship(x,y):
    gameDisplay.blit(spacecraft,(x,y))
 
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def StageRoad():
    global stage,friction
    stage=sky
    friction=1.5
    print("road",stage)

def StageSnow():
    global stage, friction
    stage=space
    friction=5

    print("Space.",stage)

def StageDesert():
    global stage,friction
    friction=2
    stage=water

    print("Water",stage)
 
def crash():
    ####################################
    pygame.mixer.music.load('collision.mp3')
    pygame.mixer.music.play(-1)

    ####################################
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    gameDisplay.blit(blast,(x-180,y-180))
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        
        #Button For Play Again Or Quit
        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        # Buttons for Stages
        button("Space!",345,400,100,30,snow_color,bright_green,StageSnow)
        button("Sky!",345,450,100,30,grey_color,bright_green,StageRoad)
        button("Water!",345,500,100,30,desert_color,bright_green,StageDesert)

        pygame.display.update()
        clock.tick(15) 

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    

def paused():
    ############
    pygame.mixer.music.pause()
    #############
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Button for Continue or Quit
        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)


        pygame.display.update()
        clock.tick(15)   


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        gameDisplay.blit(background,(-150,0))
        largeText = pygame.font.SysFont("comicsansms",100)
        TextSurf, TextRect = text_objects("Space Racer", largeText)
        TextRect.center = ((display_width/2),(display_height/2)-50)
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        #Stages
        button("Space!",345,400,100,30,snow_color,bright_green,StageSnow)
        button("Sky!",345,450,100,30,grey_color,bright_green,StageRoad)
        button("Water!",345,500,100,30,desert_color,bright_green,StageDesert)
        

        pygame.display.update()
        clock.tick(15)
        
        
    
    

    
def game_loop():
    global pause,x,y
    ############
    pygame.mixer.music.load('jazz.wav')
    pygame.mixer.music.play(-1)
    ############
    #initia position of a
    x = (display_width * 0.45)
    y = (display_height * .8)
 
    x_change = 0
 
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 6
    #thing_width = 50
    #thing_height = 50
 
    thingCount = 1
 
    dodged = 0
 
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
            # if no any key press then it goes slow left or Right
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = -friction
                if event.key == pygame.K_RIGHT:
                    x_change = friction
 
        x += x_change
        gameDisplay.blit(stage,(0,0))
       
 
        things(thing_startx, thing_starty)
 
 
        
        thing_starty += thing_speed
        spaceship(x,y)
        things_dodged(dodged)
        #xar restart
        #crash from wall both side
        if x > display_width - space_width :
            x=0
        if x < 0:
            x=display_width-space_width 
 
        if thing_starty > display_height:
            thing_starty =  - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            # thing_width += (dodged * 1.2)
 
        if y < thing_starty+thing_height-10:
            print('y crossover')
 
            if x > thing_startx and x < thing_startx + thing_width-3 or x+space_width > thing_startx and x + space_width < thing_startx+thing_width:
                print('x crossover')
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
